# Product-data workflows

## Look up product specifications

Use `mode: products`, `productUrls: ["W009559366"]` and `maxItems: 1` for a small US lookup.
Use a URL from the correct storefront when you need market detection. Direct product rows
can have fewer listing fields than category/keyword results.

## Batch keyword product collections

Run [batch_keyword_search.py](../examples/python/batch_keyword_search.py) for two separate,
sequential three-item requests. It stops on an incomplete result and caps each run separately.
Change `market` and terms together; do not assume product IDs are shared across storefronts.

## Check stock for a delivery area

Use `mode: inventory`, product identifiers for that market and a compatible `postalCode`,
such as10001 for US, M5V2T6 for Canada or SW1A1AA for UK. Unknown stock is not evidence of zero stock.

## Export a category price snapshot

Use a category URL/ID with a record cap, then run the [CSV exporter](../examples/python/export_products_csv.py)
with the existing Dataset ID. Keep storefront, currency and timestamp alongside prices.
To compare snapshots, start a new run; resuming a run reuses its verified saved rows.
