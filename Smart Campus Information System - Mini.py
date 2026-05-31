# Smart Campus Information System - Mini Project Integration
# Lab 9: Complete Integration of Modules 1-8

import os
try:
    import numpy as np
except Exception:
    np = None
try:
    import pandas as pd
except Exception:
    pd = None
try:
    try:
        import matplotlib.pyplot as plt
    except Exception:
        plt = None
except Exception:
    plt = None    

# ==================== Module 1: Student Registration and Grade Evaluation ====================
def module1_grade_evaluation():
    print("\n--- Module 1: Student Registration and Grade Evaluation ---")
    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))
    
    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"
    
    print("\n--- Student Report ---")
    print(f"Name: {student_name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Performance Remark: {remark}")

# ==================== Module 2: Course Enrollment Management ====================
def module2_course_enrollment():
    print("\n--- Module 2: Course Enrollment Management ---")
    courses = []
    max_courses = 5
    
    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break
        
        course_name = input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == "done":
            break
        
        credits = input("Enter credit value: ")
        
        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue
        
        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue
        
        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.\n")
    
    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")
    print(f"Total courses enrolled: {len(courses)}")

# ==================== Module 3: Student Record Management ====================
students_master = []

def module3_student_records():
    print("\n--- Module 3: Student Record Management ---")
    
    # Sample data
    students_master.clear()
    students_master.append({"name": "Priya", "age": 20, "grades": [85, 90, 78]})
    students_master.append({"name": "Rahul", "age": 21, "grades": [72, 88, 91]})
    students_master.append({"name": "Anita", "age": 19, "grades": [95, 89, 92]})
    
    print("=== Student Records ===")
    for student in students_master:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")
        print("-" * 20)
    
    # Event Participation Analysis
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    print("\n=== Event Participation Analysis ===")
    print(f"Common Participants: {event_A & event_B}")
    print(f"All Participants: {event_A | event_B}")
    print(f"Only Event A Participants: {event_A - event_B}")

