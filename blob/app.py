from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

@app.route('/')
def home():
    features = [
        {
            'title': 'Flask',
            'description': 'Built with Flask, a lightweight WSGI web application framework.',
            'icon': '/static/file.svg'
        },
        {
            'title': 'Python',
            'description': 'Powered by Python for efficient backend development.',
            'icon': '/static/window.svg'
        },
        {
            'title': 'Modern Stack',
            'description': 'Beautiful, responsive designs with modern web technologies.',
            'icon': '/static/globe.svg'
        }
    ]
    return render_template('index.html', features=features)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/contact')
def contact():
    contact_info = [
        {
            'label': 'Email',
            'value': 'Legolaswyq@gmail.com',
            'href': 'mailto:Legolaswyq@gmail.com'
        },
        {
            'label': 'Phone',
            'value': '0221041307',
            'href': 'tel:0221041307'
        },
        {
            'label': 'LinkedIn',
            'value': 'Yuqi Wang',
            'href': 'https://www.linkedin.com/in/yuqi-wang-74a84b218/'
        }
    ]
    return render_template('contact.html', contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True)
