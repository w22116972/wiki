# Non-Functional Requirements

## Availability

> Percentage of time that some service or infrastructure is accessible to clients and is operated upon under normal conditions

| Availability %    | Downtime per Year | Downtime per Month | Downtime per Week |
|-------------------|-------------------|--------------------|-------------------|
| 90% (1 nine)      | 36.5 days         | 72 hours           | 16.8 hours        |
| 99% (2 nines)     | 3.65 days         | 7.20 hours         | 1.68 hours        |
| 99.5% (2 nines)   | 1.83 days         | 3.60 hours         | 50.4 minutes      |
| 99.9% (3 nines)   | 8.76 hours        | 43.8 minutes       | 10.1 minutes      |
| 99.99% (4 nines)  | 52.56 minutes     | 4.32 minutes       | 1.01 minutes      |
| 99.999% (5 nines) | 5.26 minutes      | 25.9 seconds       | 6.05 seconds      |
| 99.9999% (6 nines)| 31.5 seconds      | 2.59 seconds       | 0.605 seconds     |
| 99.99999% (7 nines)| 3.15 seconds     | 0.259 seconds      | 0.0605 seconds    |

---

## Reliability

> Probability that the service will perform its functions for a specified time

### Mean Time Between Failures (MTBF): measures the average time between system failures.

$MTBF = \frac{\text{Total Operating Time}}{\text{Number of Failures}}$

### Mean Time To Repair (MTTR): measures the average time required to repair a system after a failure.

$MTTR = \frac{\text{Total Downtime}}{\text{Number of Failures}}$

### Availability: Availability is the proportion of time a system is functional and available for use.

$Availability = \frac{\text{MTBF}}{\text{MTBF + MTTR}}$

### Mean Time To Failure (MTTF): measures the expected time until a system experiences its first failure.

$MTTF = \frac{\text{Total Operating Time}}{\text{Number of Units}}$






