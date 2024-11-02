from system_performance import cpu_percentage
from system_performance import ram_memory
import log_analysis

def alertGenerator(path_to_log):
    log = log_analysis.readlogs(path_to_log)
    failedlogins, unauthaccess = log_analysis.susactivity(log)

    logSummary = log_analysis.createsummary(failedlogins, unauthaccess)

    failed_logins = logSummary["tfailedlogins"]
    unauthorized_access = logSummary["tunauthaccess"]

    if failed_logins >= 5:
        #Code for alert creation

    if unauthorized_access >= 2:
        # Code for alert creation

    if cpu_percentage >= 90:
        # Code for alert creation
    
    if ram_memory >= 90:
        # Code for alert creation

path_to_log = "logpath"
alertGenerator(path_to_log)