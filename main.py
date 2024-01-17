 
# Import necessary modules
from flask import Flask, render_template, request
from datetime import datetime

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/services')
def services():
    """Render the services page."""
    return render_template('services.html')

@app.route('/appointment')
def appointment():
    """Render the appointment page."""
    return render_template('appointment.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
