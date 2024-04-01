import zipfile
from io import BytesIO

class UnzipingInfo:

    def unziping(self,bytes:bytes):
        try :
            binary_data = BytesIO(bytes)

            with zipfile.ZipFile(binary_data,'r') as file : 
                file_list = file.namelist()
                for name in reversed(file_list):
                    if  name.endswith('.nfo'):
                        with file.open(name) as file_a :
                            x = file_a.read()
                            text = x.decode('utf-8') 
                            return text
                        break 
        except Exception as err :
            print (f'err in unziping err: {err}')

                        # print(file_list[1])
