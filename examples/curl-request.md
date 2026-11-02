# Start once with cURL, then read the result

Set `APIFY_API_TOKEN` in your shell. Starting the Actor can incur the public event price.
The request caps the run at180 seconds,256MB and$0.02. Do not add automatic retry flags to a start.

```bash
curl --fail-with-body --max-time 45 --request POST \
  'https://api.apify.com/v2/acts/datascraperes~wayfair-scraper/runs?timeout=180&memory=256&maxTotalChargeUsd=0.02' \
  --header "Authorization: Bearer $APIFY_API_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

Save `data.id` from the response as `RUN_ID`. If the connection fails after submission,
inspect recent runs in Console before sending another start; the run may already exist.

```bash
curl --fail-with-body "https://api.apify.com/v2/actor-runs/$RUN_ID" \
  --header "Authorization: Bearer $APIFY_API_TOKEN"
```

Wait until `data.status` is terminal. For a successful run, read `SUMMARY` using
`data.defaultKeyValueStoreId` and inspect its `complete`, `outcome` and warnings.
`SUCCEEDED` alone can represent a safely rejected input with zero rows.

```bash
curl --fail-with-body "https://api.apify.com/v2/key-value-stores/$STORE_ID/records/SUMMARY" \
  --header "Authorization: Bearer $APIFY_API_TOKEN"
curl --fail-with-body "https://api.apify.com/v2/datasets/$DATASET_ID/items?clean=true&format=json&offset=0&limit=100" \
  --header "Authorization: Bearer $APIFY_API_TOKEN"
```

Advance `offset` by the number of returned rows until an empty page. To export an existing
Dataset without starting a run, use the Python CSV example instead.
