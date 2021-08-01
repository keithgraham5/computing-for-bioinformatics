"""
NAME:          run.py

DESCRIPTION:   File that runs the Flask application (local hosting). To run the app, run this file
               e.g. python run.py
               Open an internet browser and enter the following URL:
               http://127.0.0.1:5000/dashboard/home/
"""

from app import app
app.run()
