from trained_classifier import *

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from bs4 import BeautifulSoup

import re

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def remove_html(content):
    '''This function removes extra html tags'''
    return  BeautifulSoup(content, "html.parser").get_text()
def keep_alpha(content):
    '''This function retains all alpha-characters, replacing invalid characters with spaces'''
    return re.sub("[^a-zA-Z]", " ", content)

def lower(content):
    '''This function converts all characters to lowercase to allow for
    uniform word checking, removing the need to check for both capital and lowercase
    verisions of words'''
    return content.lower()

def split_list(content):
    '''This function converts a string to a list, separating words into individual elements
    at each whitespace'''
    return content.split()

def remove_stopwords(content):
    '''This function removes stopwords from the current list of words'''
    return [w for w in content if not w in stopwords.words('english')]

from nltk.stem import PorterStemmer as PS
def stem(content):
    stemmed_content = []
    for word in content:
        stemmed_content.append(PS().stem(word))
    return stemmed_content

def clean_content(content):
    '''This function cleans up the raw comment, returning a list of sanitized words'''
    return remove_stopwords(split_list(lower(keep_alpha(remove_html(content)))))

def probabilityWord(word, label):
    if label == 1:
        return spamWords.get(word, 1) / positive_count
    return hamWords.get(word, 1) / negative_count

def probabilityContent(content, label):
    content = clean_content(content)
    result = 1.0
    for word in content:
        result *= probabilityWord(word, label)
    return result

def classifier(content):
    global spam_per, ham_per
    spam_prob = spam_per * probabilityContent(content, 1)
    ham_prob = ham_per * probabilityContent(content, 0)
    return spam_prob > ham_prob