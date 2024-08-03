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
3. Ensure the directory and files hierarchy is as follows:
   ``` bash
   project_directory/
   |-- app.py
   |-- templates/
   |   |-- index.html

## Usage
1. Run the FLASK application
   ``` bash
   python app.py
   ```
2. Access the website on your browser
   ``` bash
   http://127.0.0.1:5000
   ```
## Testing
1. Test the FLASK application on your browser using the above IP addresses.
2. You can run the code from VS Code or your terminal.

## Troubleshooting
### Setting up Nginx
    ``` bash
    sudo apt-get update
    ```
### Update the system:
    ``` bash
    sudo apt-get install nginx
    ```
### Configuring Nginx
1. Navigate to the Nginx configuration directory:
   ``` bash
   cd /etc/nginx/sites-enabled
   ```
2. Edit the default configuration file
   ``` bash
   sudo nano default
   ```
4. Comment out the following lines:
   ``` bash
   #root /var/www/html;
   #Add index.php to the list if you are using PHP
   #index index.html index.htm index.nginx-debian.html;
   location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                #try_files $uri $uri/ =404;
   ```
5. Add the following configuration:
   ``` bash
   location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
              }
   ```
