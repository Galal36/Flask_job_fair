# Flask Job Portal

A modern job portal application built with Flask, featuring job listings and company profiles.

## Features

- Browse available jobs
- View company profiles
- Responsive design using Bootstrap
- Error handling for 404 and 500 errors
- Clean and organized code structure

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Galal36/Flask_job_fair.git
cd Flask_job_fair
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
Flask_job_fair/
├── app.py              # Main application file
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── home.html      # Homepage
│   ├── jobs_list.html # Jobs listing page
│   ├── job_detail.html # Individual job page
│   ├── companies_list.html # Companies listing page
│   ├── company_detail.html # Individual company page
│   ├── 404.html       # 404 error page
│   └── 500.html       # 500 error page
└── README.md          # This file
```

## Contributing

Feel free to submit issues and enhancement requests! 