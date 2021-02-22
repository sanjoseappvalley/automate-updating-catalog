#!/usr/bin/env python3
import sys
import os
import reports
import final_emails


def process_data(path):
    summary = []
    for file in os.listdir(path):
        with open(path + file) as f:
            count = 0
            for line in f:
                if count < 2:
                    if count == 0:
                        summary.append("name: {}".format(line))
                        count = count + 1
                    elif count == 1:
                        summary.append("weight: {}".format(line))
                        count = count + 1
                        summary.append("\n")
    return summary


def main(argv):
    path = 'supplier-data/descriptions/'
    summary = process_data(path)
    paragraph = "<br/>".join(summary)
    title = "Upload Completed - Online Fruit Store"
    attachment = "/tmp/processed.pdf"
    reports.generate(attachment, title, paragraph)

    # Send the email
    sender = "automation@example.com"
    receiver = "student-00-4cd18796e2fb@example.com"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = final_emails.generate_email(sender, receiver, title, body, attachment)
    final_emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
