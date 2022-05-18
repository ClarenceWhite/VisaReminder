# VisaReminder
This is a visa reminder of visa for Belgium https://visaonweb.diplomatie.be/en, it will request the visa page every hour/certain minutes, once there are appointments available, it will send me a Wechat message.
This project is a practical of python selenium package, chrome headless on ubuntu linux, python WxPusher package (see: https://wxpusher.zjiecode.com/docs/#/), and python requests package.

# Idea
This project uses selenium to automate the control of the browser, through this tool you can automate many daily life alerts, such as alerting web content updates, grabbing tickets, and monitoring the running of the code deployed on the server to find running errors in time.

# Usage
Both local and remote machine have to have a 'config.txt' with some confidential parameters in it
## Local machine
On local machine you can run with or without chrome headless (see VisaReminder.py to check how to set headless status).
## Linux remote server without a chrome GUI
On a remote linux machine you need to run with chrome headless to prevent GUI error (see VisaReminder.py to check how to set headless status).
