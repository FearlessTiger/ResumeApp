from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file_contents = file.read()
    print(file_contents)
    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
