"""
Sample Vulnerable Application - Task 3 (For Security Assessment Purposes Only)
This app intentionally contains common security flaws for educational review.
"""

from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded credentials
DB_PASSWORD = "admin123"
SECRET_KEY = "mysecretkey"

# VULNERABILITY 2: Debug mode enabled in production
app.debug = True

def get_db_connection():
    conn = sqlite3.connect("users.db")
    return conn

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # VULNERABILITY 3: SQL Injection - unsanitized query
    conn = get_db_connection()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = conn.execute(query)
    user = cursor.fetchone()

    if user:
        return "Login successful"
    return "Login failed"

@app.route("/search")
def search():
    keyword = request.args.get("q")

    # VULNERABILITY 4: Reflected XSS - unsanitized output
    return f"<h1>Search results for: {keyword}</h1>"

@app.route("/download")
def download():
    filename = request.args.get("file")

    # VULNERABILITY 5: Path Traversal - no filename validation
    with open(f"files/{filename}", "r") as f:
        content = f.read()
    return content

@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")

    # VULNERABILITY 6: Command Injection - directly executing user input
    output = os.popen(cmd).read()
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
