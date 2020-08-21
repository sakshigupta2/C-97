introString = input("enter your intoduction: ")
characterCount = 0
wordCount = 1
for i in introString: 
    characterCount = characterCount + 1
    if(i == " "):
        wordCount = wordCount + 1
print("number of words in a string: ")
print(wordCount)
print("number of characters in a string: ")
print(characterCount)