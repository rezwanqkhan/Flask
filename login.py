"""
Flask – Cookies
A cookie is stored on a client’s computer in the form of a text file. Its
purpose is to remember and track data pertaining to a client’s usage for
better visitor experience and site statistics.
A Request object contains a cookie’s attribute. It is a dictionary object of
all the cookie variables and their corresponding values, a client has
transmitted. In addition to it, a cookie also stores its expiry time, path and
domain name of the site.
"""
# from flask import Flask, render_template, request, make_response
#
# app = Flask(__name__)
# @app.route('/')
# def index():
#  return render_template('indexlogin.html')
#
# """The Form is posted to ‘/setcookie’ URL. The associated view function
# sets a Cookie name userID and renders another page."""
# The readcookie.html file is missed
# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
#    if request.method == 'POST':
#      user = request.form['nm']
#      resp = make_response(render_template('readcookie.html'))
#      resp.set_cookie('userID', user)
#    return resp
# """‘indexlogin.html’ contains a hyperlink to another view function
# getcookie(), which reads back and displays the cookie value in browser."""
# @app.route('/getcookie')
# def getcookie():
#   name = request.cookies.get('userID')
#   return '<h1>welcome '+name+'</h1>'
#
# if __name__ == '__main__':
#     app.run(debug=True)

"""
Flask – Sessions
Like Cookie, Session data is stored on client. Session is the time interval
when a client logs into a server and logs out of it. The data, which is
needed to be held across this session, is stored in the client browser.
A session with each client is assigned a Session ID. The Session data is
stored on top of cookies and the server signs them cryptographically. 
Forthis encryption, a Flask application needs a defined SECRET_KEY.
"""
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "any random string"

# The following code is a simple demonstration of session works in Flask.
# URL ‘/’ simply prompts user to log in, as session variable ‘username’ is
# not set.
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"

# As user browses to ‘/login’ the login() view function, because it is called
# through GET method, opens up a login form.
# A Form is posted back to ‘/login’ and now session variable is set.
# Application is redirected to ‘/’. This time session variable ‘username’ is
# found.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action="" method="post">
        <p><input type="text" name="username"/></p>
        <p><input type="submit" value="Login"/></p>
    </form>'''

# The application also contains a logout() view function, which pops out
# ‘username’ session variable. Hence, ‘/’ URL again shows the opening
# page.
@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

# Run the application and visit the homepage. (Ensure to set secret_key of
# the application)
if __name__ == '__main__':
    app.run(debug=True)
