
## 🔧 PROJECT FOLDER STRUCTURE

### 📁 Root Folder (e.g., `school_mis`)

```
school_mis/
├── backend/          ← Django backend
│   ├── core/
│   ├── school_backend/
│   └── manage.py
│
├── frontend/         ← React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/      ← Navbar, Sidebar, etc.
│   │   ├── pages/           ← Page components by role
│   │   │   ├── admin/
│   │   │   ├── teacher/
│   │   │   ├── student/
│   │   │   └── shared/
│   │   ├── utils/           ← Axios, auth helpers
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
```

---

## 🗂️ REACT FOLDER DETAIL (Frontend)

### ✅ `src/pages/admin/`

* `Dashboard.js`: Admin home page
* `ManageUsers.js`: View/add/edit/remove teachers & students
* `Reports.js`: View school-wide reports (attendance, performance, etc.)

### ✅ `src/pages/teacher/`

* `Dashboard.js`: Teacher home
* `MyStudents.js`: List of assigned students
* `SubmitGrades.js`: Form to enter grades

### ✅ `src/pages/student/`

* `Dashboard.js`: Student home
* `MyProfile.js`: View/update personal info
* `MyGrades.js`: View grades and attendance

### ✅ `src/pages/shared/`

* `Login.js`: Login form
* `Register.js`: Registration form (if public)
* `NotFound.js`: 404 error page
* `Unauthorized.js`: If user tries to access another role’s page

---

### ✅ `src/components/`

* `Navbar.js`: Dynamic navbar based on user role
* `Sidebar.js`: Optional, role-based
* `ProtectedRoute.js`: Restrict access based on login and role
* `RoleRedirect.js`: Auto-redirect user to correct dashboard

---

### ✅ `src/utils/`

* `axiosConfig.js`: Axios instance with JWT token
* `auth.js`: Helpers to decode JWT & get user role
* `PrivateRoutes.js`: Wrapper for authenticated routes

---

## 🔙 DJANGO BACKEND OVERVIEW

### ✅ Apps:

* `core`: Main logic (students, grades, roles)
* `users` (optional): Separate app if you want more control over auth

### ✅ Useful Django Models:

* `User` (extend with role field: Admin, Teacher, Student)
* `StudentProfile`: Linked to User (for DOB, class, etc.)
* `TeacherProfile`: Linked to User (subject, class, etc.)
* `Subject`
* `Grade`
* `Attendance`

---

## 🌐 PAGE CONTENT IDEAS (BY ROLE)

### 🔐 **Login/Register**

* Fields: username, password, email, role (optional)
* On login → JWT token → store in localStorage
* Redirect to `/admin/dashboard`, `/student/dashboard`, etc.

---

### 👤 **Admin Dashboard**

* Cards:

  * Total Students
  * Total Teachers
  * Classes
* Buttons:

  * Add Teacher
  * View All Students
* Links to:

  * `ManageUsers`
  * `Reports`

---

### 👨‍🏫 **Teacher Dashboard**

* Welcome message
* Link to:

  * `MyStudents`
  * `SubmitGrades`

---

### 🎓 **Student Dashboard**

* Welcome message
* Link to:

  * `MyProfile`
  * `MyGrades`

---

## 🚦 Navigation Access Control

Use `ProtectedRoute.js` to ensure:

* Only logged-in users can access dashboard
* Only Admins can access admin routes
* Only Teachers can access teacher routes
* Only Students can access student routes

