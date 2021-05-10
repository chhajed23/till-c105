def countWordsFromFile():
    fileName=input("Enter the file name: ")
    file=open(fileName)
    lines=file.readlines()
    numberOfWords=0
    for line in lines:
        words=line.split()
        numberOfWords+=len(words)
    print("Number Of Words: ",numberOfWords)

countWordsFromFile()   
