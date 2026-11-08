# Wildfire Tracker 🔥

Get wildfire events using the NASA Earth Observatory Natural Event Tracker (EONET) API.

## Usage

### View the deployed app
Open the live app in a browser:
`https://wildfire-tracker-zeta-khaki.vercel.app`

### Run the Django app locally
From the project root, run:
`python3 django/manage.py runserver`

Then open:
`http://127.0.0.1:8000`

### Run the CLI script locally
From the project root, run:
`python3 main.py <state> <year>`

Example:
`python3 main.py california 2024`

## Project structure
- `main.py` — CLI script that fetches wildfire data from NASA EONET
- `django/` — Django web app and project configuration
- `django/templates/` — HTML templates
- `django/static/` — CSS, JS, and image assets

## How to test
From the project root, run: 
`pytest`