# How to Run
1. Create virtual environment
```bash
py -m venv env
```

2. Activate `env`
```bash
env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Makemigration and migrate database
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```

5. Run Django server
```bash
py manage.py runserver
```