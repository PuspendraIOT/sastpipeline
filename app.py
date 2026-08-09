# app.py
import os

print("Starting our dummy application...")

# FIXED: The password is now safely loaded from the environment
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")

def login():
    print("Connecting to the database...")

login()
