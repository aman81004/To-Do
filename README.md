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

## Deploy to Vercel

Use the `todo/` folder as the Vercel project root because it contains `manage.py`.

Before deploying, create a Postgres database in Vercel Storage, Neon, Supabase, or another provider. SQLite is fine for local development, but it should not be used for production on Vercel because serverless file storage is not persistent.

Add these environment variables in Vercel:

```text
DJANGO_SECRET_KEY=<generated-secret-key>
DJANGO_DEBUG=False
DATABASE_URL=<postgres-connection-url>
```

If you use Vercel Postgres, its `POSTGRES_URL` variable is also supported automatically.

Generate a Django secret key locally:

```powershell
cd .\todo
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then import the GitHub repository in Vercel and set:

```text
Root Directory: todo
```

Vercel will install `requirements.txt`, run the build script in `pyproject.toml`, apply migrations, collect static files, and serve the Django WSGI app.

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
