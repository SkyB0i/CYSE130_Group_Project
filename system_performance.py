import psutil 
from smtplib import SMTP

cpu_percentage = psutil.cpu_percent(30)
ram_memory = psutil.virtual_memory()[2]