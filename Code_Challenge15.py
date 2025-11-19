import os
import json
student_record = {}
os.system('cls')

print("DLL Student Information System\n")

while True:
    
    print("Select from the options below\nA - Add Student Record\nB - Print All Student Record\nC - Search Student Record\nD - Delete Student Record\nE - Edit Student Record\nF - Export Data\nG - Exit System")
    choice = input("Please Choose Your Option ---> ").lower().strip()

    if choice == "a":
        os.system('cls')
        print("Please add a student record")
        student_id = input("Student ID ---> ")
        first_name = input("First Name ---> ").upper()
        last_name = input("Last Name ---> ").upper()
        course = input("Student Course ---> ").upper()
        section = input("Student Section ---> ").upper()
        email = input("Student Email ---> ")
        student_record[student_id] = [first_name, last_name, course, section, email]
        print("Data Saved")
        continue
    elif choice == "b":
        os.system('cls')
        print("Printing All Student Record!")
        for id, info in student_record.items():
            print(f"Student ID - {id} Record - {info}")
        continue
    elif choice == "c":
        os.system('cls')
        print("Search Student Record")
        search_id = input("Enter Student ID ---> ")
        for each_student in student_record.keys():
            if search_id in student_record.keys(): #If makes your Search align With a Value
                print("Student Record Found!\nStudent's Record:")
                for id in student_record[search_id]:
                    print(f"-{id}")
            else:
                print("No Record Found!")
            break
        continue
    elif choice == "d":
        os.system('cls')
        print("Delete Student Record")
        search_id = input("Enter Student ID ---> ")
        for each_student in student_record.keys():
            if search_id in student_record.keys():
                print("Student Record Found!\nStudent's Record:")
                for id in student_record[search_id]:
                    print(f"-{id}")
                student_record.pop(search_id) #Deleting a Record
                print("Record has been deleted!")
            else:
                print("No Record Found!")
            break
        continue
    elif choice == "e":
        os.system('cls')
        print("Edit Student Record")
        search_id = input("Enter Student ID ---> ")
        for each_student in student_record.keys():
            if search_id in student_record.keys(): 
                print("Student Record Found!\nStudent's Record:")
                for id in student_record[search_id]:
                    print(f"-{id}")
                student_id = input("Student ID ---> ")
                first_name = input("First Name ---> ").upper()
                last_name = input("Last Name ---> ").upper()
                course = input("Student Course ---> ").upper()
                section = input("Student Section ---> ").upper()
                email = input("Student Email ---> ")

                student_record[search_id][0] = first_name
                student_record[search_id][1] = last_name
                student_record[search_id][2] = course
                student_record[search_id][3] = section
                student_record[search_id][4] = email
                print("Data Edited Successfully")
            else:
                print("No Record Found!")
            break
        continue
    elif choice == "f":
        print("Export Data")
        #json - javascript obejct notation -w (write)
        with open("student_record.json" : "w") as new_file:
            json.dump(student_record, new_file, indent=4)
        print("File Exported Successfully!")
        continue
    elif choice == "g":
        print("Exiting System!")
        break
    else:
        print("Invalid Choice")
        continue
