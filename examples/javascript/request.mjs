// Node.js 22+. One paid start, then read-only polling and paginated export.
import { readFile } from 'node:fs/promises';
import { setTimeout as delay } from 'node:timers/promises';
const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN');
const base = (process.env.APIFY_API_BASE_URL || 'https://api.apify.com').replace(/\/$/, '');
const input = JSON.parse(await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));
async function request(path, options = {}) {
  const response = await fetch(base+'/v2/'+path, {
    ...options, redirect:'error', signal:AbortSignal.timeout(45000),
    headers:{Authorization:`Bearer ${token}`,'Content-Type':'application/json'},
  });
  if (!response.ok) throw new Error(`API request failed (${response.status}); inspect Console before repeating a start.`);
  return response.json();
}
// A failed/lost start is never automatically retried.
const { data: started } = await request('acts/datascraperes~wayfair-scraper/runs?timeout=180&memory=256&maxTotalChargeUsd=0.02', {method:'POST',body:JSON.stringify(input)});
console.log('Started run '+started.id);
const deadline = Date.now()+210000;
let run = started;
while (['READY','RUNNING','ABORTING','TIMING-OUT'].includes(run.status) && Date.now()<deadline) {
  await delay(1000);
  run = (await request('actor-runs/'+started.id)).data;
}
if (run.status !== 'SUCCEEDED') throw new Error('Run '+started.id+' did not succeed; inspect it without starting another run.');
const summary = await request('key-value-stores/'+run.defaultKeyValueStoreId+'/records/SUMMARY');
if (!summary.complete) throw new Error('Collection incomplete or input warnings: inspect SUMMARY. Saved rows remain available.');
const rows = [];
for (let offset=0; ; ) {
  const page = await request(`datasets/${run.defaultDatasetId}/items?clean=true&offset=${offset}&limit=100`);
  if (!page.length) break;
  rows.push(...page);
  offset += page.length;
}
console.log(JSON.stringify(rows,null,2));
