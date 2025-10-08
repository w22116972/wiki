# Newsfeed System

## Requirement

### Functional requirements

- create newsfeed 
- read newsfeed

### Non-functional requirements

- scalability
- fault tolerance
- availability
- latency < 2 sec

## Estimation

### Assumption

- 500M DAU (total user is 1b)
- each user has 300 friends and follows 250 pages on average
- each user uses app 10 times a day

### RPS estimation

- 500M x 10 = 5b per day = 58K RPS

### Storage estimation

- render 200 posts to user

#### User's metadata

- assume 50 KB for metadata
- total user 1b x 50 KB = 50 TB

#### User's post

- assume 5 KB per post
- 200 posts x 500M DAU x 5 KB post size = 0.5 PB

#### Media content

- assume video is 2 MB and 1/5 of total
- assume image is 200 KB and 4/5 of total
- ((200 posts x 2 MB x 1/5) + (200 posts x 200 KB x 4/5)) x 500 M DAU = 56 PB

### Server estimation

- assume a typical server handle 64 K RPS
- 500 M DAU / 64 K = 8 K servers

## High-level design

```
[ Users ]
    |
    v
[ Load Balancer ]
    |
    v
[ Web Servers ]
    |        |         |         |
    |        |         |         |
    v        v         v         v
[ Notification Service ]   [ Post Service ]   [ Newsfeed Generation Service ]   [ Newsfeed Publishing Service ]
         |                        |                        |                          |
         |                        |                        |                          |
         |                        |                        v                          v
         |                        |                [ Newsfeed Cache ]         [ Blob Storage ]
         |                        |                        |                          |
         |                        |                        |                          |
         |                        |                        +--------------------------+
         |                        |                                   |
         +------------------------+-----------------------------------+
```

