# Http Methods (RFC)

> https://www.rfc-editor.org/rfc/rfc9110.html

### GET

> transfer of a current selected representation for the target resource

### POST

> requests that the target resource process the representation enclosed in the request

### PUT

> requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message content

- vs POST: different intent for the enclosed representation
    - POST intent: handle the enclosed representation according to the resource's own semantics
    - PUT intent: replacing the state of the target resource, hence PUT is idempotent

### DELETE

> requests that the origin server remove the association between the target resource and its current functionality

### HEAD

> GET method without content, only metadata

---

#### safe method

> methods that are read-only

- GET, HEAD, OPTIONS, TRACE

#### idempotent method

> if the intended effect on the server of multiple identical requests with that method is the same as the effect for a single such request

- PUT, DELETE, all safe methods
- request can be safely repeated automatically if a communication failure occurs

#### http

> a family of stateless, application-level, request/response protocols for hypertext

