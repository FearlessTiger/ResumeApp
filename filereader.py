from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        page = pdf_reader.pages[0]
        x = page.extract_text()
        return page.extract_text()
    except:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True)
