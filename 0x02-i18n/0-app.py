#!/usr/bin/env python3
# it is the introduction of the first task
# in this task will display basic Flask app
# and to do this we should have to import jinja and flask from Flask
from flask import Flask, render_template

app = Flask(__name__)

# Try to call the app through the app


@app.route('/')
# Create a function to call the html file from the template folder
def hello():
        return render_template('0-index.html')


    if __name__ == "__main__":
            app.run(debug=True)

