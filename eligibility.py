attendance = float(input("Enter your attendance percentage: "))
assignments_submitted = input("Have you submitted all assignments? (yes/no): ")

if attendance >= 75 and assignments_submitted.lower() == "yes":
    print("You are eligible to sit for the exam.")
else:
    print("You are NOT eligible to sit for the exam.")
