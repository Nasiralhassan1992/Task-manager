# 📋 Task Manager CLI App (Python + SQLite)

A simple and powerful **command-line task manager** built with Python and SQLite.
This project allows users to manage daily tasks efficiently using a clean and interactive CLI interface.

---

## 🚀 Features

* ✅ Add new tasks
* ✅ View all tasks
* ✅ Mark tasks as complete
* ✅ Edit existing tasks
* ✅ Delete tasks (with confirmation)
* ✅ Search tasks by title
* ✅ Dashboard showing:

  * Total tasks
  * Pending tasks
  * Completed tasks
* ✅ Category support (General, Work, Personal)
* ✅ Clean and user-friendly CLI interface

---

## 🛠️ Technologies Used

* **Python 3**
* **SQLite3 (built-in database)**
* **OS module (for screen handling)**

---

## 📂 Project Structure

```
task_manager_app/
│
├── main.py              # CLI interface (user interaction)
├── task_manager.py      # Database + logic (CRUD operations)
├── manager.db           # SQLite database file (auto-created)
└── README.md            # Project documentation
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/Nasiralhassan1992/task-manager-cli.git
cd task-manager-cli
```

### 2. Run the application

```
python main.py
```

---

## 🧠 How It Works

* The app uses **SQLite** to store tasks locally.
* Tasks are linked to categories using a **foreign key relationship**.
* The CLI provides a menu-driven interface for interaction.
* Each action (add, edit, delete, etc.) updates the database instantly.

---

## 📸 Sample Menu

```
===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Edit Task
6. Dashboard
7. Search by Title
8. Exit
```

---

## 🔒 Safety Features

* Confirmation prompts before deleting tasks
* Input validation to prevent errors
* Default values for invalid inputs

---

## 📈 Future Improvements

* 🔹 Priority system (Low / Medium / High)
* 🔹 Due date reminders
* 🔹 User authentication (multi-user system)
* 🔹 GUI version (Tkinter or Mobile App)
* 🔹 Web version using Flask

---

## 🙌 Author

**Nasir Alhassan**
Computer Science Graduate | Python Developer

---

## ⭐ Support

If you find this project helpful:

* Star ⭐ the repository
* Share with others
* Contribute improvements

---

## 📜 License

This project is open-source and free to use for learning purpose 
