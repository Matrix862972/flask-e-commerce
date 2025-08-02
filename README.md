# Flask E-Commerce

A simple e-commerce web application built with Flask, SQLAlchemy, and Bootstrap. This project is designed as a learning resource for building web applications with user authentication, item management, and a basic marketplace.

## Features

- User registration and login (with password hashing)
- User authentication and session management (Flask-Login)
- Marketplace for buying and selling items
- Item ownership and budget management
- Flash messages for user feedback
- Bootstrap 4 for responsive UI
- SQLite database for data persistence

## Project Structure

```
FlaskMarket/
│
├── market/
│   ├── __init__.py         # App and database initialization
│   ├── models.py           # SQLAlchemy models (User, Item)
│   ├── forms.py            # WTForms for registration, login, purchase, sell
│   ├── route.py            # Flask routes (views)
│   ├── market.db           # SQLite database file
│   ├── static/
│   │   └── images/         # Static images (e.g., duck.png)
│   └── templates/
│       ├── base.html       # Base template
│       ├── home.html       # Home page
│       ├── market.html     # Marketplace page
│       ├── register.html   # Registration page
│       ├── login.html      # Login page
│       └── includes/       # Modal and partial templates
│
├── utilities/
│   └── db_shell.py         # Helper script for DB shell in app context
│
└── run.py                  # Entry point to run the Flask app
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Matrix862972/flask-e-commerce.git
   cd flask-e-commerce/FlaskMarket
   ```
2. **Create a virtual environment (recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   _(If `requirements.txt` is missing, install manually:)_
   ```sh
   pip install flask flask_sqlalchemy flask_login flask_wtf wtforms
   ```

### Running the App

1. **Set environment variables (optional for development):**
   ```sh
   set FLASK_APP=run.py
   set FLASK_ENV=development
   ```
2. **Run the app:**
   ```sh
   python run.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

### Database Management

- The SQLite database is located at `market/market.db`.
- To interact with the database in the Flask app context, use the helper script:
  ```sh
  python utilities/db_shell.py
  ```

## Usage

- Register a new user account.
- Log in to access the marketplace.
- Buy items if you have enough budget.
- Sell items you own to increase your budget.
- All actions provide feedback via flash messages.

## Customization

- Add new items by modifying the database or extending the admin interface.
- Update UI by editing templates in `market/templates/` and static files in `market/static/`.
- Extend user or item models in `market/models.py`.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is for educational purposes. See the LICENSE file for more information if provided.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [WTForms](https://wtforms.readthedocs.io/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
