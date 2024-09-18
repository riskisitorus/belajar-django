# How to Run
1. Create `virtual environment`
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

4. Edit the `.env.example` file to `.env` and update the necessary environment variables with your own configurations.

5. Makemigration and migrate database
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```

6. Run Django server
```bash
py manage.py runserver
```

7. Enjoy!