# Handle Big Query by Serverless

## Problem

Assume a server can serve 10 queries, if incoming query is big, then that server only serves 8 queries and 2 queries are wasted. 

## Solution

Use query history to predict the incoming query size

When big query is coming, then use another server to serve the query

