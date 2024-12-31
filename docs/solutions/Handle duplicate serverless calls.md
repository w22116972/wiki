# Handle duplicate serverless calls

For async invocation, two cases

- same request ID with error or timeout → so it retries
    - sol: configure error handling function
- no error or timeout
    - sol: idempotent
    - sol: set higher concurrency limit
    - sol: use short visibility timeout (time for same message to be visible for system again)
        - time = 6 x function duration

![](./assets/images/328716848018086.png)

### References

- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/working-with-messages.html#processing-messages-timely-manner
