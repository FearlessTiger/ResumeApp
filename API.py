import requests
requested_school = input("What school would you like to go too? ")

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
except:
    print(" \n ERROR, please only put 1 school at a time, and be sure you are spelling the University correctly. \n")
