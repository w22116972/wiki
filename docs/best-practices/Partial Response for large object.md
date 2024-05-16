# Partial Response for Large Object

> https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-implementation#implement-partial-responses-for-clients-that-dont-support-asynchronous-operations

### Context and Scope

- Handling large requests and responses.
- Not support asynchronous operations.

### Steps

1. Client sends `HEAD` request to get the metadata of the object.
2. Server responds message with `Accept-Ranges` and `Content-Length` headers and empty body.
3. Client sends series of `GET` request that specify a range of bytes to receive.
4. Server responds status `206 Partial Content`, `Content-Length` about actual amount of data included in the body of the response message, and `Content-Range` header to specify which bytes (e.g. 4000~8000).
