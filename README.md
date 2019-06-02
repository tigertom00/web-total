# Project Title

Website with "Timeliste Registration"

## Getting Started

To run on local django server (port: 8000):

### Prerequisites

What things you need to install the software and how to install them

You need git and python3 installed.

### Installing

Make a new project folder then install virtualenv and activate it:
(windows:)

```
mkdir myproject
cd myproject
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

Clone repo and install packages:

```
git clone https://github.com/tigertom00/web-total.git
cd web-total
pip install -r requirements.txt
```

Open manage.py in a editor and change setting file from prod to dev:

```
...
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srv.settings.prod')
...
```

Change to:

```
...
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srv.settings.dev')
...
```

Migrate database and runserver:

```
python manage.py makemigrations users members testing timelister matriell jobb
python manage.py migrate
python manage.py runserver
```

## Deployment

## Built With

## Authors

- **Tomas Hoff**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
