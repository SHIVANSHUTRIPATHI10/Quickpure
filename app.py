from flask import Flask, request, redirect, url_for, render_template
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "contact.db"

# ---------- DATABASE INIT ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------
@app.route("/")
def home():
    success = request.args.get("success")
    return render_template("index.html", success=success)

@app.route("/save", methods=["POST"])
def save():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)",
        (name, email, phone, message)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home", success="1"))


@app.route("/admin/data")
def admin_data():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    conn.close()
    return {"data": data}
@app.route("/test")
def test():
    return "TEST OK"


if __name__ == "__main__":
    app.run()
