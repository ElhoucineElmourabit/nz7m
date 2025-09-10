# nz7m


##  Setup Instructions

This project requires **Python 3.11**

---

### 1. Create a virtual environment
```bash
py -3.11 -m venv venv
````

### 2. Activate the virtual environment

```bash
.\venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the same directory level as `.env.example` and add your credentials:

```env
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_BUCKET=
```

---

### 5. Navigate to the Django project

```bash
cd customer_project
```

---

### 6. Run the development server

```bash
python manage.py runserver
```


### 7. Open your browser and go to:

* [http://127.0.0.1:8000/customer](http://127.0.0.1:8000/customer)
