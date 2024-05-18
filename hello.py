from flask import Flask, render_template

app = Flask(__name__)

# 1
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# 2
# @app.route('/hello/<name>')
# def hello_name(name):
#       return 'Hello %s!' % name
# http://127.0.0.1:5000/hello/Rashid
# output  Hello Rashid!

# 3
# we can just inter int num
# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#      return 'Blog Number %d' % postID
# # we can just inter the float num
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number %f' % revNo


"""
The url_for() function is very useful for dynamically building a URL for a
specific function. The function accepts the name of a function as first
argument, and one or more keyword arguments, each corresponding to
the variable part of URL.
The following script demonstrates use of url_for() function."""
# from flask import Flask, redirect, url_for
#
#
# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'
#
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello %s as Guest' % guest
#
#
# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))

# from flask import Flask, redirect, url_for, request
#
# login.html is used the following code
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))


"""
Flask – Templates
It is possible to return the output of a function bound to a certain URL in
the form of HTML. For instance, in the following script, hello() function
will render ‘Hello World’ with <h1> tag attached to it.
"""

# @app.route('/')
# def index():
#     return '<html><body><h1>Hello World</h1></body></html>'

"""This is where one can take advantage of Jinja2 template engine, on which
Flask is based. Instead of returning hardcode HTML from the function, a
HTML file can be rendered by the render_template() function."""
from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def index():
#    return render_template('hello.html')

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)

# Flask will try to find the HTML file in the templates folder, in the same
# folder in which this script is present.
# Application folder
# Hello.py
# templates
#      hello.html
"""
The Jinja2 template engine uses the following delimiters for escaping
from HTML.
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements
"""

# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/hello/<int:score>')
# def hello_name(score):
#      return render_template('hello.html', marks=score)
# """ for:
# http://127.0.0.1:5000/hello/80
# Your result is pass!
# """

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/result')
# def result():
#      dict = {'phy':50,'che':60,'maths':70}
#      return render_template('result.html', result = dict)


"""
Flask – Static Files
A web application often requires a static file such as a javascript file or a
CSS file supporting the display of a web page. Usually, the web server is
configured to serve them for you, but during the development, these files
are served from static folder in your package or next to your module and it
will be available at /static on the application.
A special endpoint ‘static’ is used to generate URL for static files.
"""

# from flask import Flask, render_template
# Say hello alert exmple
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return render_template("index.html")
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result1', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result1.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
