#2d Array. With each internal array containing all words of the same length
#The focus here is to get something working now. 
import argparse
import string
parser = argparse.ArgumentParser(description="Sorts the Names in a given folder, Based on Size and Letters")
parser.add_argument("file", help="What File to sort. With out this Argument it will default to \'SortMe.txt\'.", nargs="?",metavar="File",default="./Sort Me.txt")
parser.add_argument("--reverse",dest="reversed", help="Add this to Reverse the output.", action="store_const",const=True)
wordArray = [[]]
bigNum = 0
args = parser.parse_args()
fileLoc = args.file
def selectionSort(wordArray):
    for i in range(0,len(wordArray)):
        index = i
        #Selection Sort
        for y in range(i+1,len(wordArray)):
            if(ord(wordArray[index][0:1]) > ord(wordArray[y][0:1])):
                index = y
            #If they are Equal we check the next character. if those are Equal. God have mercy on our soul
            if(ord(wordArray[index][0:1]) == ord(wordArray[y][0:1])):
                if(ord(wordArray[index][1:2]) > ord(wordArray[y][1:2])):
                    index = y
        temp = wordArray[index]
        wordArray[index] = wordArray[i]
        wordArray[i] = temp
    return wordArray

with open(fileLoc,"r") as sortFile:
    #First I find the biggest word in the file
    for words in sortFile:
        if(len(words)> bigNum):
            bigNum = len(words)
    for i in range (1,bigNum+1):
        wordArray.append([])

    #Get all Words into seperate arrays.
with open(fileLoc,"r") as sortFile:
    for word in sortFile:
        if(word != '\n'):
            #Word Size determines what Array it goes into. 
            wordArray[len(word.strip())].append(word.strip())
    #Implement a real sort instead of this. As it does not work Fully.  
    for wordSize in wordArray:
        wordSize =  selectionSort(wordSize)
if(not args.reversed):
    with open("./output.txt","w") as outputFile:
        for wordRows in wordArray:
            for words in wordRows:
                outputFile.write(words+"\n")
else:
    with open("./output.txt","w") as outputFile:
        for wordRows in reversed(wordArray):
            for words in reversed(wordRows):
                outputFile.write(words.strip()+"\n")
print("File is Sorted!")

