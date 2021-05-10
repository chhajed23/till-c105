import dropbox

class TransferData:
    def __init__(self,token):
        self.token=token

    def upload_file(self,file_From,dropbox_path):
        dbx=dropbox.Dropbox(self.token)
    
        with open(file_From,'rb')as f:
            dbx.files_upload(f.read(),dropbox_path,mode=Writemode('overwrite'))


def main():
    access_token='sl.AvufyOrOlKMO708NgXVnhiikvaDffnJG6ou3KYc3NQm0v6iltA0PJIJ7KmmhNfmS5mwjBQXXMTumJ5maWk-H62klre7YjaCVRsLsuxcbAymiKQ3bBBDSPyoZwlrQ-My1c6mYH-E'
    transferData=TransferData(access_token)
    file_From=input("Enter The File path to Transfer: ")
    dropbox_path=input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(file_From,dropbox_path)
    print("File uploaded successfully")

if __name__=='__main__':
    main()



