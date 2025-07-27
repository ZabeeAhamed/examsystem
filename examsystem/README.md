# 📝 Online Exam System – Django Application

A **robust**, **secure**, and **user-friendly** Django-based online exam platform with powerful features for admins and students.

---

## 🚀 Features

### 🔐 User Authentication
- Secure **user registration**, **login**, and **logout**.
- Clean session management and CSRF protection.

### 👥 Role Handling
- **Admin**: Manage system via Django admin panel.
- **Students**: Interact through a custom frontend interface.

---

## 🛠️ Exam Management (Admin)
- Full **CRUD** for:
  - Exams
  - Questions
  - Options
- **Inline editing**: 
  - Add questions directly to exams.
  - Add options to questions.
  - Enforce **exactly one correct option** per question.

---
## 🎓 Student Experience
- Start exam with a **“Start”** button.
- One-question-at-a-time flow:  
  `(/exams/<slug>/question/<number>/)`
- **Timer** with auto-submit after duration ends.
- **Cheating prevention**:
  - Tab switch detection.
  - 3 warnings before auto-submit.

---
## 📊 Exam Results & History
- Instant score + breakdown after submission.
- View full result:
  - Question
  - Selected answer
  - Correct status
- No **retake** allowed after submission.
- Dedicated **Student Exam History** page showing:
  - Past attempts
  - Dates
  - Scores

---
## 📈 Admin Insights
- List and filter all exam attempts.
- View individual results.
- Export submissions and results via Django admin.

---
