This is the README file with instructions on how to set up and run the Flask application as a systemd service.

markdown
Copy code
# Flask QA Application

This application uses a pre-trained model from the Hugging Face Transformers library to answer questions based on a given context.

## Requirements

- Python 3.8+
- pip
- virtualenv

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/diwaharSmart/merzol-qa-bot.git
   cd your_repository
Create a virtual environment:


python3 -m venv venv
source venv/bin/activate
Install the dependencies:


pip install -r requirements.txt
Test the application locally:


python app.py
The application should be running at http://127.0.0.1:5000.

Deploying as a systemd Service
Create a systemd service file:

Replace placeholders in my_flask_app.service with your actual paths.
Copy the service file to /etc/systemd/system/:


sudo cp my_flask_app.service /etc/systemd/system/
Start and enable the service:


sudo systemctl start my_flask_app
sudo systemctl enable my_flask_app
Check the status of the service:


sudo systemctl status my_flask_app
The application should now be running at http://your_server_ip:5000.

Troubleshooting
To view logs:


sudo journalctl -u my_flask_app
To restart the service:

sudo systemctl restart my_flask_app
bash
Copy code

### 4. Deployment Steps

1. **Create the directories**:
   ```
   sudo mkdir -p /path/to/your/project
   cd /path/to/your/project
Copy your Flask app, my_flask_app.service, and requirements.txt to this directory.

Create a virtual environment and install dependencies:


python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Deploy with systemd:


sudo cp my_flask_app.service /etc/systemd/system/
sudo systemctl start my_flask_app
sudo systemctl enable my_flask_app
Check if the service is running:


sudo systemctl status my_flask_app
This setup will run your Flask application as a service on Ubuntu without needing Gunicorn.