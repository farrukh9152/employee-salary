from flask import Flask, render_template

app = Flask(__name__)

# Sample employee salary data
employees = [
    {"id": 1, "name": "Faizan", "role": "DevOps Engineer", "salary": 70000},
    {"id": 2, "name": "Ayesha", "role": "Software Developer", "salary": 65000},
    {"id": 3, "name": "Rahul", "role": "Cloud Engineer", "salary": 72000},
    {"id": 4, "name": "Neha", "role": "QA Engineer", "salary": 55000}
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
