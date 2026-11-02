# FAQ

## Does a successful run always mean results were collected?

No. Inspect SUMMARY. Invalid selections finish with warnings and may have zero rows.
A mixed request can preserve verified rows and report a partial outcome. The examples check
`complete` and stop for attention instead of silently returning an empty success.

## What happens with an invalid category filter?

The filter and its option must belong to the target listing/market. Unknown values warn and
skip that listing without delivering or charging a result. Filters are never removed to
broaden the search. Unavailable option metadata is a source problem, not proof of bad input.

## Can I collect every product or every variant?

The cap is1–500 unique rows across the request, with at most40 listing pages of up to24 cards
per input. Source limits, source changes and filtering can reduce the count. Reaching a page
limit before source end is partial. Exhaustive catalog/variant coverage is not promised.

## Are descriptions and dimensions always available?

No. Enable `includeDetails` for category/keyword listings. Optional detail failure preserves
the base listing and reports partial collection. Values and units remain as supplied by Wayfair.

## Is the hosted service free?

It uses the published event prices. Apify's available plan credit can fund small trials;
check [Actor pricing](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata) and [platform pricing](https://apify.com/pricing?fpr=edudata). Later Dataset reads can also
consume platform usage. This repository's MIT license does not waive hosted service charges.

## Should I retry a start after a network error?

First inspect recent runs in Console. A lost response can still have created a paid run.
The examples issue one start without automatic retries, print acknowledged run IDs, and use
read-only polling/pagination afterward. Poll/export failure does not require another Actor run.

## Can I export nested fields to CSV?

The included exporter selects common scalar columns. Keep JSON for nested descriptions,
dimension groups and specifications, or define a flattening policy for your own downstream tool.
