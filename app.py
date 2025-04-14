from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")

def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])

def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    return render_template("submit.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)