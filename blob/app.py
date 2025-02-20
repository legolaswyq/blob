from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create tables
with app.app_context():
    db.create_all()

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

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Successfully signed in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('signin'))
            
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not all([name, email, password]):
            flash('All fields are required', 'error')
            return redirect(url_for('register'))
            
        if len(password) < 8:
            flash('Password must be at least 8 characters long', 'error')
            return redirect(url_for('register'))
            
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
            
        # Create new user
        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password)
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please sign in.', 'success')
            return redirect(url_for('signin'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('register'))
            
    return render_template('register.html')

@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash('Successfully signed out!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
