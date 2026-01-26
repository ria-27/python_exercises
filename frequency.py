# Write a python code block that inputs a sentence from the user.
# Count the frequency of each word in the sentence and store the result in a dictionary.
# Print the dictionary with words as keys and their frequencies as values.
sentence=input("Enter sentence: ")
words=sentence.split()
word_freq={}             #creating an empty dictionary
for word in words:       # "go through each item in the list words one by one and temporarily call it word"
    frequency=words.count(word)    #word=current item being processed
    word_freq[word]=frequency   #stores word in dictionary
print(word_freq)