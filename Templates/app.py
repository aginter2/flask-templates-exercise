from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", page_title="Home Page")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        return render_template(
            "contact.html",
            page_title="Contact",
            success_message=f"Thank you {name}! We received your email: {email}"
        )

    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(debug=True)