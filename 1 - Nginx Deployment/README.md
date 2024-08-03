# My Profile Website

## Assignment Overview

Created a basic front-end website showcasing my profile. Developed a basic FLASK application to render the website seamlessly on localhost and set up Nginx to host the website.

## Steps Taken

1. **Creating the Website**:
   - Developed a front-end website to showcase the profile.

2. **Setting Up the FLASK Application**:
   - Created a basic FLASK application to render the website on localhost:
     ```python
     from flask import Flask, render_template

     app = Flask(__name__)

     @app.route('/')
     def home():
         return render_template('index.html')

     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5000)
     ```

3. **Testing the FLASK Application**:
   - Tested the FLASK application on the following IP addresses:
     - http://127.0.0.1:5000
     - http://192.168.0.190:5000
   - Ran the code with:
     ```bash
     python app.py
     ```

4. **Setting Up Nginx**:
   - Installed Nginx and configured it to proxy requests to the FLASK application:
     ```bash
     sudo apt-get update
     sudo apt-get install nginx
     ```
   - Edited the Nginx configuration:
     ```bash
     cd /etc/nginx/sites-enabled
     sudo nano default
     ```
   - Commented out default configuration lines:
     ```nginx
     #root /var/www/html;
     #index index.html index.htm index.nginx-debian.html;
     #index index.html index.htm index.nginx-debian.html;
      location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                #try_files $uri $uri/ =404;
     ```
   - Added following configuration to proxy requests:
     ```nginx
     location / {
         proxy_pass http://127.0.0.1:5000;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
     }
     ```
   - Restarted and tested Nginx:
     ```bash
     sudo service nginx start
     sudo service nginx reload
     sudo nginx -t
     ifconfig
     ```

5. **Configuring Domain Name**:
   - Setting up a local domain name "awesomeweb":
     ```bash
     cd /etc/
     sudo nano hosts
     ```
   - Added the following line:
     ```
     192.168.0.190 awesomeweb
     ```

6. **Testing Domain Configuration**:
   - Tested the domain name in the browser:
     - http://awesomeweb

## Conclusion

Successfully developed and deployed a profile website using FLASK and Nginx. The setup included configuring Nginx to host the FLASK application and testing the deployment both via local IP and a custom domain name.

