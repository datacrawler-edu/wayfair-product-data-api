# Wayfair product data API: Python examples and CSV exports

Collect **Wayfair prices, stock and product specifications** through the hosted
[Wayfair Scraper](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata), then use the results in your own data workflow.
This repository provides integration examples and an output-format reference.
The MIT license covers these guides and examples; hosted Actor usage follows its Store terms and pricing.

## What this repository helps you do

- Retrieve product details from a Wayfair URL or SKU.
- Collect category products or keyword listings across US, Canada and UK.
- Add descriptions, dimensions and specifications to listing rows.
- Export an existing Dataset to CSV without launching another scraping run.

## Example result

This preview is taken from a real listing. The [complete sample](data/sample-output.json)
preserves every field of one representative item from a three-result request;
[sample-output.csv](data/sample-output.csv) is a selected-column projection.

```json
{
  "sku": "W119744972",
  "name": "65.3\" Convertible Corduroy Futon Sofa Bed With Adjustable Backrest & Solid Wood Leg, Sleeper Sofa Loveseat For Small Spaces, Apartment Or Office",
  "price": 209.99,
  "currency": "USD",
  "stockStatus": "IN_STOCK",
  "detailsFetched": true
}
```

## Run without code

1. Open [Wayfair Scraper on Apify](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata).
2. Choose Product details and add product URLs/SKUs, or choose Category products or Products by keyword.
3. Set the market for bare identifiers, a small Maximum records value and any listing options.
4. Click Start, inspect the Dataset and read SUMMARY for warnings or partial collection.
5. Export JSON, CSV or Excel from Console.

The [no-code guide](docs/no-code-guide.md) explains the modes and filter form.

## Try it with Apify's free plan

Apify currently includes $5 in monthly prepaid usage on its Free plan, with no credit card
required to start. A small trial uses available credit; it is not unlimited free scraping.
Unused credit expires with the billing cycle. Review [current Apify pricing](https://apify.com/pricing?fpr=edudata) before a larger workflow.

## Quick start for developers

Use Python3.11+ and install the pinned API client:

```bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/collect_products.py
```

PowerShell token setup: `$env:APIFY_API_TOKEN = "your-token"`.
Keep tokens out of source files and Git. Run commands from the repository root.
The primary example starts once with a $0.02 cap, prints its run ID, polls through the SDK,
checks SUMMARY and reads all Dataset pages. A lost start response is not automatically retried.

## Input example

This small category request matches the representative output's collection:

```json
{
  "mode": "category",
  "categoryUrls": [
    "413892"
  ],
  "includeDetails": true,
  "maxItems": 3,
  "filters": [
    {
      "filterId": "69278",
      "optionId": "8"
    }
  ]
}
```

Use [full-input.json](data/full-input.json) for all fifteen supported keys and
the [input reference](docs/input-reference.md) for their interactions.

## Request examples

- [cURL start, status and Dataset reads](examples/curl-request.md).
- [Python single request](examples/python/collect_products.py).
- [Python sequential keyword batch](examples/python/batch_keyword_search.py).
- [Python existing-Dataset CSV export](examples/python/export_products_csv.py).
- [JavaScript request and pagination](examples/javascript/request.mjs): `node examples/javascript/request.mjs`.

Every live start can incur charges. The two-keyword example has a separate $0.02 cap per run;
it is not one shared budget. If a start response is lost, check Console before repeating it.

## Output fields

| Field | Meaning |
|---|---|
| `recordType`, `market`, `sku`, `variantId` | Type, storefront and available product identity |
| `name`, `brand`, `url` | Product label and source link |
| `price`, `wasPrice`, `currency` | Available price values in the storefront currency |
| `stockStatus`, `availableQuantity` | Available stock fields; values vary by mode |
| `rating`, `reviewCount` | Listing rating and review count, not individual reviews |
| `description`, `dimensions`, `specifications`, `materials` | Product content when available |
| `detailsFetched`, `scrapedAt` | Detail-enrichment marker and collection timestamp |

See the [output guide](docs/output-reference.md). Null values are retained in JSON;
do not interpret missing stock or price as zero.

## Common use cases

The [workflow guide](docs/use-cases.md) covers a product lookup, a keyword batch,
stock by postal code and category price exports. SKUs are market-specific.

## Export Wayfair category prices to CSV

Start a category collection, copy its Dataset ID from Console and run:

```bash
python examples/python/export_products_csv.py YOUR_DATASET_ID --output data/exported-products.csv
```

This command reads an existing Dataset and creates no new Actor run. It exports selected
scalar columns; use JSON for nested dimensions and specifications.

## Retrieve Wayfair dimensions and specifications with Python

For category or keyword listings, set `includeDetails` to true. Preserve `sku`, `variantId`,
`market` and `scrapedAt` when joining records. Product weights and dimension labels retain
the source's units; product weight is not weight capacity. Direct product rows can omit
listing-only brand, ratings or stock fields.

## FAQ

Read [the FAQ](docs/faq.md) for empty results, filter warnings, completion and exports.
A successful platform run can still have `complete: false`; the examples inspect SUMMARY
and stop without starting another run when collection needs attention.

## Limits and pricing

One `product` event is charged for each verified delivered Dataset row: product, listing,
search-resolution or stock. Detail enrichment is part of the same row. Rejected input
selections produce no result event. This Actor has no separate detail/startup fee or Actor
usage surcharge. Independent platform actions such as later Dataset reads follow Apify's pricing.

| Tier | USD per delivered event | Equivalent per1,000 events |
|---|---:|---:|
| FREE |0.001|1.00|
| BRONZE |0.0009|0.90|
| SILVER |0.0008|0.80|
| GOLD |0.00075|0.75|
| PLATINUM |0.00075|0.75|
| DIAMOND |0.00075|0.75|

Check the current [Actor pricing](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata) before use. The run limit is1–500 unique rows,
with up to200 product identifiers or20 category URLs/keywords. Source availability and
filtering can yield fewer rows. See [limits and completion details](docs/faq.md).

## Hosted version

[Open Wayfair Scraper on Apify](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata) for the maintained hosted service, saved results,
input form and API tab. These examples call that service from your own programs.

## Responsible use

Use public catalog data lawfully and respect Wayfair's terms and applicable privacy rules.
Confirm prices and availability before relying on a purchase decision. This project is
independent of and not endorsed by Wayfair.

## Support

For example-code issues, [open a GitHub issue](https://github.com/datacrawler-edu/wayfair-product-data-api/issues)
with sanitized input and the command used. For hosted execution issues, use the Actor's
Issues tab and include the run ID, never your token.

## License

[MIT](LICENSE) for this repository's documentation and integration examples.
