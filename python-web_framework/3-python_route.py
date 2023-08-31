"""
Flask Web Application for HBNB

This Flask web application defines two routes to respond to specific URLs.
The routes provide simple messages as responses, demonstrating basic Flask functionality.

Routes:
    - "/" : Responds with "Hello HBNB!".
    - "/hbnb" : Responds with "HBNB".

Usage:
    Run this script to start the Flask development server. Access the defined
    routes using a web browser or an HTTP client.

"""

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    A route function that responds to the root URL ("/") with a message.

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    A route function that responds to the "/hbnb" URL with a message.

    Returns:
        str: A message "HBNB".
    """
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    A route function that responds to the "/c/<text>" URL with a message.

    Returns:
        str: A message "C <text>".
    """
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    A route function that responds to the "/python/<text>" URL with a message.

    Returns:
        str: A message "Python <text>".
    """
    text = text.replace('_', ' ')
    return f'Python {text}'

if __name__ == "__main__":
    # Start the Flask development server
    # Host: 0.0.0.0 (accessible from any IP)
    # Port: 5000
    # Debug mode: True (auto-reloads on code changes)
    app.run(host='0.0.0.0', port=5000, debug=True)
