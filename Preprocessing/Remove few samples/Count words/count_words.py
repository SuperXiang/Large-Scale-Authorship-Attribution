####################################################################################################################################################
#
# The script aims to count the words in each sample. It can also count
# the lines, words and characters in the sample.
#
# Environment Requirement: Python 3.5, Anaconda3
# Date of Last Modified: 03/14/2016
# Author: Yingfei(Jeremy) Xiang
#
####################################################################################################################################################

import os

# Type the destination path which sample locates
file = open("C:/Users/sony/Desktop/Count_words/test_sample.txt","r")

wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for x1,x2 in wordcount.items():
    print(x1, x2)

# Export the words and the number of their appearance to 'count_result.txt'
file = open("count_result.txt","w")
for x1,x2 in wordcount.items():
	file.write("{0}: {1}\n".format(x1,x2))
file.close()


# Count the lines, words and characters in the sample
line_counts = 0  
word_counts = 0  
character_counts = 0  

# Type the destination path which sample locates
with open("C:/Users/sony/Desktop/Count_words/test_sample.txt", "r") as f:  
    for line in f:  
        words = line.split()  

        line_counts += 1  
        word_counts += len(words)  
        character_counts += len(line)  

print("line_number: ", line_counts)  
print("word_number: ", word_counts) 
print("character_number: ", character_counts)

# Export the number of the lines, words and characters in the sample to'count_result.txt'
with open("count_result.txt","a") as countnew:
	countnew.write("line_number: {0}; word_number: {1}; character_number: {2}\n".format(line_counts,word_counts,character_counts))
countnew.close()

