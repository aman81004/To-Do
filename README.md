# Django To-Do App

A simple Django to-do application with user signup, login, logout, and personal task management.

## Features

- User signup and login
- Duplicate username handling
- Add new tasks
- Edit existing tasks
- Delete tasks
- User-specific task list
- Logout support

## Project Structure

```text
To-Do/
+-- todo/
|   +-- manage.py
|   +-- db.sqlite3
|   +-- todo/
|       +-- models.py
|       +-- urls.py
|       +-- views.py
|       +-- templates/
|       +-- static/
+-- README.md
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Install Django:

```powershell
pip install django
```

Apply database migrations:

```powershell
python .\todo\manage.py migrate
```

Run the development server:

```powershell
python .\todo\manage.py runserver
```

Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Main URLs

- `/signup/` - Create a new account
- `/login/` - Login
- `/todopage/` - View and add tasks
- `/edit_todo/<srno>/` - Edit a task
- `/delete_todo/<srno>/` - Delete a task
- `/signout/` - Logout

## Development Checks

Run Django's project check:

```powershell
python .\todo\manage.py check
```

Check for missing migrations:

```powershell
python .\todo\manage.py makemigrations --check --dry-run
```
