from flask import Flask, request, redirect, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ✅ Create DB connection per request
def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/")
def home():
    return render_template("contact.html")   # ✅ SHOW HTML FORM

@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.form
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO contact (name, email, phone, message)
            VALUES (%s, %s, %s, %s)
        """, (
            data["name"],
            data["email"],
            data.get("phone"),
            data.get("message")
        ))

        conn.commit()
        cur.close()
        conn.close()

        return redirect("/success")

    except Exception as e:
        return f"Error: {e}", 500


@app.route("/success")
def success():
    return "<h2 style='text-align:center'>Message sent successfully ✅</h2>"


if __name__ == "__main__":
    app.run()
