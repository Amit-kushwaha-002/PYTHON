# lets make a smart study planneer

import json
import os
from datetime import datetime

DATA_FILE = "study_data.json"


# -------------------------
# DATA HANDLING
# -------------------------

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {"subjects": [], "history": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------
# ADD SUBJECT
# -------------------------

def add_subject(data):
    print("\n--- Add New Subject ---")
    name = input("Subject Name: ")
    exam_date = input("Exam Date (YYYY-MM-DD): ")
    priority = int(input("Priority (1-5): "))

    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")
    days_left = (exam - today).days

    if days_left <= 0:
        print("⚠ Exam date must be in future.")
        return

    subject = {
        "name": name,
        "exam_date": exam_date,
        "days_left": days_left,
        "priority": priority,
        "completed_hours": 0
    }

    data["subjects"].append(subject)
    save_data(data)
    print("✅ Subject added successfully!")


# -------------------------
# GENERATE SMART PLAN
# -------------------------

def generate_plan(data):
    if not data["subjects"]:
        print("⚠ No subjects added.")
        return

    print("\n📅 SMART STUDY PLAN\n")

    for subject in data["subjects"]:
        daily_hours = round((subject["priority"] * 2) / (subject["days_left"] / 7), 2)
        print(f"{subject['name']}")
        print(f"  Days Left: {subject['days_left']}")
        print(f"  Suggested Study: {daily_hours} hrs/day\n")


# # -------------------------
# # MARK STUDY PROGRESS
# # -------------------------

# def log_study(data):
#     if not data["subjects"]:
#         print("⚠ No subjects available.")
#         return

#     print("\nSelect Subject:")
#     for i, subject in enumerate(data["subjects"]):
#         print(f"{i+1}. {subject['name']}")

#     choice = int(input("Choice: ")) - 1
#     hours = float(input("Hours Studied Today: "))

#     data["subjects"][choice]["completed_hours"] += hours
#     data["history"].append({
#         "subject": data["subjects"][choice]["name"],
#         "hours": hours,
#         "date": str(datetime.today().date())
#     })

#     save_data(data)
#     print("✅ Study logged!")


# # -------------------------
# # ANALYTICS
# # -------------------------

# def show_analytics(data):
#     print("\n📊 STUDY ANALYTICS\n")

#     total_hours = sum(s["completed_hours"] for s in data["subjects"])
#     print(f"Total Study Hours: {total_hours}")

#     for subject in data["subjects"]:
#         print(f"{subject['name']} → {subject['completed_hours']} hrs completed")


# # -------------------------
# # MAIN MENU
# # -------------------------

# def main():
#     data = load_data()

#     while True:
#         print("\n===== AI SMART STUDY PLANNER =====")
#         print("1. Add Subject")
#         print("2. Generate Study Plan")
#         print("3. Log Study Hours")
#         print("4. View Analytics")
#         print("5. Exit")

#         choice = input("Select option: ")

#         if choice == "1":
#             add_subject(data)
#         elif choice == "2":
#             generate_plan(data)
#         elif choice == "3":
#             log_study(data)
#         elif choice == "4":
#             show_analytics(data)
#         elif choice == "5":
#             print("👋 Goodbye!")
#             break
#         else:
#             print("Invalid choice!")


# if __name__ == "__main__":
#     main()
