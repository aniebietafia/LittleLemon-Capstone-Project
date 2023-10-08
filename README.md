# Little Lemon Capstone Project

## Introduction

This is a capstone project for the Backend Engineering on Coursera. The goal of this project is to develop a RESTful API for LittleLemon Restaurant. The API will be used to manage the restaurant's menu and orders. The API will be developed using Python and Django Rest Framework.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.0 or higher
- Django Rest Framework 3.11 or higher
- MySQL 12.1 or higher

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aniebietafia/LittleLemon-Capstone-Project.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Create a database in MySQL
   ```sh
   CREATE DATABASE littlelemon;
   ```
4. Create a .env file in the root directory and add the following environment variables

   ```sh

   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=littlelemon
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=yout_db_host
   DB_PORT=your_db_port
   ```

5. Run migrations
   ```sh
   python manage.py migrate
   ```
6. Run the server
   ```sh
   python manage.py runserver
   ```
7. Run tests
   ```sh
   python manage.py test
   ```

## API Reference

### Endpoints

#### Menu

| Method | Endpoint        | Description              |
| ------ | --------------- | ------------------------ |
| GET    | /api/menu/      | Get all menu items       |
| POST   | /api/menu/      | Create a new menu item   |
| GET    | /api/menu/{id}/ | Get a menu item by id    |
| PUT    | /api/menu/{id}/ | Update a menu item by id |
| DELETE | /api/menu/{id}/ | Delete a menu item by id |

#### Booking

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | /api/booking/      | Get all bookings     |
| POST   | /api/booking/      | Create a new booking |
| GET    | /api/booking/{id}/ | Get a booking by id  |
