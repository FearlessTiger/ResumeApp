import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag


def parse_resume(resume_text):
    sections = resume_text.split('\n\n')  # Split resume into sections based on empty lines
    resume_data = {}

    for section in sections:
        lines = section.split('\n')
        section_header = lines[0].strip().lower()
        print(section_header)
        section_content = ' '.join(lines[1:]).strip()

        if section_header == 'education:':
            resume_data['education'] = section_content
        elif section_header == 'test scores:':
            resume_data['test_scores'] = section_content
        elif section_header == 'extracurricular activities:':
            resume_data['extracurricular_activities'] = section_content
        elif section_header == 'leadership positions:':
            resume_data['leadership_positions'] = section_content

    return resume_data

# Example usage
resume_text = '''
John Doe
Education:
- AP Calculus
- Honors Physics
- English Literature

Test Scores:
- SAT: 1500
- ACT: 32

Extracurricular Activities:
- Debate Club
- Chess Club
- Volunteer at local animal shelter

Leadership Positions:
- President, Student Council
- Captain, Varsity Basketball Team
'''

# Parsing the resume
parsed_resume = parse_resume(resume_text)

# Printing the parsed resume data
for section, content in parsed_resume.items():
    print(f"{section.capitalize()}:")
    print(content)
    print()