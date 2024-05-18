# Flask Application Repository

Welcome to the Flask Application Repository. This project is a basic introduction to Flask, a lightweight WSGI web application framework in Python. This repository contains code examples up to the section "Flask – Message Flashing" from the Flask Quick Guide.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
  - [Hello World](#hello-world)
  - [Variable Rules](#variable-rules)
  - [URL Building](#url-building)
  - [HTTP Methods](#http-methods)
  - [Templates](#templates)
  - [Static Files](#static-files)

## Introduction

Flask is a micro web framework written in Python. It is designed to be easy to use and extend, making it ideal for small to medium-sized web applications. Flask does not require particular tools or libraries, making it flexible and adaptable to various use cases.

## Installation

To set up this Flask project, follow the steps below:

1. **Clone the Repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set Up Virtual Environment:**

    Install `virtualenv` if you haven't already:

    If you are using pycharm IDE during the creating project you can generate the .venv .
    ```sh
    pip install virtualenv
    ```

    Create and activate a virtual environment:

    ```sh
    virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Flask:**

    Install Flask within the virtual environment:

    ```sh
    pip install Flask
    ```
## Usage

To run the Flask application, execute the following command:

```sh
python hello.py
```
This will start a development server on http://127.0.0.1:5000/. Open this URL in your browser to see the application in action.

## Features
The repository includes examples of the following Flask features:

-Routing: Define URL routes to handle different web requests.
-Variable Rules: Create dynamic URLs by defining routes with variable parts.
-URL Building: Use url_for() to build URLs dynamically.
-HTTP Methods: Handle different HTTP methods like GET and POST.
-Templates: Render HTML templates using Jinja2, Flask's template engine.
-Static Files: Serve static files such as CSS and JavaScript.

## Examples

```sh
Hello World
python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
```
## Variable Rules
```sh
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True)
```
## URL Building

```sh
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'Hello {guest} as Guest'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
    app.run(debug=True)
```
## HTTP Methods
- Create a Form (login.html):
```sh
html
Copy code
<html>
   <body>
      <form action="http://localhost:5000/login" method="post">
         <p>Enter Name:</p>
         <p><input type="text" name="nm" /></p>
         <p><input type="submit" value="submit" /></p>
      </form>
   </body>
</html>
```
- Handle Form Submission:
```sh
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
```
## Templates
- Render HTML Template:

```sh
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)
```
- Template File (hello.html):

```sh
<!doctype html>
<html>
   <body>
      <h1>Hello {{ name }}!</h1>
   </body>
</html>
```
## Static Files

- Serving Static Files:

Place your static files (e.g., CSS, JavaScript) in the static folder within your project directory.

Example project structure:

```sh
/project
    /static
        /css
            style.css
        /js
            script.js
    hello.py
```
- Access Static Files:

In your HTML templates, you can refer to the static files using the url_for() function.

```sh
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```
## HAPPY CODDING
 - Rezwanullah QURAISHI



