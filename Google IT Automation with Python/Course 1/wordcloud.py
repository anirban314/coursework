# Coursera, Google IT Automation with Python
# Course 1, Crash Course on Python
# FINAL ASSIGNMENT
# Generating Wordcloud from Text File


# Here are all the installs and imports you will need for your word cloud script and uploader widget
'''
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')
'''
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed.
# **IMPORTANT!** If this was your first time running the above cell containing the installs and imports, you will need save this notebook now.
# Then under the File menu above, select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the
# necessary changes will take affect. To upload your text file, run the following cell that contains all the code for a custom uploader widget.
# Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# This is the uploader widget
def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process.
# This was a lot of preliminary work, but you are now ready to begin your script. Write a function in the cell below that iterates through the
# words in *file_contents*, removes punctuation, and counts the frequency of each word. Oh, and be sure to make it ignore word case, words that
# do not contain all alphabets and boring words like "and" or "the". Then use it in the 'generate_from_frequencies' function to generate your
# very own word cloud! **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the
# 'generate_from_frequencies' function.

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you",
        "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this",
        "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with",
        "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
        "can", "will", "just"]

    # LEARNER CODE START HERE ---------------------------------------
    punctuations += '“”'  #additional punctuations that occur in the text
    uninteresting_words.extend(["in", "for", "not", "on", "so", "one", "there", "would", "up", "only", "said", "out", "now", "man", "though",
        "about", "then", "come", "like", "go", "went", "shall", "could"]) #additional boring words to skip
    file_processed = ''

    # Remove Punctuations (Except: hyphenated words, possesive nouns, contractions)
    for char in file_contents:
        if char == '—':  #replace em dashes with spaces to maintain word separation
            file_processed += ' '
        elif char not in punctuations:
            file_processed += char
    list_of_words = file_processed.lower().split()  #ignore case and store all words in a list
    file_processed = {}

    # Count Frequency and Store in Dictionary
    for word in list_of_words:
        if word not in uninteresting_words and word.isalpha():
            if word in file_processed:
                file_processed[word] += 1
            else:
                file_processed[word] = 1
    # END OF LEARNER CODE--------------------------------------------

    #WordCloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(file_processed)
    return cloud.to_array()

# If you have done everything correctly, your word cloud image should appear after running the cell below. Fingers crossed!

# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

# If your word cloud image did not appear, go back and rework your 'calculate_frequencies' function until you get the desired output.
# Definitely check that you passed your frequecy count dictionary into the 'generate_from_frequencies' function of 'wordcloud'.
# Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!