import PyPDF2
import re

def extract_name(text):
    # Extract the name from the resume text
    name_regex = r"([A-Z][a-z]+)(\s[A-Z][a-z]+)*"
    name_match = re.search(name_regex, text)
    if name_match:
        return name_match.group(0)
    return ""

def extract_email(text):
    # Extract the email address from the resume text
    email_regex = r"[\w\.-]+@[\w\.-]+\.\w+"
    email_match = re.search(email_regex, text)
    if email_match:
        return email_match.group(0)
    return ""

def extract_phone_number(text):
    # Extract the phone number from the resume text
    phone_regex = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
    phone_match = re.search(phone_regex, text)
    if phone_match:
        return phone_match.group(0)
    return ""

def extract_skills(text):
    # Extract skills from the resume text
    skills = ["Python", "Java", "C++", "SQL"]  # Add more skills as needed
    extracted_skills = []
    for skill in skills:
        if skill.lower() in text.lower():
            extracted_skills.append(skill)
    return extracted_skills

def extract_test_scores(text):
    # Extract test scores from the resume text
    test_scores = []
    test_regex = r"(SAT|ACT|GRE|GMAT):\s?(\d+)"
    test_matches = re.findall(test_regex, text)
    for match in test_matches:
        test_scores.append({"Test": match[0], "Score": match[1]})
    return test_scores

def extract_courses(text):
    # Extract courses from the resume text
    courses = []
    course_regex = r"Courses?:\s?(.+?)(?:(?:\n{2,})|\Z)"
    course_match = re.search(course_regex, text, re.DOTALL)
    if course_match:
        courses_text = course_match.group(1)
        courses = re.findall(r"\b[A-Z]{2,}\b(?:\s+\d{3})?", courses_text)
    return courses

def parse_resume(file_path):
    # Parse the resume PDF and extract relevant information
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

    name = extract_name(text)
    email = extract_email(text)
    phone_number = extract_phone_number(text)
    skills = extract_skills(text)
    test_scores = extract_test_scores(text)
    courses = extract_courses(text)

    # Return the extracted information as a dictionary
    resume_data = {
        "Name": name,
        "Email": email,
        "Phone Number": phone_number,
        "Skills": skills,
        "Test Scores": test_scores,
        "Courses": courses
    }
    return resume_data

# Usage example
resume_file = "ResumeFeb2023.pdf"  
parsed_data = parse_resume(resume_file)
print(parsed_data)


