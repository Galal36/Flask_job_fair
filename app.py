from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import current_user
from forms import JobApplicationForm
from datetime import datetime
import os
from extensions import db, mail, login_manager
from flask_bootstrap import Bootstrap
from auth import auth  # Import the auth blueprint
from models import User  # Import User model for the user_loader
from flask_mail import Message

# Initialize applications list
applications = []  # In a real app, you would use a database

def send_password_reset_email(user):
    app = Flask.current_app
    try:
        token = user.get_reset_password_token()
        msg = Message('Password Reset Request',
                    recipients=[user.email],
                    subject='Password Reset Request')
        reset_url = url_for('auth.reset_password', token=token, _external=True)
        msg.body = f'''To reset your password, visit the following link:
{reset_url}

If you did not make this request then simply ignore this email and no changes will be made.

This link will expire in 1 hour.
'''
        msg.html = f'''
        <p>To reset your password, <a href="{reset_url}">click here</a>.</p>
        <p>If you did not make this request then simply ignore this email and no changes will be made.</p>
        <p>This link will expire in 1 hour.</p>
        '''
        mail.send(msg)
        app.logger.info(f'Password reset email sent to {user.email}')
        return True
    except Exception as e:
        app.logger.error(f'Failed to send email: {str(e)}')
        app.logger.exception('Detailed error:')
        return False

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Email Configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'hungrypy@gmail.com'
    app.config['MAIL_PASSWORD'] = 'kibn pekx logq qhmw'
    app.config['MAIL_DEFAULT_SENDER'] = 'hungrypy@gmail.com'
    app.config['MAIL_MAX_EMAILS'] = 5
    app.config['MAIL_ASCII_ATTACHMENTS'] = False
    app.config['MAIL_SUPPRESS_SEND'] = False
    app.config['MAIL_DEBUG'] = True

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    Bootstrap(app)

    # Register blueprints
    app.register_blueprint(auth)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Add this inside create_app() function, before your routes
    jobs = [
        {
            'id': 1,
            'title': 'Python Developer',
            'company': 'Tech Company',
            'location': 'Cairo',
            'salary': '$3000-$4000',
            'description': 'We are looking for a Python developer with experience in Flask and Django.',
            'posted_date': '2023-05-15'
        },
        {
            'id': 2,
            'title': 'Data Analyst',
            'company': 'Data Corp',
            'location': 'Alexandria',
            'salary': '$2500-$3500',
            'description': 'Seeking a data analyst with strong SQL and visualization skills.',
            'posted_date': '2023-05-10'
        },
        {
            'id': 3,
            'title': 'Frontend Developer',
            'company': 'Web Solutions',
            'location': 'Zagazig',
            'salary': '$2000-$3000',
            'description': 'Looking for a frontend developer with React experience.',
            'posted_date': '2023-05-05'
        },
        {
            'id': 4,
            'title': 'Mobile App Developer',
            'company': 'App Innovations',
            'location': 'Cairo',
            'salary': '$3500-$4500',
            'description': 'Experienced mobile app developer needed for iOS and Android platforms.',
            'posted_date': '2023-05-01'
        },
    ]

    companies = [
        {
            'id': 1,
            'name': 'Tech Company',
            'location': 'Cairo',
            'industry': 'Software Development',
            'employees_count': 150,
            'description': 'Leading software development company in Egypt.',
            'website': 'https://techcompany.com'
        },
        {
            'id': 2,
            'name': 'Data Corp',
            'location': 'Alexandria',
            'industry': 'Data Analytics',
            'employees_count': 75,
            'description': 'Specialized in big data and analytics solutions.',
            'website': 'https://datacorp.com'
        },
        {
            'id': 3,
            'name': 'Web Solutions',
            'location': 'Zagazig',
            'industry': 'Web Development',
            'employees_count': 45,
            'description': 'Full-service web development agency.',
            'website': 'https://websolutions.com'
        },
        {
            'id': 4,
            'name': 'App Innovations',
            'location': 'Cairo',
            'industry': 'Mobile Development',
            'employees_count': 60,
            'description': 'Leading mobile app development company in Egypt.',
            'website': 'https://appinnovations.com'
        },
    ]

    @app.route('/')
    def home():
        return render_template('home.html', jobs=jobs[:3], companies=companies[:3])

    @app.route('/jobs')
    def list_jobs():
        return render_template('jobs_list.html', jobs=jobs)

    @app.route('/jobs/<int:job_id>')
    def job_detail(job_id):
        job = next((job for job in jobs if job['id'] == job_id), None)
        if not job:
            return render_template('404.html'), 404
        return render_template('job_detail.html', job=job)

    @app.route('/companies')
    def list_companies():
        return render_template('companies_list.html', companies=companies)

    @app.route('/companies/<int:company_id>')
    def company_detail(company_id):
        company = next((company for company in companies if company['id'] == company_id), None)
        if not company:
            return render_template('404.html'), 404
        return render_template('company_detail.html', company=company)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
