# Logging Best Practices

### Always log

- Application errors
- Input and output validation failures
- Authentication successes and failures
- Authorization failures
- Session management failures
- Privilege elevation successes and failures
- Other higher-risk events, like data import and export
- Logging initialization
- (ref: SWE Guide book) events to log
  - authentication/authorization (login, logout, failed login)
  - system access, data access
  - data changes (create, update, delete)
  - invalid input
  - resources (RAM, Disk, CPU, Bandwidth, any sw/hw limits)
  - health or availability checks (start, stop, fault/errors, delays, backup success/failure)
  - Format:
    - when: timestamp + timezone
    - where: system or app, IP
    - who: user
    - what: action
    - result: status
    - priority
    - reason

### Logging other events to address following use cases

- Troubleshooting
- Monitoring and performance improvement
- Testing
- Understanding user behavior
- Security
- Auditing
    - e.g. log an event whenever a user updates their profile in your app

### What message content

- What action was performed
- Who performed the action
- Why a failure occurred
- Remediation information when possible for WARN and ERROR messages
- HTTP request ID

e.g. use JSON for structured logging

```text
2019-06-20T17:21:00.002899+00:00 app[web.1]: INFO: Address removed by customer. {"addressid":18344857, "customerid":50333}
```

```text
2019-06-20T17:21:00.002899+00:00 app[email-wrkr.1]: DEBUG: Fetching mailing list {"listid":14777}
2019-06-20T17:22:00.000098+00:00 app[email-wrkr.1]: DEBUG: User opted out {"userid":3654}
```

### Log entry should answer following questions:

- ***who** (username)*
- ***when** (timestamp)*
- ***where** (context, servletorpage,database)*
- ***what** (command)*
- ***result** (exception)*

e.g. 

```text
[errorhandlername] username: userabc databasename: abc timestamp: 15.07.2009 13:02:08 context:servlet page: /prod/sales/salesorders.jsp window: windwname command: savesalesorder exception: shortdescriptionofexception exceptionstacktracehere
```

### Log all information numerically

- (O) IP address (X) hostname 
- (O) timestamps, seconds since epoch (X) string data Monday, June, 3

### Avoid string concatenation and method call unless logging has been enabled

```java
// unnecessary calls are also made to the calcX() and calcY()
logger.debug("value of X is " + calcX() + " and Y is " + calcY());

// avoids the string concatenation and no method calls unless logging has been enabled
if (logger.isDebugEnabled()) { 
	logger.debug("value of X is "+ calcX() + " and Y is " + calcY());
}
```

### **Loggers should always be `private static final`**

- Why final? The logger for a class should never need to change
- Why static? since logger usage should be consistent throughout a codebase + singleton + possibly will be used from static initializers

### Make the logger the first static field in a class

```java
private static final Data data = initStaticData();
private static final GoogleLogger logger = GoogleLogger.forEnclosingClass();

private static Data initStaticData() {
  logger.atInfo().log("Initializing static data");
  // ...
}
```

When `initStaticData()` is called, the static logger field is still `null` . A habit of initializing your logger first will prevent this problem.

### Log level

- `FATAL`: severe error that will prevent the application from continuing
- `ERROR`: error in the application, possibly recoverable
- `WARN`: event that might possible lead to an error
- `INFO`: event for informational purposes
- `DEBUG`: general debugging event
  - e.g. *`Opening config file ...`*
- `TRACE`: fine-grained debug message (more detailed than `DEBUG`)  , typically capturing the flow through the application
  - e.g. *`openssl: Handshake: start` , `read from buffered SSL brigade, mode 0, 17 bytes` , `map lookup FAILED: map=rewritemap key=keyname` , `cache lookup FAILED, forcing new map lookup`*


### References

- https://devcenter.heroku.com/articles/writing-best-practices-for-application-logs
