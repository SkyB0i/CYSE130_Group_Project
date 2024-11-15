import pandas as pd

def test_logs(filepath):
    with open(filepath, 'w') as f:
        f.write("2021-01-01 12:00:00 123.45.67.89 login failed\n")
        f.write("2021-01-01 12:01:00 321.54.76.98 access unauthorized\n")
        f.write("2021-01-01 12:02:00 432.65.87.09 login succeeded\n")
        f.write("2021-01-01 12:03:00 543.76.98.10 access unauthorized\n")
        f.write("2021-01-01 12:04:00 654.87.09.21 login failed\n")
        f.write("2021-01-01 12:05:00 765.98.10.32 access unauthorized\n")
    print("Test logs created")

def readlogs (file_path): #reads the log files

    logs = pd.read_csv(file_path, delimiter = " ", header = 0, names = ["date", "time", "ip", "event", "status"])
    logs["datetime"] = pd.to_datetime(logs["date"] + " " + logs["time"]) #note use lowercase for headings

    return logs

def susactivity (logs): #returns any weird activity

    failedlogins = logs[(logs["event"] == "login") & (logs["status"] == "failed")] # num of failed logins
    unauthaccess = logs[(logs["event"] == "access") & (logs["status"] == "unauthorized")] # num of unauthorized access attempts

    return failedlogins, unauthaccess

def createsummary (failedlogins, unauthaccess): #creates a summary using the data above
   
   summary= {
    "tfailedlogins": len(failedlogins),
    "tunauthaccess": len(unauthaccess),

    "tfailedlogins_perhour": failedlogins["datetime"].dt.hour.value_counts(),
    "tunauthaccess_perhour": unauthaccess["datetime"].dt.hour.value_counts()
   }

   return summary

def main(): #combines the previous to create a report
    logfilepath = "insert_file_here.csv"
    test_logs(logfilepath)
    logs = readlogs(logfilepath)

    if logs is not None: 
        failedlogins, unauthaccess = susactivity(logs)
        summary = createsummary(failedlogins, unauthaccess)

        print("Summary report: ")
        print("Total failed logins: " + len(summary["tfailedlogins"]))
        print("Total attempts at unauthorized access: " + summary["tunauthaccess"])

        print("Failed logins per hour: " + len(summary["tfailedlogins_perhour"]))
        print("Failed unauthorized access per hour: " + summary["tunauthaccess_perhour"])


main()


    


