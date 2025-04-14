from flask import Flask, render_template, request, url_for

form_app = Flask(__name__)

@form_app.route("/")

def form():
    return render_template("form.html")

@form_app.route("/submit", methods=["POST"])

def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    return render_template("submit.html", name=name, email=email)

if __name__ == "__main__":
    form_app.run(debug=True)