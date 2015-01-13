# -*- coding: utf-8 -*-
"""
A script that takes a autopkg -v log and look for new imported items.

Author: Kristian Botnen
Email: kristian.botnen@uib.no
License: The MIT License
"""
import argparse
import smtplib
from datetime import *

class Autoparse:
    
    def readandparse(self, input_filename, mailto_address, mailfrom_address, mailserver_address):
        #Open the log file
        with open(input_filename) as f:
            content = f.readlines()
        
        data = []
        content.reverse()
        iterator = 0
        while iterator < len(content):
            line = content.pop()
            if line.rstrip().lstrip():
                if "The following new items were imported:" in line:
                    line = content.pop()
                    line = content.pop()
                    line = content.pop()
                    data.append(line.strip().replace(',',''))
        result = map(lambda data_line: data_line.split(), data)
        if result:
            self.sendautomail(result, mailto_address, mailfrom_address, mailserver_address)
            
    def sendautomail(self, content, mailto_address, mailfrom_address, mailserver_address):        
        date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Construct the mailheader
        msg = "From: " + mailfrom_address + "\r\nTo: " + mailto_address + "\r\n"
        msg = msg + "Subject: Autopkg says hello " + date_string + "\r\n\r\n"
        msg = msg + str(content)
        
        #print msg
        # Send the mail        
        server = smtplib.SMTP(mailserver_address)
        server.set_debuglevel(1)
        server.sendmail(mailfrom_address, mailto_address, msg)
        server.quit()
        

def main():
    print "Start..."
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Name of the file to read autopkg loginformation from.", type=str)
    parser.add_argument("to_address", help="The mail recipient you want to mail TO.", type=str)
    parser.add_argument("from_address", help="The mail recipient you want to mail FROM.", type=str)
    parser.add_argument("smtp_address", help="The mailserver address, typical smtp.domain.com.", type=str)    
    parser.parse_args()
    args = parser.parse_args()
    
    # We store the args value in variables so we can sanitize the input later if needed.
    in_filename = args.input
    mailto_address = args.to_address
    mailfrom_address = args.from_address
    mailserver_address = args.smtp_address
    
    autoparse = Autoparse()
    autoparse.readandparse(in_filename, mailto_address, mailfrom_address, mailserver_address)
    print "Done..."
        
if __name__ == '__main__':
    main()