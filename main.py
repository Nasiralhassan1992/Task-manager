import os
import task_manager as db


# =================================
# HELPERS
# =================================

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Pause execution so user can read output"""
    input("\nPress Enter to continue...")


def confirm_action(message):
    """Ask user for confirmation"""
    return input(f"{message} (y/n): ").strip().lower() == "y"


def show_menu():
    """Display menu options"""
    print("===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Dashboard")
    print("7. Search by Title")
    print("8. Exit")


# =================================
# MAIN APP
# =================================

def main():
    db.setup_database()

    while True:
        clear_screen()

        # Auto dashboard display
        db.count_tasks()

        show_menu()
        choice = input("\nChoose an option (1-8): ").strip()

        if choice == "1":
            clear_screen()
            db.add_task()
            pause()

        elif choice == "2":
            clear_screen()
            db.view_tasks()
            pause()

        elif choice == "3":
            if confirm_action("Mark task as complete?"):
                clear_screen()
                db.update_task()
            else:
                print("Action cancelled.")
            pause()

        elif choice == "4":
            if confirm_action("Are you sure you want to delete this task?"):
                clear_screen()
                db.delete_task()
            else:
                print("Delete cancelled.")
            pause()

        elif choice == "5":
            clear_screen()
            db.edit_task()
            pause()

        elif choice == "6":
            clear_screen()
            db.count_tasks()
            pause()

        elif choice == "7":
            clear_screen()
            db.filter_by_title()
            pause()

        elif choice == "8":
            if confirm_action("Exit application?"):
                db.close_db()
                print("Goodbye 👋")
                break

        else:
            print("Invalid option. Please select 1-8.")
            pause()


if __name__ == "__main__":
    main()		