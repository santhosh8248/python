import tkinter as tk
from tkinter import messagebox
from datetime import date

# ---------- DATA ----------
courses = {
    "Python Basics": ["Variables", "Data Types", "Operators"],
    "Python Loops": ["For Loop", "While Loop", "Break"],
    "Python Functions": ["Function", "Arguments", "Return"]
}

enrolled = []       # courses the student joined
completed = []      # lessons finished
attendance = []     # list of (name, date, status)


# ---------- COURSE FUNCTIONS ----------
def view_courses():
    course_list.delete(0, tk.END)
    for course in courses:
        course_list.insert(tk.END, course)


def enroll_course():
    selected = course_list.curselection()      # which item is clicked
    if not selected:
        messagebox.showwarning("LMS", "Select a course")
        return

    course = course_list.get(selected)
    if course in enrolled:
        messagebox.showinfo("LMS", "Already enrolled!")
    else:
        enrolled.append(course)
        messagebox.showinfo("LMS", "Course enrolled successfully!")


def view_lessons():
    selected = course_list.curselection()
    if not selected:
        messagebox.showwarning("LMS", "Select a course")
        return

    course = course_list.get(selected)
    lesson_list.delete(0, tk.END)
    for lesson in courses[course]:
        lesson_list.insert(tk.END, lesson)


def complete_lesson():
    selected = lesson_list.curselection()
    if not selected:
        messagebox.showwarning("LMS", "Select a lesson")
        return

    lesson = lesson_list.get(selected)
    if lesson in completed:
        messagebox.showinfo("LMS", "Already completed!")
    else:
        completed.append(lesson)
        messagebox.showinfo("LMS", "Lesson completed!")


def view_progress():
    total = sum(len(lessons) for lessons in courses.values())
    done = len(completed)
    percent = (done / total) * 100
    messagebox.showinfo("Progress", f"Completed: {done}/{total}\nProgress: {percent:.1f}%")


# ---------- ATTENDANCE FUNCTIONS ----------
def mark_attendance(status):
    name = name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Attendance", "Enter student name")
        return

    today = str(date.today())
    attendance.append((name, today, status))

    attendance_list.insert(tk.END, f"{name}  |  {today}  |  {status}")
    # colour the new row: green for Present, red for Absent
    last = attendance_list.size() - 1
    if status == "Present":
        attendance_list.itemconfig(last, bg="#c8f7c5")
    else:
        attendance_list.itemconfig(last, bg="#f7c5c5")

    name_entry.delete(0, tk.END)


def attendance_percent():
    name = name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Attendance", "Enter student name")
        return

    days = 0
    present = 0
    for student, day, status in attendance:
        if student.lower() == name.lower():
            days += 1
            if status == "Present":
                present += 1

    if days == 0:
        messagebox.showinfo("Attendance", "No record found")
    else:
        percent = (present / days) * 100
        messagebox.showinfo("Attendance",
                            f"{name}\nDays: {days}\nPresent: {present}\nAttendance: {percent:.1f}%")


# ---------- WINDOW ----------
root = tk.Tk()
root.title("Core Python LMS")
root.geometry("850x560")
root.configure(bg="#eef2ff")

# Header
tk.Label(root, text="CORE PYTHON LMS", font=("Arial", 22, "bold"),
         bg="#4f46e5", fg="white", pady=15).pack(fill="x")

# ---------- COURSES (left) ----------
course_frame = tk.Frame(root, bg="#dbeafe", padx=10, pady=10)
course_frame.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(course_frame, text="Courses", font=("Arial", 13, "bold"),
         bg="#dbeafe", fg="#1d4ed8").pack()
course_list = tk.Listbox(course_frame, height=6, width=25)
course_list.pack(pady=5)

tk.Button(course_frame, text="View Courses", bg="#8b5cf6", fg="white",
          command=view_courses).pack(pady=3, fill="x")
tk.Button(course_frame, text="Enroll Course", bg="#22c55e", fg="white",
          command=enroll_course).pack(pady=3, fill="x")
tk.Button(course_frame, text="View Lessons", bg="#f97316", fg="white",
          command=view_lessons).pack(pady=3, fill="x")

# ---------- LESSONS (middle) ----------
lesson_frame = tk.Frame(root, bg="#ffedd5", padx=10, pady=10)
lesson_frame.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(lesson_frame, text="Lessons", font=("Arial", 13, "bold"),
         bg="#ffedd5", fg="#c2410c").pack()
lesson_list = tk.Listbox(lesson_frame, height=6, width=25)
lesson_list.pack(pady=5)

tk.Button(lesson_frame, text="Complete Lesson", bg="#14b8a6", fg="white",
          command=complete_lesson).pack(pady=3, fill="x")
tk.Button(lesson_frame, text="View Progress", bg="#3b82f6", fg="white",
          command=view_progress).pack(pady=3, fill="x")

# ---------- ATTENDANCE (right) ----------
attendance_frame = tk.Frame(root, bg="#fce7f3", padx=10, pady=10)
attendance_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

tk.Label(attendance_frame, text="Student Attendance", font=("Arial", 13, "bold"),
         bg="#fce7f3", fg="#be185d").pack()

tk.Label(attendance_frame, text="Student Name:", bg="#fce7f3").pack()
name_entry = tk.Entry(attendance_frame, width=25)
name_entry.pack(pady=3)

tk.Button(attendance_frame, text="Present", bg="#22c55e", fg="white",
          command=lambda: mark_attendance("Present")).pack(pady=3, fill="x")
tk.Button(attendance_frame, text="Absent", bg="#ef4444", fg="white",
          command=lambda: mark_attendance("Absent")).pack(pady=3, fill="x")
tk.Button(attendance_frame, text="Attendance %", bg="#8b5cf6", fg="white",
          command=attendance_percent).pack(pady=3, fill="x")

attendance_list = tk.Listbox(attendance_frame, height=8, width=35)
attendance_list.pack(pady=5, fill="both", expand=True)

# Exit button
tk.Button(root, text="Exit", bg="#ef4444", fg="white", width=10,
          command=root.destroy).pack(side="bottom", pady=8)

view_courses()
root.mainloop()