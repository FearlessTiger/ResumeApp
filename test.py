import nltk
import re

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

def parse_resume(resume_text):
    # Initialize variables to store parsed information
    name = None
    email = None
    phone = None
    skills = []
    experience = []
    education = []

    text = re.sub(r"[^a-zA-Z0-9]", " ", resume_text.lower())
    words = text.split()

    sentances = sent_tokenize(resume_text)
    email_expression = "\A[\w!#$%&'*+/=?`{|}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+)*@↵(?:[A-Z0-9-]+\.)+[A-Z]{2,6}\Z"
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", resume_text)
    return emails
    



    return sentences
    
    
resume_text = """
    John Doe
    john.doe@email.com
    (123) 456-7890

    Skills:
    - Python
    - Data Analysis
    - Machine Learning

    Experience:
    - Data Scientist, Company X, 2020-present
      - Conducted data analysis and built machine learning models.

    Education:
    - Bachelor's in Computer Science, University Y, 2019
    """
print(parse_resume(resume_text))