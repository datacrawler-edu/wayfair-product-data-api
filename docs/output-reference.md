# Output and completion

The default Dataset contains one final record per delivered item. See the complete
[real listing sample](../data/sample-output.json). The CSV sample selects common scalar fields.

- Identity: `recordType`, `market`, `sku`, `variantId`, `sourceInput`, `scrapedAt`.
- Labels/pricing: `name`, `brand`, `url`, `price`, `wasPrice`, `currency`, `savings`, `discountPercent`.
- Stock/ratings: `stockStatus`, `stockMessage`, `availableQuantity`, `maxPurchasableQuantity`,
  `rating`, `reviewCount`. Fields vary by mode and source availability.
- Listing context: `classId`, `className`, `categoryId`, `categoryName`, `categoryUrl`, `resultType`, `postalCode`.
- Images/options: `imageIds`, `imageUrl`, `imageUrls`, `choiceCategories`.
- Details: `description`, `featureBullets`, `dimensions`, `specifications`, `productWeight`, `materials`, `detailsFetched`.

Product details can lack listing-only brand, rating, stock or images. Inventory rows primarily
contain product identity and stock; search-resolution rows primarily contain the destination.
The image list is not an exhaustive gallery, and variants are not exhaustively enumerated.

Read the SUMMARY key-value record after each run. `complete: true` and `outcome: complete`
mean the requested collection completed within its documented cap. `invalid_input` means
selections were rejected; `partial` means verified rows may exist while other work needs attention.
Warnings alone can finish with a successful platform status. Technical failures can leave
already saved rows available; inspect them before repeating work. REFINEMENTS lists available
filter options for listing requests.
