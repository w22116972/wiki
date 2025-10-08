# Example: Back-of-the-envelope estimation for Twitter service

### Assumptions

- 500M DAU
- at most 20 requests per DAU per day
- a single server (with 64 cores) can handle 64000 RPS

-> 500M x 20 = 10B requests per day = 10B / 86400 = 115K RPS

### Server Requirement

$Number\ of\ servers\ needed\ = \frac{RPS}{RPS\ per\ server} = \frac{115K}{64000} = $

Consider peak capacity when `at most 20 requests per DAU per day` to all 20 requests are made in a second.

$ \text{尖峰所需伺服器數量} = \frac{\text{每秒請求數（總數）}}{\text{每台伺服器的每秒請求數（RPS）}} = \frac{10,000,000,000}{64,000} = 157,000 \, (\text{台伺服器})$

then we can use this number to calculate the cost of the system.

### Storage Requirement

- 500M DAU
- each user has 3 posts per day
- posts with image is 200KB average, with video is 3MB average
- 10% of posts have images, 5% have videos
- text and metadata is 250 bytes
- Total storage in a day = 500M x 3 x (0.1 x 200KB + 0.05 x 3MB + 0.85 x 250B) = 500M x 3 x (20KB + 150KB + 212.5B) = 500M x 3 x 170.2KB = **255TB**

### Bandwidth Requirement

- Estimate the daily amount of incoming data to the service.
- Estimate the daily amount of outgoing data from the service.
- Estimate the bandwidth in Gbps (Gigabits per second) by dividing the incoming and outgoing data by the number of seconds in a day.

note: units in bandwidth are in bits, not bytes.

$ \frac{255\ TB}{86400\ seconds\ per\ day} \times 8\ bits\ per\ byte  \approx 24Gbps $

Incoming data is the data that user writes to the Twitter service. Outgoing data is the data that user reads from the Twitter service.

We already have $255\ TB$ that user posts to Twitter for incoming data.
Assume that user reads 10 times more data than they write, then the outgoing data is $255\ TB \times 10 = 2550\ TB$.

Then the total bandwidth is $24\ Gbps + 2550\ TB \times 8\ bits\ per\ byte / 86400\ seconds\ per\ day \approx\ 264\ Gbps$.


