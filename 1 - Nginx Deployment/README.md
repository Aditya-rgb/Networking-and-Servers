# My Profile Website

## Introduction

Created a basic front-end website showcasing my profile. Additionally, developed a basic FLASK application to render the website seamlessly on localhost.

## Features

- Basic front-end website.
- FLASK application for seamless rendering.
- Tested on IP addresses.
- Setup Nginx to host the FLASK application.

## Prerequisites

- Python installed on your system.
- Flask library for Python.
- Nginx or Apache web server.

## Installation

1. Cloned the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python libraries:
   ```bash
   pip install flask

## Configuration
1. Flask Application
2. Create a basic FLASK application to render the website
   ``` bash
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```
3. Directory and Files Hierarchy
   Ensure the directory and files hierarchy is as follows:
   ``` bash
   project_directory/
   |-- app.py
   |-- templates/
   |   |-- index.html

