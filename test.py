import nltk
import re

nltk.download()

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

    # Tokenize the resume text into sentences
    sentences = sent_tokenize(resume_text)

    for sentence in sentences:
        # Tokenize each sentence into words
        words = word_tokenize(sentence)

        # Perform part-of-speech tagging to identify named entities
        tagged_words = pos_tag(words)

        # Extract information based on named entities and patterns
        for word, tag in tagged_words:
            if tag == 'NNP' and not name:
                name = word
            elif re.match(r'\S+@\S+', word) and not email:
                email = word
            elif re.match(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', word) and not phone:
                phone = word

        # You can add more parsing logic here to extract skills, experience, and education.

    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": skills,
        "Experience": experience,
        "Education": education
    }

if __name__ == "__main__":
    # Example resume text (replace with your actual resume text)
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

    parsed_resume = parse_resume(resume_text)

    # Print the parsed information
    for key, value in parsed_resume.items():
        print(f"{key}: {value}")
