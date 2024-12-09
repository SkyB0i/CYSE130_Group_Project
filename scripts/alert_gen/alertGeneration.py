import log_analysis
import datetime

alertLog = open('logs/AlertLogs.txt', 'w')

def read_performance_logs(path_to_log):
     with open(path_to_log, 'r') as log:
          log_data = log.readlines()
          recent = log_data[-1].split(" ")
          cpu = float(recent[4].strip('%,')) * 100
          ram = float(recent[6].strip('%,')) * 100
          return cpu, ram


def alertGenerator(path_to_log):
    log = log_analysis.readlogs(path_to_log)
    failedlogins, unauthaccess = log_analysis.susactivity(log)

    logSummary = log_analysis.createsummary(failedlogins, unauthaccess)

    failed_logins = logSummary["tfailedlogins"]
    unauthorized_access = logSummary["tunauthaccess"]

    cpu_percentage, ram_memory = read_performance_logs("system_performance.log")

    if failed_logins >= 5:
        alertLog.write('{:%Y-%m-%d %H:%M:%S} [SECURITY ALERT] Excessive failed login attempts detected.'.format(datetime.datetime.now()))

    if unauthorized_access >= 2:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [SECURITY ALERT] Excessive unauthorized access attempts detected.'.format(datetime.datetime.now()))

    if cpu_percentage >= 90:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [RESOURCE ALERT] Excessive CPU use detected.'.format(datetime.datetime.now()))
    
    if ram_memory >= 90:
         alertLog.write('{:%Y-%m-%d %H:%M:%S} [RESOURCE ALERT] Excessive RAM use detected.'.format(datetime.datetime.now()))

testfilepath = "logs/AlertGenerationTestLogs.txt"
alertGenerator(testfilepath)