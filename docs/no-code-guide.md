# Run Wayfair collections without code

Open [the hosted Actor](https://apify.com/datascraperes/wayfair-scraper?fpr=edudata) and start with a small Maximum records value.

1. Choose Product details for product URLs/SKUs, Category products for category URLs/IDs,
   Products by keyword for keyword products, Search destinations for matching URLs,
   or Stock by postal code for inventory.
2. Fill the list used by that mode. Select the storefront for bare identifiers; URL domains
   override the storefront. US SKUs do not necessarily exist in Canada or UK.
3. Set a postal code when needed, especially for stock checks. Use separate runs for areas.
4. In listing modes, enable details or use brand/price/rating/stock controls. Advanced filters
   use Add item with Filter ID and Option ID boxes; use options from REFINEMENTS.
5. Start the run, inspect Dataset rows and read SUMMARY. Correct input warnings before repeating
   rejected selections. Download JSON for nested content, or CSV/Excel for spreadsheets.

You can paste [sample-input.json](../data/sample-input.json) into the JSON input editor.
Malformed JSON or schema-invalid values can be rejected by Apify before a run starts.
