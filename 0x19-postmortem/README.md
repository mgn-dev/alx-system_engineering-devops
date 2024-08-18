### Issue Summary
**Duration:**
The outage lasted for **2 hours and 37 minutes** from **10:13 AM to 12:50 PM UTC** on **August 18, 2024**.

**Impact:**
During the outage, approximately **75%** of our users experienced a complete inability to access our main web application. The affected service was the core API, which resulted in users encountering "500 Internal Server Error" responses across all endpoints. The outage primarily affected users in the European and North American regions.

**Root Cause:**
The root cause of the outage was an unintended deployment of a misconfigured Nginx load balancer that caused the API requests to be routed to a deprecated backend server, which was no longer in service.

### Timeline
- **10:13 AM UTC:** Issue detected by automated monitoring alert, indicating a sudden spike in "500 Internal Server Error" responses from the API.
- **10:15 AM UTC:** On-call engineer began investigating the API server logs to identify any issues.
- **10:25 AM UTC:** Initial assumption was that the issue was related to a recent code deployment; the deployment was rolled back as a precaution.
- **10:35 AM UTC:** Rollback did not resolve the issue; network logs and load balancer configurations were inspected.
- **10:50 AM UTC:** Issue escalated to the Network Engineering team for further investigation into potential load balancer misconfigurations.
- **11:15 AM UTC:** A secondary assumption led the team to check database connectivity, but no issues were found.
- **11:45 AM UTC:** Further inspection revealed that the Nginx load balancer was mistakenly configured to route traffic to a deprecated backend server.
- **12:00 PM UTC:** Nginx configuration was updated to point to the correct backend servers, but cache propagation delayed the resolution.
- **12:50 PM UTC:** The updated configuration fully propagated, and the service was restored for all users.

### Root Cause and Resolution
**Root Cause:**  
The outage was caused by an unintended deployment of an Nginx load balancer configuration that routed traffic to a deprecated backend server. The configuration error occurred during a routine maintenance update where an older configuration file was mistakenly pushed to production. The deprecated backend server, which had been decommissioned a week prior, could not handle any requests, leading to the "500 Internal Server Error" responses.

**Resolution:**  
The resolution involved identifying the misconfiguration in the Nginx load balancer and updating the routing rules to point to the active backend servers. The configuration change was tested in a staging environment before being deployed to production. Due to caching issues, the new configuration took some time to fully propagate across all nodes, which extended the outage duration.

### Corrective and Preventative Measures
**Improvements:**   
1. **Version Control and Deployment Safeguards:** Implement stricter version control practices for configuration files, including automated checks to ensure deprecated configurations are not deployed.
2. **Monitoring Enhancements:** Enhance monitoring to include specific checks for routing misconfigurations and backend server connectivity, to provide quicker identification of such issues.
3. **Automated Rollbacks:** Develop automated rollback mechanisms for load balancer configurations that can revert to the last known good state if an issue is detected.

**Task List:**
- **Update Nginx Configuration Management:** Implement automated validation checks for Nginx configuration files before deployment.
- **Expand Monitoring Coverage:** Add monitoring probes that test API endpoints' health from various backend servers to detect routing issues early.
- **Create Staging-Production Parity Checks:** Ensure that configurations are tested in a staging environment that mirrors production more closely.
- **Document Configuration Change Process:** Review and update the documentation on the configuration change process to ensure clarity and prevent human error.
- **Conduct Training:** Provide training sessions for the operations team on the importance of configuration management and rollback procedures.
