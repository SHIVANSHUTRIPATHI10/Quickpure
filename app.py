from flask import Flask, request,url_for, redirect, render_template
import sqlite3

app = Flask(__name__)
def __init__db():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
                   name TEXT NOT NULL,   
                   email TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   message TEXT NOT NULL
                   )
                   ''')
    
    conn.commit()
    conn.close

__init__db()
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)", (name, email, phone, message))
    conn.commit()
    conn.close()
    return redirect(url_for("home",success="1"))
 

if __name__ == "__main__":
    app.run()
