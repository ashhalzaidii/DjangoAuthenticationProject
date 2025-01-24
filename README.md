# Django Authentication Project

This project is a Django-based web application that implements a user authentication system with the following features:

- User Sign Up
- User Sign In
- Password Reset via Email
- Authentication-protected Home Page

## Features

1. **User Sign Up**:
   - Allows new users to register for an account.
   - Validates user input and ensures email uniqueness.

2. **User Sign In**:
   - Allows registered users to log in using their credentials.
   - Implements session-based authentication.

3. **Password Reset**:
   - Users can request a password reset link by providing their registered email address.
   - A password reset link is sent to the user's email if the email exists in the database.

4. **Authentication-protected Home Page**:
   - Only logged-in users can access the home page.
   - Non-authenticated users are redirected to the login page.

## Technologies Used

- **Django**: High-level Python web framework.
- **SQLite**: Default Django database for local development.
- **HTML/CSS**: Front-end templates.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Sign Up**:
   - Visit the Sign Up page to create a new account.

2. **Sign In**:
   - Log in using your registered email and password.

3. **Password Reset**:
   - Use the "Forgot Password" link on the login page.
   - Enter your registered email to receive a password reset link.

4. **Access Home Page**:
   - Log in to access the home page.
   - Non-authenticated users will be redirected to the login page.

## Configuration

- **Email Settings**:
  Update the `EMAIL_BACKEND` and related settings in the `settings.py` file to configure email functionality. For example, using Gmail:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = 'your-email@gmail.com'
  EMAIL_HOST_PASSWORD = 'your-email-password'
  ```

- **Database**:
  By default, the project uses SQLite. To switch to another database, update the `DATABASES` setting in `settings.py`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact:
- **Name**: Ashhal Zaidi
- **Email**: ashhalzzaidi@gmail.com
- **GitHub**: ashhalzaidii(https://github.com/ashhalzaidii/)

