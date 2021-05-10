import shutil
import os
import time

def main():
    path="path_to_delete"
    days=1
    seconds=time.time()-(days*24*60*60)
    folderCount=0
    fileCount=0
    isExist=os.path.exists(path)

    if isExist=="false":
        print(path," Not found")
        fileCount+=1
    else:
        for root,folders,files in os.walk(path):
            
            if seconds>=getAgeOfFile(root):
                removeFolder(root)
                folderCount+=1
                break
            else:
                for folder in folders:
                    fp=os.path.join(root,folder)
                    if seconds>=getAgeOfFile(root):
                        removeFolder(fp)
                        folderCount+=1
                
                for file in files:
                    filePath=os.path.join(root,file)
                    if seconds>=getAgeOfFile(root):
                        removeFile(filePath)
                        fileCount+=1
        else:
            if seconds>=getAgeOfFile(path):
                removeFile(path)
                fileCount+=1
    print("Total Folders Deleted: ",folderCount)
    print("Total Files Deleted: ",fileCount)




def getAgeOfFile(path):
    ctime=os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if not shutil.rmtree(path):
        print(path," removed successfully")
        
    else:
        print("Unable to delete the ",path)

def removeFile(path):
    if not os.remove(path):
        print(path," removed successfully")
    else:
        print("Unable to delete the ",path)


if __name__=="__main__":
    main()