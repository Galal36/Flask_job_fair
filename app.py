from flask import Flask, render_template, abort
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key

# Sample data
jobs = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Cairo',
        'company': 'Tech Company',
        'salary': '$80,000 - $100,000',
        'posted_date': datetime(2024, 3, 15),
        'description': 'Looking for an experienced software engineer to join our team.'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Alexandria',
        'company': 'Data Corp',
        'salary': '$90,000 - $110,000',
        'posted_date': datetime(2024, 3, 14),
        'description': 'Join our data science team to work on cutting-edge projects.'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Zagazig',
        'company': 'Web Solutions',
        'salary': '$70,000 - $90,000',
        'posted_date': datetime(2024, 3, 13),
        'description': 'Frontend and backend development position available.'
    },
    {
        'id': 4,
        'title': 'Mobile Developer',
        'location': 'Cairo',
        'company': 'App Innovations',
        'salary': '$75,000 - $95,000',
        'posted_date': datetime(2024, 3, 12),
        'description': 'Looking for a skilled mobile developer to join our team.'
    },
    {
        'id': 5,
        'title': 'DevOps Engineer',
        'location': 'Giza',
        'company': 'Cloud Services',
        'salary': '$85,000 - $105,000',
        'posted_date': datetime(2024, 3, 11),
        'description': 'Join our DevOps team to help manage our cloud infrastructure.'
    }
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
    {
        'id': 5,
        'name': 'Cloud Services',
        'location': 'Giza',
        'industry': 'Cloud Computing',
        'employees_count': 90,
        'description': 'Leading cloud services provider in Egypt.',
        'website': 'https://cloudservices.com'
    }
]

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Routes
@app.route('/')
def home():
    return render_template('home.html', jobs=jobs[:3], companies=companies[:3])

@app.route('/jobs')
def list_jobs():
    return render_template('jobs_list.html', jobs=jobs)

@app.route('/jobs/<int:job_id>')
def get_job(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job is None:
        abort(404)
    return render_template('job_detail.html', job=job)

@app.route('/companies')
def list_companies():
    return render_template('companies_list.html', companies=companies)

@app.route('/companies/<int:company_id>')
def get_company(company_id):
    company = next((company for company in companies if company['id'] == company_id), None)
    if company is None:
        abort(404)
    return render_template('company_detail.html', company=company)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)