# Registration/Login Project

Whatbytes is a modern web application built with Django and TailwindCSS, designed for seamless scalability, styling, and deployment. It integrates advanced user authentication and a deployment pipeline using Docker and GitHub Actions.

## Features
- **User Authentication**:
  - Login
  - Register with OTP verification
  - Forgot Password with secure email reset
  - Profile Management
  - Logout
- **Styling**: Fully integrated with TailwindCSS for responsive, modern UI.
- **Email Integration**: Powered by `django-anymail` for transactional emails.
- **Deployment**:
  - Containerized using Docker.
  - Automated CI/CD with GitHub Actions for testing and deployment.
- **Production-ready**: Served using Gunicorn and static files handled by WhiteNoise.

## Requirements
- Python 3.9 or higher
- Node.js 18.x
- Docker (optional, for containerized deployment)
- Django 4.x
- SMTP server (for email functionality)

## Installation

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/Samuthe/whatbytes.git
   cd whatbytes
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Node.js dependencies:
   ```bash
   cd frontend/static_src
   yarn install
   cd ../..
   ```

5. Set up environment variables:
   - Create a `.env` file in the root directory and configure it with the necessary secrets (e.g., email settings for `django-anymail`).
     ```env
     SECRET_KEY=<your-secret-key>
     EMAIL_HOST=<your-email-host>
     EMAIL_PORT=<your-email-port>
     EMAIL_HOST_USER=<your-email>
     EMAIL_HOST_PASSWORD=<your-email-password>
     EMAIL_USE_TLS=True
     ```

6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

7. Build TailwindCSS assets:
   ```bash
   python manage.py tailwind build
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t whatbytes .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 whatbytes
   ```

### GitHub Actions CI/CD
The project includes a GitHub Actions workflow for:
- Running tests on every push.
- Building and deploying the Docker container.

Ensure you configure the required secrets (e.g., Docker Hub credentials) in your GitHub repository settings.

## Project Structure
- **`accounts/`**: Manages user authentication (login, register, OTP, etc.).
- **`frontend/`**: TailwindCSS configuration and frontend code.
- **`whatbytes_project/`**: Main Django project folder with settings and WSGI configuration.
- **`manage.py`**: Entry point for Django administrative tasks.
- **`.github/`**: Contains GitHub Actions workflows.
- **`Dockerfile`**: Configuration for containerizing the application.
- **`requirements.txt`**: Lists Python dependencies.

## Deployment
1. Build and deploy the project using Docker:
   ```bash
   docker-compose up --build
   ```

2. Use Gunicorn in production for efficient request handling:
   ```bash
   gunicorn --bind 0.0.0.0:8000 whatbytes_project.wsgi:application
   ```


