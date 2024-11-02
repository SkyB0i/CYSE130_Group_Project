import psutil 
from smtplib import SMTP
from email.mime.text import MIMEText
import time
from datetime import datetime

# percentage thersholds for usage

cpu_thresh = 90
memory_thresh = 80
disk_thresh = 90
alert_length = 120 # seconds
interval_length = 10 # every 10 seconds

log = '_______'

cpu_alert = None
memory_alert = None
disk_alert = None

def send_alert(message): # method to send alert, wip 

    msg = MIMEText(message)
    msg["Subject"] = "System performance alert"
    msg["From"] = ______ # not sure what to put here and underneath, i think i need to do something with smtp?
    msg["To"] = ______

def log_performance(cpu_use, memory_use, disk_use): #creates log entry of performance

    timestamp = datetime.now.strftime("%Y-%m-%d %H:%M:%S") # timestamp to the second for log
    log_entry = f"{timestamp} -- CPU: {cpu_use}%, Memory: {memory_use}%, Disk: {disk_use}%" # log entry format (idk if there's a specific format to follow)

    with open(log, 'a') as log_file: #a creates if not created already and appends if already created
        log_file.write(log_entry) 

def system (): #monitors system
    global cpu_alert, memory_alert, disk_alert #sets variables to be editable in func

    while True:
        cpu_use = psutil.cpu_percent(interval=1) #checks every sec
        memory_use = psutil.virtual_memory().percent
        disk_use = psutil.disk_usage("/").percent

        log_performance(cpu_use, memory_use, disk_use) #uses method to log

        if cpu_use > cpu_thresh:
            if not cpu_alert: # to check if the value is still none or not
                cpu_alert = time.time() # when high cpu usage is found first
            elif time.time() - cpu_alert > alert_length:
                message = f"Abnormal CPU usage for over {alert_length//60} minutes: {cpu_use}%"
                send_alert(message)
                cpu_alert = None #resets
        else:
            cpu_alert = None

# repeat code for others

        if memory_use > memory_thresh:
            if not memory_alert: 
                memory_alert = time.time() 
            elif time.time() - memory_alert > alert_length:
                message = f"Abnormal memory usage for over {alert_length//60} minutes: {memory_use}%"
                send_alert(message)
                memory_alert = None 
        else:
            memory_alert = None
        
        #-----

        if disk_use > disk_thresh:
            if not disk_alert: 
                disk_alert = time.time() 
            elif time.time() - disk_alert > alert_length:
                message = f"Abnormal disk usage for over {alert_length//60} minutes: {disk_use}%"
                send_alert(message)
                disk_alert = None 
        else:
            disk_alert = None
    

        time.sleep(interval_length)

def main(system):
    system()


main()
