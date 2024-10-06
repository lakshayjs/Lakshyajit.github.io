#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lakshyajit Singh 100921673

from collections import Counter
import re
import os

class WordCounter:
    # Preparing a regular expression for word detection
    word_pattern = re.compile(r"\b\w+\b")
    
    def __init__(self, filename):
        # Check if the file exists to avoid FileNotFoundError
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")
            
        # Initializing the counter
        self.words_dict = Counter()
        
        # Read file and count words
        with open(filename, 'r') as file:
            text = file.read().lower()  # Making the text lowercase 
            text = self.remove_punctuation(text)  # Stripping punctuations
            words = self.word_pattern.findall(text)  # Finding all words using the pattern
            self.words_dict.update(words)  # Counting words
    
    def remove_punctuation(self, text):
        # List of punctuations to remove
        punctuations = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"
        # Removing punctuations
        return text.translate(str.maketrans('', '', punctuations))
    
    def get_words_dict(self):
        # Returning the dictionary with word counts
        return self.words_dict
    
    def top_10_words(self):
        # Printing the top 10 words
        for index, (word, count) in enumerate(self.words_dict.most_common(10)):
            print(f"{index}: ('{word}', {count})")

# Example usage:
# Define the path to your text file
file_path = 'C:/Users/laksh/Downloads/ontario tech uni.txt'

try:
    # Using the WordCounter with the provided text file
    word_counter = WordCounter(file_path)
    # Displaying the top 10 words
    word_counter.top_10_words()
except FileNotFoundError as e:
    print(e)


# In[ ]:




