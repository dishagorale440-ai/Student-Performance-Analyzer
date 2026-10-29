## import modules
import csv   ##(helps save student records in a table-like file.)
import os
  ##(helps check whether the file already exists)
# This Funtion keep asking untill valid marks are entered
def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks : "))
            if(0<= marks <=100):
                return marks
            print("Invalid marks! Please enter marks between 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Validate Student Name
def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        #check whether the name is empty
        if not name:
            print("Student name cannot be empty. Please try again.")
        # Allow only letters and spaces
        elif all(part.isalpha() for part in name.split()):
            return name
        else:
            print("Invalid name! Please enter letter only.")

# Update the CSV file to include the failed subject colum
def update_csv_format():
    filename = "student_records.csv"
    # Check whether the csv file exists
    if not os.path.exists(filename):
        return
    # read all existing records
    with open(filename, "r", newline="")as file:
        reader = csv.reader(file)
        rows = list(reader)
    # stop if the file is empty
    if not rows:
        return
    # Define the new csv heading
    new_header = [
        "Name", "Maths", "Physics", "Chemistry", 
        "Total Marks", "Percentage", "Grade", "Result", 
        "Failed subject"
    ]
    # check wherther the file already has the new headings
    if rows[0] == new_header:
        return
    # check whether the file has the old headings
    old_header = new_header[:8]
    if rows[0] == old_header:
        updated_rows = [new_header]
        # Add the failed-subject information to old records
        for row in rows[1:]:
            if len(row) == 8:
                failed_subject = []

                try:
                    if float(row[1])<35:
                        failed_subject.append("Maths")
                    if float(row[2])<35:
                        failed_subject.append("Physics")
                    if float(row[3])<35:
                        failed_subject.append("Chemistry")
                    failed = ", ".join(failed_subject) if failed_subject else "None"
                    updated_rows.append(row + [failed])
                except ValueError:
                    updated_rows.append(row + ["Unknown"])
            elif len(row) == 9:
                updated_rows.append(row)
        # Write the update records back to the csv file
        with open(filename, "w", newline="")as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("CSV file formate update successfully.")

# Save student records
def save_student(name, maths, physics, chemistry, 
                total_marks, percentage, grade, result, failed_subjects):
    update_csv_format()
    file_exists = os.path.exists("student_records.csv")
    try:
        with open("student_records.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # Add headings only when creatin a new file
            if not file_exists:
                writer.writerow([
                    "Name", "Maths", "Physics", "Chemistry", 
                    "Total Marks", "Percentage", "Grade", "Result", "Failed subject"
                ])
            # save the student's details
            writer.writerow([
                name, maths, physics, chemistry, 
                total_marks, round(percentage, 2), grade, result, 
                ", ".join(failed_subjects) if failed_subjects else "None"
            ])
        return True
    except OSError as error:
        ## except OSError- catches common files-related errors,such as permission problems. 
        print(f"Unable to save student record: {error}")
        return False

## view All student record
def view_student_records():
    #check whether the CSV file exists
    if not os.path.exists("student_records.csv"):
        print("\nNo student records found yet.")
        return
    # Read the csv file
    with open("student_records.csv", "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    # check whether student record are available
    if len(rows) <= 1:
        print("\nNo student records found yet.")
        return
    # Display the saved records
    print("\n" + "=" * 100)
    print("SAVED STUDENT RECORDS")
    print("=" * 100)

    for row in rows:
        print(" | ".join(row))
    print("=" * 100)

# Search Student by name
def search_student():
    # Ask for the student's name
    while True:
        search_name = input("\nEnter student name to search: ").strip()  
            ## strip() remove unnecessary spaces around the name.
        if search_name:
            break
        print("Student name cannot be empty. Please try again.")
    #check whether the csv file exists
    if not os.path.exists("student_records.csv"):
        print("\nNo student records found.")
        return

    # Read the saved student records
    with open("student_records.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
                  ## csv.DictReader() read the CSV file using its column heading.
        found = False
           ##found- tracks whether a matching student was found
        for student in reader:
            # Search without case sensitivity
            if student["Name"].strip().lower() == search_name.lower():
                print("\n" + "=" * 40)
                print("       STUDENT DETAILS")
                print("=" * 40)

                print("Name          :",student["Name"])
                print("Maths         :",student["Maths"])
                print("Physics       :",student["Physics"])
                print("Chemistry     :",student["Chemistry"])
                print("Total Marks   :",student["Total Marks"])
                print("Percentage    :",student["Percentage"], "%")
                print("Grade         :",student["Grade"])
                print("Result        :",student["Result"])
                print("Failed Subject:",student.get("Failed subject", "None"))

                print("=" * 40)
                found = True

        #Dispaly a message if no matching student exists
        if not found:
            print("\nStudent not found!")

# create Student Analysis Function
def analyze_student():
    # Get Student Name
    print("Student Performance Analyzer")
    print("Welcome!")
    
    # Ask the user to enter the student's name
    
    name = get_student_name()
    print("Student Name : ",name)

    # Get marks for all subjects
    maths = get_marks("Maths")
    physics = get_marks("Physics")
    chemistry = get_marks("Chemistry")
        
    print("Maths Marks : ", maths)
    print("Physics Marks : ", physics)
    print("Chemistry Marks : ", chemistry)
        
    # Calculate the Total Marks
        
    total_marks = maths + physics + chemistry
    print("Total Marks : ", total_marks)
        
    # Calculate the Percentage
        
    percentage = (total_marks/300)*100
    print("Percentage : ", percentage)
        
    # Decide the Grade based on percentage
        
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "E"
    print("Grade : ", grade)
        
    #check wheather the student has passed each subject
    failed_subjects = []
    if maths < 35:
        failed_subjects.append("Maths")
    if physics < 35:
        failed_subjects.append("Physics")
    if chemistry < 35:
        failed_subjects.append("Chemistry")
    if failed_subjects:
        result = "Fail"
    else:
        result = "Pass"    
        
    # create a professional Report
    print("\n")
    print("="*40)
    print("      STUDENT PERFORMANCE REPORT")
    print("="*40)
        
    print("Student Name : ", name)
    print("Maths        : ", maths)
    print("Physics      : ", physics)
    print("Chemistry    : ", chemistry)
    print("-"*40)
        
    print("Total Marks : ", total_marks)
    print("Percentage  : ", round(percentage, 2),"%")
    print("Grade       : ", grade)
    print("Result      : ", result)
    if failed_subjects:
        print("Failed Subject:",",".join(failed_subjects))

    # save the student record to a csv file
    saved = save_student(
        name, maths, physics, chemistry, 
        total_marks, percentage, grade, result, failed_subjects
    )
    if saved:
        print("Student record saved successfully!")

    print("="*40)
    print("      Thank you for using the analyzer!")
    print("="*40)

    again = input("\nDo you want to analyze another student? (yes/no): ")
    return again.strip().lower()
        
# Create Main Menu
while True:
    print("\n====================================")
    print("      STUDENT PERFORMANCE ANALYZER")
    print("======================================")

    print("1. Analyze Student Performance")
    print("2. View All Student Records")
    print("3. Search Student Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Analyze student performance

    if choice == "1":
        while True:
            print("\nStarting Student Performance Analysis...")
            again = analyze_student()

            if again != "yes":
                break

    #option 2: View all saved records

    elif choice == "2":
        view_student_records()
        print("\nReturning to the main menu....")

    #Option 3: Search for a student
    elif choice == "3":
        search_student()
        print("\nReturning to the main menu....")

    # Option 4: Exit the program         
    elif choice == "4":
        print("\nThank you for using the analyzer!")
        print("Goodbye!")
        break
    # Handel invaild choices
    else:
        print("Invalid choice ! Please enter 1,2,3, or 4.")




