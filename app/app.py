import os
import subprocess
import sqlite3

DB_NAME = "test.db"

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ❌ SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def ping(host):
    # ❌ Command Injection
    subprocess.call("ping -c 1 " + host, shell=True)

# ❌ Hardcoded secret
API_KEY = "AKIA1234567890SECRET"
