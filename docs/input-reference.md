# Input reference

Use the exact API mode values below. The complete neutral example is [full-input.json](../data/full-input.json).

| Field | Type | Meaning |
|---|---|---|
| `mode` | string | Choose Product details for product URLs or SKUs; Category products for category URLs or IDs; Products by keyword for keyword results; Stock by postal code for stock checks. Search destinations returns the matching destination URL rather than its product listing. |
| `market` | string | Wayfair storefront used when the identifier does not include a domain. Products and category IDs are market-specific: a US SKU does not resolve on the Canadian or UK site. |
| `maxItems` | integer | Upper bound for unique records across the whole run. Reaching this cap is a valid completion when no collection or delivery problems remain. Missing or incomplete data is reported separately in the run summary. |
| `productUrls` | array | Add one Wayfair product URL or SKU per item, for example W005299789. URLs may come from wayfair.com, wayfair.ca or wayfair.co.uk; the market is detected from the domain and overrides the market setting. Used by the Products and Inventory modes. Up to 200 identifiers. |
| `categoryUrls` | array | Add one Wayfair category URL or numeric category ID per item, for example https://www.wayfair.com/furniture/sb0/sofas-c413892.html or 413892. Used by the Category mode. Up to 20 categories. |
| `searchTerms` | array | Add one keyword or phrase per item, such as coffee table. Used by Products by keyword and Search destinations. Up to 20 terms. |
| `postalCode` | string | Postal code used for stock and delivery information and the shipping context of listings. Required by Inventory. It must be valid for every market selected by the active input URLs. Omitted category postal codes default to 10001 (US), M5V 2T6 (Canada), or SW1A 1AA (UK). |
| `includeDetails` | boolean | Enrich category/searchProducts rows with description, dimensions and specifications before delivery. A failed enrichment preserves the listing and marks the run partial. Used only by category and searchProducts. |
| `brand` | string | Exact brand name offered by the category/search refinement. Empty disables. Unavailable brands produce a partial or failed result, never a broader unfiltered catalog. Used only by category and searchProducts. |
| `minPrice` | number | Keep known prices at or above this value in the market currency. Zero disables. Missing prices are excluded when enabled. Used only by category and searchProducts. |
| `maxPrice` | number | Keep known prices at or below this value. Zero disables. Missing prices are excluded when enabled. Used only by category and searchProducts. |
| `minRating` | number | Keep known ratings at or above this value. Zero disables. Missing ratings are excluded when enabled. Used only by category and searchProducts. |
| `inStockOnly` | boolean | Keep listings explicitly marked IN_STOCK. Unknown stock is excluded. Used only by category and searchProducts. |
| `sortBy` | string | Source order for category/searchProducts. Filtering preserves that order. Used only by category and searchProducts. |
| `filters` | array | Optional advanced filters. Click Add item and fill Filter ID and Option ID in the form; no JSON is needed. Use identifiers from a previous listing run in REFINEMENTS. For most runs, use the Brand, Price, Rating and In stock controls instead. Leave empty to apply no additional source filters. |

Only the active mode's identifier list is required. `products` uses product URLs/SKUs;
`category` uses category URLs/IDs; `searchProducts` collects keyword products; `search`
returns resolved destination URLs; `inventory` checks product stock and requires a postal code.

Use category filters only with `category` or `searchProducts`. IDs vary by listing and market;
choose matching pairs from REFINEMENTS. Unknown filters/options warn and skip that listing,
with no row/event for it. If options cannot be verified, collection with those source filters
stops safely. A directly matched product cannot use category filters. Prefer the ordinary
Brand, Price, Rating and In stock controls when they cover the task.
