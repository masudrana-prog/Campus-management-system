# 🎓 CampusHub — Django Campus Management System

A full-featured, role-based campus management system built with **Django** and **Tailwind CSS**, featuring a **3D Modern glassmorphism UI**.

---

## 📸 Features Overview

### 🔐 Authentication & Role-Based Access
| Feature | Admin | Teacher | Student | Alumni |
|---|---|---|---|---|
| Dashboard | ✅ Full Stats | ✅ Course Mgmt | ✅ Deadline Tracker | ✅ Events & Network |
| Library | ✅ Manage | ✅ Borrow | ✅ Borrow | ❌ Restricted |
| Assignments | ✅ All | ✅ Upload & Grade | ✅ Submit | ❌ Restricted |
| Courses | ✅ All | ✅ My Courses | ✅ Enrolled | ❌ Restricted |
| Previous Questions | ✅ All | ✅ Upload | ✅ Download | ❌ Restricted |
| Canteen | ✅ Manage | ✅ Order | ✅ Order | ✅ Order |
| Events | ✅ Manage | ✅ Register | ✅ Register | ✅ Register |
| Lost & Found | ✅ All | ✅ Report/Claim | ✅ Report/Claim | ✅ Report/Claim |
| News Feed | ✅ Approve | ✅ Post | ✅ Post | ✅ Post |
| Alumni Network | ✅ All | — | — | ✅ Connect |

---

## 🏗️ System Architecture

```
campus_management/
├── users/              # Auth, Profiles (Student / Teacher / Alumni / Admin)
├── academic/           # Courses, Assignments, Previous Questions, Routine
├── library/            # Books, Borrow System, Return Deadlines
├── social/             # Posts, Comments, Likes (News Feed)
├── campus/             # Canteen, Events, Lost & Found, Classrooms
├── templates/          # Tailwind CSS glassmorphism UI
├── static/             # Static assets
├── media/              # Uploaded files (images, PDFs, etc.)
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone / Extract the project
```bash
cd campus_management
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note:** `Pillow` is required for all image/file fields (profile pictures, book covers, post images, etc.)

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed sample data (recommended)
```bash
python manage.py seed_data
```

This creates **4 test accounts** and populates the database with courses, books, assignments, events, canteen items, and posts.

### 6. Run the development server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## 🔑 Test Accounts

| Role | Email | Password |
|---|---|---|
| 👑 Admin | admin@campus.edu | admin123 |
| 🧑‍🏫 Teacher | teacher@campus.edu | teacher123 |
| 🎓 Student | student@campus.edu | student123 |
| 🤝 Alumni | alumni@campus.edu | alumni123 |

---

## 📦 Dependencies

```
Django>=4.2,<5.0
Pillow>=10.0.0          # Image processing (REQUIRED)
django-crispy-forms>=2.0
crispy-tailwind>=0.5.0
```

---

## 🎨 UI Design System

- **Framework:** Tailwind CSS (CDN)
- **Style:** Glassmorphism + Soft 3D shadows
- **Font:** Sora (Google Fonts)
- **Icons:** Font Awesome 6
- **Theme:** Dark slate (`#0f172a`) with emerald accents
- **Cards:** Frosted glass effect (`backdrop-filter: blur`)

---

## 📱 App Breakdown

### `users` app
- `User` — Custom `AbstractUser` with `email` login, `role`, `phone`, `profile_picture`
- `StudentProfile` — `student_id`, `department`, `year`, `semester`
- `TeacherProfile` — `teacher_id`, `department`, `designation`
- `AlumniProfile` — `alumni_id`, `graduation_year`, `profession`, `company`
- Role-based dashboard with **Deadline Tracker** for students

### `academic` app
- `Department` — CSE, EEE, BBA, etc.
- `Course` — Teacher-assigned, student-enrolled
- `Assignment` — FileField, due dates, overdue detection
- `AssignmentSubmission` — Per-student, with grading support
- `PreviousQuestion` — PDF uploads, year-wise
- `Routine` — Day/time schedule by department & semester

### `library` app
- `Book` — `ImageField` cover, copy tracking (`total_copies` / `available_copies`)
- `BookIssue` — Borrow system with **14-day auto return deadline**, overdue detection
- Student & teacher dashboard shows return deadlines

### `social` app
- `Post` — `ImageField`, type tags (Notice / News / Question / General)
- `Comment` — Threaded comments per post
- `Like` — Toggle like with live AJAX counter

### `campus` app
- `Canteen` + `MenuItem` — Menu with image, price, availability
- `Order` + `OrderItem` — Full ordering system with status tracking
- `Event` — Registration, participant count, banner image
- `LostAndFound` — Report & claim items with images
- `Classroom` — Room management

---

## 🔧 Admin Panel

Access the Django Admin at: **http://127.0.0.1:8000/admin/**

Login with: `admin@campus.edu` / `admin123`

Admin can:
- Manage all users and assign roles
- Approve/reject posts
- Add/edit books, courses, departments
- Update canteen menus and manage orders
- Manage events and classrooms

---

## 🗂️ Media Files

All uploaded files are stored in the `media/` directory:

| Path | Contents |
|---|---|
| `media/profile_pics/` | User profile pictures |
| `media/assignments/` | Assignment attachments |
| `media/submissions/` | Student submission files |
| `media/previous_questions/` | Past exam papers |
| `media/book_covers/` | Library book covers |
| `media/post_images/` | News feed images |
| `media/event_banners/` | Event banner images |
| `media/menu_items/` | Canteen food images |
| `media/lost_found/` | Lost & found item photos |

---

## ⚙️ Configuration

Key settings in `campus_management/settings.py`:

```python
AUTH_USER_MODEL = 'users.User'      # Custom user model
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
TIME_ZONE = 'Asia/Dhaka'
MEDIA_ROOT = BASE_DIR / 'media'     # File uploads location
```

For **production**, update:
- `SECRET_KEY` — Use environment variable
- `DEBUG = False`
- `ALLOWED_HOSTS` — Set your domain
- Configure a proper database (PostgreSQL recommended)
- Set up static file serving (WhiteNoise or Nginx)

---

## 📋 URL Structure

| URL Pattern | View |
|---|---|
| `/` | Redirects to login |
| `/users/login/` | Login page |
| `/users/register/` | Registration |
| `/dashboard/` | Role-based dashboard |
| `/academic/courses/` | Course list |
| `/academic/assignments/` | Assignment tracker |
| `/academic/routine/` | Class schedule |
| `/academic/previous-questions/` | Past exam papers |
| `/library/` | Book search |
| `/library/my-books/` | Borrowed books + deadlines |
| `/social/` | News feed |
| `/campus/canteen/` | Canteen menu |
| `/campus/events/` | Event listings |
| `/campus/lost-found/` | Lost & Found |
| `/admin/` | Django admin panel |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📄 License

MIT License — free to use and modify.
