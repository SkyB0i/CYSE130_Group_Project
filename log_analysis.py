import pandas as pd

def readlogs (file_path): #reads the log files

    logs = pd.read_csv(file_path, delimiter = " ", header = None, headings = ["date", "time", "ip", "event", "status"])
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
    logfilepath = "insert_file_here"
    logs = readlogs("logfilepath")

    if logs is not None: 
        failedlogins, unauthaccess = susactivity(logs)
        summary = createsummary(failedlogins, unauthaccess)

        print("Summary report: ")
        print("Total failed logins: " (summary["tfailedlogins"]))
        print("Total attempts at unauthorized access: " (summary["tunauthaccess"]))

        print("Failed logins per hour: " (summary["tfailedlogins_perhour"]))
        print("Failed unauthorized access per hour: " (summary["tunauthaccess_perhour"]))


main()


    


