from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="quickpure_user",
    password="Quickpure@2025",
    database="contact_db"
)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO contact_us (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        db.commit()

        return "✅ Message sent successfully!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
