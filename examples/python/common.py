"""Hosted Actor API helpers. Start once; safely retry only reads via the SDK."""
import json
import os
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler
from apify_client import ApifyClient

ACTOR_ID = 'datascraperes/wayfair-scraper'
ROOT = Path(__file__).resolve().parents[2]

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def credentials():
    token = os.environ.get('APIFY_API_TOKEN')
    if not token:
        raise RuntimeError('Set APIFY_API_TOKEN before calling the hosted Actor.')
    return token, os.environ.get('APIFY_API_BASE_URL', 'https://api.apify.com').rstrip('/')

def client():
    token, base = credentials()
    return ApifyClient(token, api_url=base)

def start_once(actor_input, maximum_usd=0.02):
    token, base = credentials()
    query = urlencode({'timeout':180, 'memory':256, 'maxTotalChargeUsd':maximum_usd})
    url = base+'/v2/acts/'+ACTOR_ID.replace('/', '~')+'/runs?'+query
    request = Request(url, data=json.dumps(actor_input).encode('utf-8'), method='POST',
                      headers={'Authorization':'Bearer '+token, 'Content-Type':'application/json'})
    # No retry and no redirect for a potentially paid start. If the response is
    # lost, inspect recent runs in Console; do not repeat this request blindly.
    with build_opener(NoRedirect()).open(request, timeout=45) as response:
        run = json.load(response)['data']
    print('Started run '+run['id'], flush=True)
    return run['id']

def wait_for_dataset(run_id):
    api = client()
    run = api.run(run_id).wait_for_finish(wait_duration=timedelta(seconds=210))
    status = getattr(run.status, 'value', run.status) if run else None
    if status != 'SUCCEEDED':
        raise RuntimeError('Run '+run_id+' did not succeed; inspect it without starting another run.')
    summary = api.key_value_store(run.default_key_value_store_id).get_record('SUMMARY')
    value = summary['value'] if isinstance(summary, dict) else summary.value
    print('Collection outcome: '+value['outcome']+'; records: '+str(value['records']), flush=True)
    if not value.get('complete'):
        raise RuntimeError('Run '+run_id+' has incomplete collection or input warnings. Review SUMMARY; saved rows remain accessible.')
    return run.default_dataset_id

def iter_rows(dataset_id, page_size=100):
    api = client()
    offset = 0
    while True:
        page = api.dataset(dataset_id).list_items(offset=offset, limit=page_size, clean=True)
        if not page.items:
            return
        yield from page.items
        offset += len(page.items)

def sample_input():
    return json.loads((ROOT/'data/sample-input.json').read_text(encoding='utf-8'))
