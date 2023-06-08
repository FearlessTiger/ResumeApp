from flask import Flask, render_template, request, jsonify
import PyPDF2
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

nltk.download('stopwords')



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
    
def skill_exists(skill):
    url = f'https://api.apilayer.com/skills?q={skill}&amp;count=1'
    headers = {'apikey': 'iHJJHf2OGCMoMVP2NhT6c63ZH2SeGeyY'}
    response = requests.request('GET', url, headers=headers)
    result = response.json()
 
    if response.status_code == 200:
        return len(result) &gt; 0 and result[0].lower() == skill.lower()
    raise Exception(result.get('message'))

   
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

    #Skills extraction
    
    
        
        

if __name__ == "__main__":
    app.run(debug=True)

