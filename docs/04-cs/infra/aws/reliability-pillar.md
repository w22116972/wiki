# Reliability Pillar

## REL01-BP01 Aware of service quotas and constraints

### Goal
Customers can prevent service degradation or disruption in their AWS accounts by implementing proper guidelines for monitoring key metrics, infrastructure reviews, and automation remediation steps to verify that services quotas and constraints are not reached that could cause service degradation or disruption.

### Benefits
- Proactively reduce failures through monitoring and automated management of service quotas.
- Improve application resiliency under adverse or unplanned events by managing quotas across all regions and accounts.
- Prevent service disruption caused by unexpected changes in traffic patterns.

### Risk Level
**High**

### Implementation

#### Implementation Guidance
To effectively manage service quotas and constraints, you must first understand them. AWS provides the **Service Quotas** dashboard to view and manage quotas for over 250 services in one place. For programmatic access, you can use the AWS SDK or CLI. Additionally, **AWS Trusted Advisor** offers checks that display your usage against existing quotas, helping you identify limits you are approaching.

It's crucial to distinguish between adjustable **service quotas** and fixed **service constraints**.
- **Service Quotas** are operational guardrails to prevent accidental over-provisioning. These can often be increased upon request. They can be region-specific or global, and reaching a quota limit may cause service degradation (e.g., failing to scale EC2 instances during a traffic spike).
- **Service Constraints** are hard limits defined by the resource type, such as the maximum size of an EBS volume. These cannot be changed and must be engineered around.

For limits that are not adjustable but impact performance, you should contact AWS Support for potential mitigation strategies.

Several tools are available to help you monitor and manage your quotas:
- **AWS Trusted Advisor**: Provides checks to identify services nearing their quota.
- **AWS Management Console**: Allows you to view, manage, and request new quotas.
- **AWS CLI and SDKs**: Offer programmatic methods to automate quota management and monitoring.

#### Steps
For Service Quotas:

* Review AWS Service Quotas.
* To be aware of your existing service quotas, determine the services (like IAM Access Analyzer) that are used. There are approximately 250 AWS services controlled by service quotas. Then, determine the specific service quota name that might be used within each account and Region. There are approximately 3000 service quota names per Region.
* Augment this quota analysis with AWS Config to find all AWS resources used in your AWS accounts.
* Use AWS CloudFormation data to determine your AWS resources used. Look at the resources that were created either in the AWS Management Console or with the list-stack-resources AWS CLI command. You can also see resources configured to be deployed in the template itself.
* Determine all the services your workload requires by looking at the deployment code.
* Determine the service quotas that apply. Use the programmatically accessible information from Trusted Advisor and Service Quotas.
* Establish an automated monitoring method (see REL01-BP02 Manage service quotas across accounts and regions and REL01-BP04 Monitor and manage quotas) to alert and inform if services quotas are near or have reached their limit.
* Establish an automated and programmatic method to check if a service quota has been changed in one region but not in other regions in the same account (see REL01-BP02 Manage service quotas across accounts and regions and REL01-BP04 Monitor and manage quotas).
* Automate scanning application logs and metrics to determine if there are any quota or service constraint errors. If these errors are present, send alerts to the monitoring system.
* Establish engineering procedures to calculate the required change in quota (see REL01-BP05 Automate quota management) once it has been identified that larger quotas are required for specific services.
* Create a provisioning and approval workflow to request changes in service quota. This should include an exception workflow in case of request deny or partial approval.
* Create an engineering method to review service quotas prior to provisioning and using new AWS services before rolling out to production or loaded environments. (for example, load testing account).

For service constraints:

* Establish monitoring and metrics methods to alert for resources reading close to their resource constraints. Leverage CloudWatch as appropriate for metrics or log monitoring.
* Establish alert thresholds for each resource that has a constraint that is meaningful to the application or system.
* Create workflow and infrastructure management procedures to change the resource type if the constraint is near utilization. This workflow should include load testing as a best practice to verify that new type is the correct resource type with the new constraints.
* Migrate identified resource to the recommended new resource type, using existing procedures and processes.

## REL01-BP02 Manage service quotas across accounts and regions

### Goal
Services and applications should not be affected by service quota exhaustion for configurations that span accounts or Regions or that have resilience designs using zone, Region, or account failover.

### Benefits
- Ensure you can handle your current load in secondary regions or accounts if regional services become unavailable.
- Reduce the number of errors or levels of degradations that occur during region loss.

### Risk Level
**High**

### Implementation

#### Implementation Guidance
Service quotas are tracked per account and are typically AWS Region-specific. It is essential to manage quotas in all environments, including non-production, to prevent disruption of testing and development. For workloads spanning multiple Regions (e.g., Active/Active or Active/Passive designs), you must ensure quota levels are aligned across all regions. A discrepancy in quota limits between regions, known as *service quota drift*, must be actively tracked and reconciled. Utilize automated processes to continuously assess and manage these quotas to ensure consistent resilience.

#### Steps
- Review Service Quotas values that might have breached a risk level of usage. AWS Trusted Advisor provides alerts for 80% and 90% threshold breaches.
- Review values for service quotas in any Passive Regions (in an Active/Passive design). Verify that load will successfully run in secondary Regions in the event of a failure in the primary Region.
- Automate assessing if any service quota drift has occurred between Regions in the same account and act accordingly to change the limits.
- If you use Organizational Units (OUs), update service quota templates to reflect changes that should be applied to multiple Regions and accounts.
- Create a template and associate Regions to the quota change.
- Review all existing service quota templates for any changes required (Region, limits, and accounts).

## REL01-BP03 Accommodate fixed service quotas and constraints through architecture

### Goal
The application or service performs as expected under normal and high traffic conditions. They have been designed to work within the limitations for that resource’s fixed constraints or service quotas.

### Benefits
- Verifying that the application will run under all projected services load levels without disruption or degradation.

### Risk Level
**Medium**

### Implementation

#### Implementation Guidance
Unlike soft service quotas, which can be increased, fixed (or hard) quotas cannot be changed. Your architecture must be designed to accommodate these limitations. Hard limits are identified in the Service Quotas console where a service is marked as not adjustable.

For example, an AWS Lambda function has a maximum execution time of 15 minutes. If your application design might exceed this limit, you must consider alternative technologies or architectures. Failing to account for these hard limits during the design phase can lead to service degradation or disruption in production. It is critical to use stress testing, load testing, and chaos testing to identify if any hard limits can be reached before deploying to production.

#### Steps
- Review the complete list of AWS services that could be used in the application design phase.
- Review the soft quota limits and hard quota limits for all these services. Not all limits are shown in the Service Quotas console. Some services describe these limits in alternate locations.
- As you design your application, review your workload’s business and technology drivers, such as business outcomes, use case, dependent systems, availability targets, and disaster recovery objects. Let your business and technology drivers guide the process to identify the distributed system that is right for your workload.
- Analyze service load across Regions and accounts. Many hard limits are regionally based for services. However, some limits are account based.
- Analyze resilience architectures for resource usage during a zonal failure and Regional failure. In the progression of multi-Region designs using active/active, active/passive – hot, active/passive - cold, and active/passive - pilot light approaches, these failure cases will cause higher usage. This creates a potential use case for hitting hard limits.