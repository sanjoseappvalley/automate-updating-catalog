#!/usr/bin/env python3

import final_emails
import psutil
import smtplib
import socket

subject = ""

if psutil.cpu_percent(interval=1) > 80:
    subject = "Error - CPU usage is over 80%"

diskusage = psutil.disk_usage('/')
if diskusage.percent > 80:
    subject = "Error - Available disk space is less than 20%"

mem = psutil.virtual_memory()
threshold = 500 * 1024 * 1024
if mem.available < threshold:
    subject = "Error - Available memory is less than 500MB"

hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"

sender = "automation@example.com"
recipient = "username@example.com"
body = "Please check your system and resolve the issue as soon as possible."
if subject != "":
    message = final_reports.generate_error_report(sender, recipient, subject, body)
    final_reports.send_email(message)
