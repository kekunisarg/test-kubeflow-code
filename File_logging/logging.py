import os
import sys
import datetime
import traceback

class FileLogging:
    def __init__(self,calling_script = None,filepath = None,filename = None, ):
        self.calling_script = calling_script
        self.filepath = filepath
        self.filename = filename

        if not os.path.isdir(self.filepath):
            raise Exception("Invalid Path: ",self.filepath)

    def appendlog(self,logline):
        try:
            log_file_path = self.filepath+'/'+self.filename
            if not os.path.isfile(log_file_path):
                with open(log_file_path,'a') as fp:
                    pass

            log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            formatted_logline = log_time + " | "+ self.calling_script +" | "+ logline

            with open(log_file_path,'a') as file:
                file.write(formatted_logline+"\n")
        except Exception:
            print(traceback.format_exc())