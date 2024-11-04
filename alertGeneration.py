from system_performance import cpu_percentage
from system_performance import ram_memory
import log_analysis
import datetime

alertLog = open('AlertLogs.txt', 'w')

print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
def alertGenerator(path_to_log):
    log = log_analysis.readlogs(path_to_log)
    failedlogins, unauthaccess = log_analysis.susactivity(log)

    logSummary = log_analysis.createsummary(failedlogins, unauthaccess)

    failed_logins = logSummary["tfailedlogins"]
    unauthorized_access = logSummary["tunauthaccess"]

    if failed_logins >= 5:
        alertLog.write('{:%Y-%m-%d %H:%M:%S} [SECURITY ALERT] Excessive failed login attempts detected.'.format(datetime.datetime.now()))

    if unauthorized_access >= 2:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [SECURITY ALERT] Excessive unauthorized access attempts detected.'.format(datetime.datetime.now()))

    if cpu_percentage >= 90:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [RESOURCE ALERT] Excessive CPU use detected.'.format(datetime.datetime.now()))
    
    if ram_memory >= 90:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [RESOURCE ALERT] Excessive RAM use detected.'.format(datetime.datetime.now()))

path_to_log = "logpath"
alertGenerator(path_to_log)