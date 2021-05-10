introduction=input("Enter something about yourself: ")
charCount=0
wordCount = 1
for x in introduction:
    charCount+=1
    if x ==" ":
        wordCount+=1
       
print("Number of characters in the entered string: ",charCount)
print("Number of words in the entered string: ",wordCount) 