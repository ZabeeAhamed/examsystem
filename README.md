# Examify 📝

**Examify** is a full-featured online examination platform designed for schools, colleges, coaching centers, and certification bodies. Built with Django and PostgreSQL, it offers secure, scalable, and real-time assessments with a modern and responsive user interface.

---

## 🚀 Overview

Examify transforms traditional assessments into a digital experience with features that ensure reliability, integrity, and ease of use. Whether you're managing hundreds of students or organizing small quizzes, Examify adapts to your needs.

---

## 🌟 Features

- 🔐 **Role-Based Access** – Admins manage exams/questions; students access only assigned exams.
- ⏱ **Real-Time Timer** – Exams auto-submit upon time completion.
- ❌ **Anti-Cheat Protection** – Disables tab-switching, copying, and refresh.
- 📊 **Instant Scoring** – Objective MCQs are auto-evaluated in real-time.
- 💾 **Auto-Save Mechanism** – Saves student answers periodically.
- 📱 **Responsive Design** – Works seamlessly across devices.
- 🧩 **Modular Exam Builder** – Add questions, options, durations, and marks flexibly.

---

## 🛠️ Tech Stack

| Layer     | Technology                |
|-----------|---------------------------|
| Backend   | Django 4.x, Python 3       |
| Frontend  | HTML, CSS, JavaScript      |
| Styling   | Bootstrap (with custom CSS)|
| Database  | PostgreSQL                 |
| Others    | Django ORM, Middleware     |

---

## 📂 Project Structure

examsystem/
├── exams/ # Core exam logic
├── users/ # Custom user roles and auth
├── templates/ # HTML templates
├── static/ # CSS, JS, custom styles
├── media/ # Uploaded files
├── examsystem/ # Project settings and URLs
├── manage.py
└── requirements.txt


---

## ⚙️ How It Works

1. **Admins** create exams with time, questions, and options.
2. **Students** log in securely and attend available exams.
3. During exam:
   - Timer counts down in real-time.
   - Navigation and copy-paste are blocked.
   - Auto-save captures answers every few seconds.
4. On submission or timeout:
   - Answers are auto-evaluated.
   - Results are shown instantly to students.
5. **Post-exam analytics** (planned): Admins can view detailed performance reports.

---

## 🖥️ Getting Started

1. **Clone the repo:**
   git clone https://github.com/ZabeeAhamed/examsystem.git
   cd examsystem
2. Install dependencies:
   pip install -r requirements.txt
3. Configure PostgreSQL:

Create a database and user

Update credentials in settings.py

4.Run migrations and start server:

python manage.py migrate
python manage.py runserver

5.Open browser:

Visit http://127.0.0.1:8000 to start using Examify.

---
🚧 Future Improvements
---
📈 Analytics Dashboard with charts

✍️ Subjective question evaluation

📱 Progressive Web App (PWA) support

🧪 Exam history and certificate PDF generation

🔌 RESTful APIs for mobile/third-party integration

🐳 Docker and CI/CD pipeline integration

---
🤝 Contributions
---
Contributions are welcome!
Feel free to fork, raise issues, or submit pull requests.
