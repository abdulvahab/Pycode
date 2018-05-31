#random_words

WORDS=["ABDULVAHAB","ABDULVAHAB","ABDULREHMAN","MUSU","FATEMA"]
print_word = []
for word in WORDS:
    if word in print_word:
        print ()
    else:
        print(word)
        print_word.append(word)
    
