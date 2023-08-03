# Prixite Task Assessment

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Installation](#installation)
- [API](#api)
- [Testing](#testing)
- [Code Style](#code-style)
- [License](#license)

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes. See [Installation](#installation) for notes on how to deploy the project on a live system.


## Features

List the key features of your Django project here.

- CRUD For User Model
- Test Cases for the APIs
- Flake8, Code Style Implementation


## Installation

Provide step-by-step instructions to install and set up the project.

1. Clone the repository: `git clone https://github.com/your-username/prixite_task_assessment.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Perform database migrations: `python manage.py migrate`
4. Create a superuser for the admin panel: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`


## API

### Endpoints

- `GET /api/users/`: Fetch a list of users.
- `GET /api/users/<id>/`: Fetch details of a specific user by their ID.
- `PUT /api/users/<id>/`: Update a specific user's information.
- `POST /api/users/`: Add a new user to the list.


## Testing

To run the test cases for your project, execute the following command:

`python manage.py test`

Ensure that all test cases pass successfully before making contributions or deploying the project.


## Code Style

We enforce code style and formatting using Flake8. Make sure your code follows the project's coding standards before submitting a pull request. To check for code style issues, run:

`flake8`

Fix any reported issues before committing your changes.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
