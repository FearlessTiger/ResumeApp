from flask import Flask, render_template, request
import PyPDF2

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
    pdf_reader = PyPDF2.PdfReader(file)
    page = pdf_reader.pages[0]
    return page.extract_text()

if __name__ == "__main__":
    app.run(debug=True)
