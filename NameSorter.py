#2d Array. With each internal array containing all words of the same length
#The focus here is to get something working now. 
import argparse
import string
parser = argparse.ArgumentParser(description="Sorts the Names in a given folder, Based on Size and Letters")
parser.add_argument("file", help="What File to sort. With out this Argument it will default to \'SortMe.txt\'.", nargs="?",metavar="File",default="./Sort Me.txt")
parser.add_argument("--reverse",dest="reversed", help="Add this to Reverse the output.", action="store_const",const=True)
parser.add_argument("--test",dest="test", help="Add this to Test the output!", action="store_const",const=True)
wordArray = [[]]
bigNum = 0
args = parser.parse_args()
fileLoc = args.file
if(args.test):
    fileLoc = './TestData/Sort Me.txt'

def test_selectionSort(output,expected):
    for x in range(0,len(output)):
         if(output[x] != expected[x]):
             print("Somethings Wrong with the Sort!")
             print(output[x] +" "+ expected[x])
             print("This is Incorrect!! Report any bugs to the Github!!")
             return -1
    #This feels somewhat pointless. Since If its wrong forwards then will definietly be wrong backwards.
    listSize = len(output)
    output = list(reversed(output))
    expected = list(reversed(expected))
    for x in range(0,listSize):
        if(output[x] != expected[x]):
             print("Somethings Wrong with the Sort!")
             print(output[x] +" "+ expected[x])
             return -1
    return 0


def selectionSort(wordArray):
    for i in range(0,len(wordArray)):
        index = i
        #Selection Sort
        for y in range(i+1,len(wordArray)):
            if(ord(wordArray[index][0:1]) > ord(wordArray[y][0:1])):
                index = y
            #If they are Equal we check the next character. if those are Equal. God have mercy on our soul
            if(ord(wordArray[index][0:1]) == ord(wordArray[y][0:1])):
                for x in range(2,len(wordArray[index])):
                    if(ord(wordArray[index][x-1:x]) == ord(wordArray[y][x-1:x])):
                        continue
                    if(ord(wordArray[index][x-1:x]) > ord(wordArray[y][x-1:x])):
                        index = y
                        break
                    else:
                        break

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
if(args.test):
    output = []
    expected = []
    expectedFile = open("./TestData/TestText.txt",'r')
    for wordRows in wordArray:
        for words in wordRows:
            output.append(words)
    for words in expectedFile.readlines():
        expected.append(words.strip())
    result = test_selectionSort(output,expected)
    if(result == -1):
        assert result == -1
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

