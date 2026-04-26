import sqlite3
from datetime import datetime

DB_NAME = "manager.db"


# -------------------------------
# Utility Functions
# -------------------------------

def get_date():
    """Get a valid date input from user"""
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        
        if date_input == "":
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")


def get_text(prompt):
    """Ensure non-empty text input"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


# -------------------------------
# Database Setup
# -------------------------------

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def setup_database():
    """Create tables and default data"""

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cat_name TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS manager (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT NOT NULL,
        deadline TEXT,
        category_id INTEGER,
        FOREIGN KEY(category_id) REFERENCES category(id)
    )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO category (cat_name)
    VALUES ('general'), ('work'), ('personal')
    """)

    conn.commit()


# -------------------------------
# CRUD FUNCTIONS
# -------------------------------

def add_task():
    """Add a new task"""

    title = get_text("Enter title: ")

    status_input = input("Enter status (p = pending, c = complete): ").lower()
    status = "complete" if status_input == "c" else "pending"

    deadline = get_date()

    cursor.execute("SELECT id, cat_name FROM category")
    categories = cursor.fetchall()

    print("\n--- Available Categories ---")
    for cat_id, name in categories:
        print(f"{cat_id}. {name}")

    try:
        cat_choice = int(input("Select category ID: "))
    except ValueError:
        print("Invalid category. Defaulting to 'general'")
        cat_choice = 1

    try:
        cursor.execute("""
        INSERT INTO manager (title, status, deadline, category_id)
        VALUES (?, ?, ?, ?)
        """, (title, status, deadline, cat_choice))

        conn.commit()
        print("Task added successfully")

    except Exception as e:
        print("Error inserting task:", e)


def view_tasks():
    """Display all tasks"""

    query = """
    SELECT m.id, m.title, m.status, m.deadline, c.cat_name
    FROM manager m
    INNER JOIN category c ON m.category_id = c.id
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"\n{'ID':<4}|{'Title':<20}|{'Status':<10}|{'Deadline':<12}|Category")
    print("-" * 65)

    for row in rows:
        print(f"{row[0]:<4}|{row[1]:<20}|{row[2]:<10}|{row[3]:<12}|{row[4]}")


def update_task():
    """Mark task as complete"""

    try:
        task_id = int(input("Enter task ID to mark complete: "))
        cursor.execute("UPDATE manager SET status = 'complete' WHERE id = ?", (task_id,))

        if cursor.rowcount == 0:
            print("No task found.")
        else:
            conn.commit()
            print("Task updated successfully")

    except ValueError:
        print("Invalid ID")


def delete_task():
    """Delete a task"""

    try:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM manager WHERE id = ?", (task_id,))
        conn.commit()
        print("Task deleted successfully")

    except ValueError:
        print("Invalid ID")


def edit_task():
    """Edit task details"""

    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("Invalid ID")
        return

    print("\n1. Title\n2. Status\n3. Deadline\n4. All")
    choice = input("Choose option (1-4): ")

    if choice == "1":
        new_title = get_text("New title: ")
        cursor.execute("UPDATE manager SET title = ? WHERE id = ?", (new_title, task_id))

    elif choice == "2":
        cursor.execute("SELECT status FROM manager WHERE id = ?", (task_id,))
        result = cursor.fetchone()

        if result:
            new_status = "complete" if result[0] == "pending" else "pending"
            cursor.execute("UPDATE manager SET status = ? WHERE id = ?", (new_status, task_id))
            print(f"Status updated to {new_status}")
        else:
            print("Task not found")

    elif choice == "3":
        new_deadline = get_date()
        cursor.execute("UPDATE manager SET deadline = ? WHERE id = ?", (new_deadline, task_id))

    elif choice == "4":
        new_title = get_text("New title: ")
        new_deadline = get_date()

        status_input = input("New status (p/c): ").lower()
        new_status = "complete" if status_input == "c" else "pending"

        cursor.execute("""
        UPDATE manager
        SET title = ?, status = ?, deadline = ?
        WHERE id = ?
        """, (new_title, new_status, new_deadline, task_id))

    else:
        print("Invalid option")
        return

    conn.commit()
    print("Task updated successfully")


def count_tasks():
    """Display dashboard stats"""

    cursor.execute("SELECT COUNT(*) FROM manager")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM manager WHERE status = 'pending'")
    pending = cursor.fetchone()[0]

    print("\n--- DASHBOARD ---")
    print(f"Total tasks: {total}")
    print(f"Pending: {pending}")
    print(f"Completed: {total - pending}")
    print("------------------\n")


def filter_by_title():
    """Search tasks by title"""

    keyword = input("Enter keyword: ")

    cursor.execute("SELECT * FROM manager WHERE title LIKE ?", (f"%{keyword}%",))
    results = cursor.fetchall()

    if not results:
        print("No results found")
        return

    print(f"{'ID':<4}|{'Title':<20}|{'Status':<10}|Deadline")
    print("-" * 50)

    for row in results:
        print(f"{row[0]:<4}|{row[1]:<20}|{row[2]:<10}|{row[3]}")


def close_db():
    """Close database connection"""
    conn.close()
    print("Database closed")


# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":
    setup_database()
    print("Database ready.")