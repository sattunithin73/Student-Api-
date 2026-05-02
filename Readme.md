# 🎓 Student Management API (Django REST Framework)

A simple REST API built using Django and Django REST Framework to manage student data.
This project supports full CRUD operations and is designed for learning backend development.

---

## 🚀 Features

* Add new student records
* View all students
* Retrieve a single student by ID
* Update student details
* Delete student records
* RESTful API design

---

## 🛠️ Tech Stack

* Python 3
* Django
* Django REST Framework
* SQLite (default database)

---

## 📁 Project Structure

```
SMS/
│
├── manage.py
├── db.sqlite3
├── sms/                  # Main project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── student/              # Student app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash
python manage.py migrate
```

---

### 5. Run server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## 📌 API Endpoints

| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| GET    | /students/        | Get all students   |
| POST   | /students/        | Create a student   |
| GET    | /students/\<id\>/ | Get single student |
| PUT    | /students/\<id\>/ | Update student     |
| DELETE | /students/\<id\>/ | Delete student     |

---

## 🧾 Sample Request Body

```json
{
  "name": "Nithin",
  "roll": 22,
  "course": "python"
}
```

---

## 📬 Testing the API

You can test the API using:

* Postman
* Thunder Client (VS Code)
* Browser (for GET requests)

---

## 💡 Future Improvements

* Add authentication (JWT)
* Add pagination
* Add search & filtering
* Deploy on Render / AWS

---

## 👨‍💻 Author

**Nithin S**

---

## 📄 License

This project is created for learning and practice purposes.
