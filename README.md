# My Tweet Project

## Overview

My Tweet Project is a basic web application allowing users to post, edit, and delete tweets with media. Users can also view tweets from other users. The project uses Django for the backend and plain HTML, CSS, and JavaScript for the frontend.

## Prerequisites

- Python 3.x
- Django
- Basic knowledge of HTML, CSS, and JavaScript

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/my_tweet_project.git
cd my_tweet_project
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
