# Email headers are crucial metadata components of an email that reveal 
# important details about its origin, transmission, and content. 
# Although they’re not visible to the recipient by default, 
# you can view them using email client features or specialized tools. 
# These headers contain various fields, each serving a specific function.

import email
import quopri
from email import policy
from email.parser import BytesParser

def parse_email(file_path):
    with open(file_path, 'rb') as file:
        msg = BytesParser(policy=policy.default).parse(file)

    print("From:", msg.get("From", "N/A"))
    print("To:", msg.get("To", "N/A"))
    print("Subject:", msg.get("Subject", "N/A"))
    print("Date:", msg.get("Date", "N/A"))
    print("Message ID:", msg.get("Message-ID", "N/A"))
    print("X-Mailer:", msg.get("X-Mailer", "N/A"))
    # Additional Information
    print("\n--- Additional Information ---\n")
    print("SPF:", msg.get("Received-SPF", "N/A"))
    print("DKIM:", msg.get("DKIM-Signature", "N/A"))
    print("DMARC:", msg.get("DMARC-Filter", "N/A"))
    print("SENDERIP:", msg.get("X-Sender-IP", "N/A"))
    print("RETURN PATH:", msg.get("Return-Path", "N/A"))
    print("Reply-To:", msg.get("Reply-To", "N/A"))  
    print('Authentication Results:\n', msg.get('Authentication-Results','N/A'))
    print('Message ID', msg.get('Message-Id','N/A'))

def main():
    email_file_path = "/content/Sample.eml"  ## Email File
    parse_email(email_file_path)
if __name__ == "__main__":
    main()