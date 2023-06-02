from flask import Flask, render_template, request, jsonify
import PyPDF2
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag




app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/start')
def start():
    return render_template('start.html')

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        page = pdf_reader.pages[0]
        resume = page.extract_text()
        resumedata(resume)
        return resume
    except:
        return "Error"

@app.route('/get_school_data', methods=['POST'])
def get_school_data():
    requested_school = request.form['searchInput']

    # Set the API endpoint URL
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

    # Set the API parameters
    params = {
        'api_key': 'MnUaufQkXtASro2Exr2pidQCXJbx9wNWjBxsSf3g',
        'school.name': {requested_school},
        '_fields': 'id,school.name,latest.admissions.admission_rate.overall,' + \
                   'latest.admissions.sat_scores.midpoint.math,' + \
                   'latest.admissions.sat_scores.midpoint.critical_reading,' + \
                   'latest.admissions.sat_scores.midpoint.writing,' + \
                   'latest.admissions.act_scores.midpoint.cumulative'
    }

    # Make the API call
    try:
        response = requests.get(url, params=params)
        # Get the admission rate, SAT score midpoint, and ACT score midpoint data from the response
        result = response.json()['results'][0]
        admission_rate = result['latest.admissions.admission_rate.overall']
        sat_math_midpoint = result['latest.admissions.sat_scores.midpoint.math']
        sat_reading_midpoint = result['latest.admissions.sat_scores.midpoint.critical_reading']
        sat_writing_midpoint = result['latest.admissions.sat_scores.midpoint.writing']
        act_cumulative_midpoint = result['latest.admissions.act_scores.midpoint.cumulative']
        # Print the admission rate, SAT score midpoint, and ACT score midpoint data
        print(f"The admission rate for {params['school.name']} is {admission_rate}")
        print(f"The SAT score midpoint for Math is {sat_math_midpoint}")
        print(f"The SAT score midpoint for Critical Reading is {sat_reading_midpoint}")
        print(f"The SAT score midpoint for Writing is {sat_writing_midpoint}")
        print(f"The ACT score midpoint (cumulative) is {act_cumulative_midpoint}")

        # Send the data to Flask function using a POST request
        api_data = {
            "admission_rate": admission_rate,
            "sat_math_midpoiont": sat_math_midpoint,
            "sat_reading_midpoint": sat_reading_midpoint,
            "sat_writing_midpoint": sat_writing_midpoint,
            "act_cumulative_midpoint": act_cumulative_midpoint
        }
        
        
        
        return api_data
    except:
        return (" \n ERROR, please only put 1 school at a time, and be sure you are spelling the University correctly. \n")
    
def resumedata(resume):
    data = {}
    resume = resume.lower()
    # Define a regular expression pattern to match GPA values
    gpa_pattern = r"\bgpa\b\s*:\s*([\d.]+)"

    # Search for the GPA value in the resume text using the regular expression
    match_gpa = re.search(gpa_pattern, resume)

    if match_gpa:
        # If a match is found, extract the GPA value
        gpa = match_gpa.group(1)
        print(f"GPA: {gpa}")
        data.update({"GPA" : gpa})
    else:
        print("GPA not found in the resume text.")

    sections = resume.split('\n\n')  # Split resume into sections based on empty lines
    resume_data = {}
    print(sections)

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

    print(resume_data)

        
        

if __name__ == "__main__":
    app.run(debug=True)

