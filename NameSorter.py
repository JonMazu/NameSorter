#2d Array. With each internal array containing all words of the same length
#The focus here is to get something working now. 
wordArray = [[]]
bigNum = 0
def selectionSort(wordArray):
    for i in range(len(wordArray)):
        index = i
        #Selection Sort
        for y in range(i+1,len(wordArray)):
            if(ord(wordArray[index][1:2]) > ord(wordArray[y][1:2])):
                index = y
            #If they are Equal we check the next character. if those are Equal. God have mercy on our soul
            if(ord(wordArray[index][1:2]) == ord(wordArray[y][1:2])):
                if(ord(wordArray[index][2:3]) > ord(wordArray[y][2:3])):
                    index = y
        temp = wordArray[index]
        wordArray[index] = wordArray[i]
        wordArray[i] = temp
    return wordArray

with open("./Sort Me.txt","r") as sortFile:
    #First I find the biggest word in the file
    for words in sortFile:
        if(len(words)> bigNum):
            bigNum = len(words)
    for i in range (1,bigNum+1):
        wordArray.append([])
    #Get all Words into seperate arrays.
with open("./Sort Me.txt","r") as sortFile:
    for word in sortFile:
        if(word != '\n'):
            wordArray[len(word)].append(word)
    #Implement a real sort instead of this. As it does not work  
    for wordSize in wordArray:
        wordSize =  selectionSort(wordSize)
with open("./output.txt","w") as outputFile:
    for wordRows in wordArray:
        for words in wordRows:
            outputFile.write(words.strip()+"\n")

