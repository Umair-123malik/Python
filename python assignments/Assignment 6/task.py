def manage_student_database():
    students = []  # List to store student tuples (ID, Name)
    student_names = set()  # Set to track unique student names
    student_id = 1  # Initialize student ID starting from 1

    while True:
        # Prompt for student name input
        name = input("Please enter the student's name (or type 'stop' to finish): ")

        # Check if the user wants to stop the input process
        if name.lower() == "stop":
            break

        # Check for duplicate names
        if name in student_names:
            print("This name is already in the list.")
        else:
            # Add the student's name to the list and set
            students.append((student_id, name))
            student_names.add(name)
            student_id += 1

    # Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Calculate the total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")

    # Find the student with the longest and shortest names
    if students:
        longest_name_student = max(students, key=lambda x: len(x[1]))[1]
        shortest_name_student = min(students, key=lambda x: len(x[1]))[1]
        print(f"The student with the longest name is: {longest_name_student}")
        print(f"The student with the shortest name is: {shortest_name_student}")

# Call the function to run the program
manage_student_database()
