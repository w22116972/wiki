# What happens between when the client sends a request and when it reaches your backend code?

1. Client Sends the Request
The user (via a browser or mobile app) initiates an HTTP/HTTPS request. The request is packaged with method, URL, headers, and optionally a body, then passed down the network stack.

2. DNS Resolution and Network Transmission
The client resolves the domain to an IP address using DNS. Then, it establishes a TCP connection (3-way handshake). For HTTPS, a TLS handshake also occurs to establish a secure encrypted channel.

3. Reverse Proxy / Load Balancer (Optional)
In most production environments, the request first hits a reverse proxy, API Gateway, or Load Balancer like NGINX or AWS ELB. These components handle SSL termination, routing, rate limiting, or authentication.

4. Application Server Receives the Request
The request is forwarded to the application server (e.g., Spring Boot embedded server, Tomcat, Node.js). The server parses the HTTP request into a structured object like HttpServletRequest.

5. Framework-Level Routing
The backend framework (e.g., Spring MVC) routes the request to the correct controller or handler method based on HTTP method and path. It may also pass through interceptors or filters for tasks like authentication, logging, or CORS handling.

6. Reaching Business Logic Code
Finally, the request arrives at the business logic code written by the developer — such as a controller method that queries a database, performs computation, and returns a response.

