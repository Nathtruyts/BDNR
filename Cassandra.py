export ASTRA_DB_ID=35873877-451f-45a7-a32c-66a25bb625eb
export ASTRA_DB_REGION=us-east1
export ASTRA_DB_KEYSPACE=Eva01
export ASTRA_DB_APPLICATION_TOKEN=AstraCS:uAqxRwmrJeAEoCsykbkNcCEX:c2078294ff26828c291453eb7f420adc3a97c2ca484e57cf8b5abc43a88c84e1
curl --request POST \
  --url https://$ASTRA_DB_ID-$ASTRA_DB_REGION.apps.astra.datastax.com/api/rest/v2/namespaces/$ASTRA_DB_KEYSPACE/collections/hello_docs \
  -H "X-Cassandra-Token: $ASTRA_DB_APPLICATION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Some Stuff",
    "other": "This is nonsensical stuff."
  }'
