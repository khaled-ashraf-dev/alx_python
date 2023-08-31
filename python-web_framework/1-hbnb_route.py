from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Enable debug mode for the application
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

if __name__ == "__main__":
    # Start the Flask development server
    # Host: 0.0.0.0 (accessible from any IP)
    # Port: 5000
    # Debug mode: True (auto-reloads on code changes)
    app.run(host='0.0.0.0', port=5000, debug=True)
