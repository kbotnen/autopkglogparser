# -*- coding: utf-8 -*-
"""
A script that takes a autopkg -v log and look for new imported items.

Author: Kristian Botnen
Email: kristian.botnen@adm.uib.no
License: The MIT License
"""
import argparse

class Autoparse:
    
    def readandparse(self, input_filename):
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
            self.sendautomail(result)
            
    def sendautomail(self, content):
        import smtplib
        from datetime import *
        
        # Configuration of the mailsettings
        date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        smtp_server = ""
        from_addr = ""
        to_addrs = ""
        
        # Construct the mailheader
        msg = "From: " + from_addr + "\r\nTo: " + to_addrs + "\r\n"
        msg = msg + "Subject: Autopkg says hello " + date_string + "\r\n\r\n"
        msg = msg + str(content)
        
        # Send the mail        
        server = smtplib.SMTP(smtp_server)
        server.set_debuglevel(1)
        server.sendmail(from_addr, to_addrs, msg)
        server.quit()
        

def main():
    print "Start..."
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Name of the file to read autopkg loginformation from.", type=str)
    parser.parse_args()
    args = parser.parse_args()
    
    # We store the args value in variables so we can sanitize the input later if needed.
    in_filename = args.input
    
    autoparse = Autoparse()
    autoparse.readandparse(in_filename)
    print "Done..."
        
if __name__ == '__main__':
    main()