import sqlite3
from flask import Flask, request

app = Flask(__name__)

# TRAINING ONLY - intentionally fake value for secrets-scanning practice.
# Do not use real credentials in this lab.
FAKE_API_KEY = "sk_test_FAKE1234567890_DO_NOT_USE"

@app.route("/")
def home():
    return "Product Security Vulnerability Management Lab"

@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")

    # TRAINING ONLY - intentionally insecure SQL pattern for SAST practice.
    query = "SELECT * FROM users WHERE id = " + user_id

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    return {"result": str(result)}

if __name__ == "__main__":
    app.run(debug=True)