# ==================== Module 4: Sorting and Searching ====================
def module4_sorting_searching():
    print("\n--- Module 4: Sorting and Searching of Student IDs ---")
    student_ids = [105, 102, 110, 108, 101, 115]
    print(f"Original IDs: {student_ids}")
    
    # Bubble Sort
    sorted_ids = student_ids.copy()
    n = len(sorted_ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_ids[j] > sorted_ids[j + 1]:
                sorted_ids[j], sorted_ids[j + 1] = sorted_ids[j + 1], sorted_ids[j]
    print(f"Sorted IDs (Bubble Sort): {sorted_ids}")
    
    # Linear Search
    target = int(input("Enter Student ID to search: "))
    found_index = -1
    for i in range(len(sorted_ids)):
        if sorted_ids[i] == target:
            found_index = i
            break
    
    if found_index != -1:
        print(f"Linear Search: ID {target} found at index {found_index}")
        
        # Binary Search
        low, high = 0, len(sorted_ids) - 1
        found_index = -1
        while low <= high:
            mid = (low + high) // 2
            if sorted_ids[mid] == target:
                found_index = mid
                break
            elif sorted_ids[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print(f"Binary Search: ID {target} found at index {found_index}")
    else:
        print(f"ID {target} not found")

# ==================== Module 5: Fee Calculation ====================
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

def module5_fee_calculation():
    print("\n--- Module 5: Student Fee Calculation ---")
    tuition = 50000
    
    print(f"Tuition Fee: {tuition}")
    print(f"Total Fee (Tuition only): {calculate_fee(tuition)}")
    
    hostel = 30000
    print(f"Total Fee (Tuition + Hostel): {calculate_fee(tuition, hostel_fee=hostel)}")
    
    transport = 10000
    print(f"Total Fee (Tuition + Hostel + Transport): {calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)}")

# ==================== Module 6: File Handling ====================
def module6_file_handling():
    print("\n--- Module 6: File Handling for Academic Records ---")
    
    # Write to file
    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print("Student records written to file successfully.")
    
    # Read from file
    print("\nReading stored records:")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())
    
    # Generate report
    print("\nGenerating Report:")
    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""
    
    for record in records[1:]:
        parts = record.strip().split(",")
        name = parts[1]
        marks = int(parts[2])
        total_students += 1
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = name
    
    average_marks = total_marks / total_students
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Top Student: {top_student} with {highest_marks} marks")

# ==================== Module 7: Directory Scanning ====================
class MissingFileOrFolderError(Exception):
    pass

def module7_directory_scan():
    print("\n--- Module 7: Directory Scanning with Exception Handling ---")
    path = input("Enter directory path to scan: ")
    
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")
        
        print(f"\nScanning directory: {path}\n")
        empty_folders = []
        
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(f"{sub_indent}{f}")
            
            if not files and not dirs:
                empty_folders.append(root)
        
        if empty_folders:
            for folder in empty_folders:
                raise MissingFileOrFolderError(f"Empty folder detected: {folder}")
        else:
            print("\nDirectory scan completed successfully.")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# ==================== Module 8: Performance Analytics ====================
def module8_performance_analytics():
    print("\n--- Module 8: Student Performance Analytics ---")
    
    # Create sample CSV if not exists
    if not os.path.exists("student_performance.csv"):
        sample_data = pd.DataFrame({
            "Name": ["Priya", "Rahul", "Anita", "Kiran", "Sneha"],
            "Math": [85, 72, 95, 78, 88],
            "Science": [90, 88, 89, 82, 91],
            "English": [78, 91, 92, 85, 87]
        })
        sample_data.to_csv("student_performance.csv", index=False)
        print("Sample CSV file created: student_performance.csv")
    
    try:
        df = pd.read_csv("student_performance.csv")
        print("\n--- Raw Data ---")
        print(df.head())
        
        print("\n--- Statistical Summary ---")
        print(df.describe())
        
        scores = df[["Math", "Science", "English"]].to_numpy()
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)
        
        print("\n--- NumPy Analysis ---")
        print(f"Mean Scores (Math, Science, English): {mean_scores}")
        print(f"Median Scores (Math, Science, English): {median_scores}")
        print(f"Standard Deviation: {std_dev_scores}")
        
        print("\n--- Top Performers ---")
        print(f"Math: {df.loc[df['Math'].idxmax(), 'Name']}")
        print(f"Science: {df.loc[df['Science'].idxmax(), 'Name']}")
        print(f"English: {df.loc[df['English'].idxmax(), 'Name']}")
        
        # Visualizations
        subjects = ["Math", "Science", "English"]
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.ylabel("Average Score")
        
        plt.subplot(1, 2, 2)
        df.plot(x="Name", y=["Math", "Science", "English"], kind="bar", ax=plt.gca())
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# ==================== Main Dashboard ====================
def main_dashboard():
    while True:
        print("\n" + "=" * 50)
        print("    SMART CAMPUS INFORMATION SYSTEM")
        print("=" * 50)
        print("1. Student Registration & Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Record Management")
        print("4. Sorting and Searching Student IDs")
        print("5. Student Fee Calculation")
        print("6. File Handling for Academic Records")
        print("7. Directory Scanning with Exception Handling")
        print("8. Student Performance Analytics")
        print("9. Run All Modules")
        print("0. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (0-9): ")
        
        if choice == "1":
            module1_grade_evaluation()
        elif choice == "2":
            module2_course_enrollment()
        elif choice == "3":
            module3_student_records()
        elif choice == "4":
            module4_sorting_searching()
        elif choice == "5":
            module5_fee_calculation()
        elif choice == "6":
            module6_file_handling()
        elif choice == "7":
            module7_directory_scan()
        elif choice == "8":
            module8_performance_analytics()
        elif choice == "9":
            print("\n=== Running All Modules ===")
            module1_grade_evaluation()
            module2_course_enrollment()
            module3_student_records()
            module4_sorting_searching()
            module5_fee_calculation()
            module6_file_handling()
            module7_directory_scan()
            module8_performance_analytics()
        elif choice == "0":
            print("Exiting Smart Campus Information System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")

# ==================== Program Entry Point ====================
if __name__ == "__main__":
    main_dashboard()