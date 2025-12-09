#Hello Dear User! Welcome to Jahra Adan C. Fabon's Interactive menu program! This is his submission for the Finals Project,
#Using ONLY everything he learned, meaning he created this without watching tutorials or learning any new types of code. ONLY using the code that he was taught
#And from what he can recall in his mind (Besides the coding task, he had to get help online for those)
#Hopefully that explains why it looks basic but at least it's his own work!
#This entire thing took him about one week (including break times and sleeps) from coding the actual program to adding decoration.
#Hopefully the code is satisfactory :)

import os
import json
import io
import contextlib

# ------------------------------------------
# THIS TOOK THE MOST TIME TO MAKE SINCE I HAD TO LEARN SOME NEW TYPES OF CODE MYSELF BUT HERE IS WHAT IT DOES:
# This custom function detects the users *OUTPUT*, *NOT* their *INPUT*
# Meaning as long as the output is the exact same as what it requires. The user passes the task
# Example would be for the printing task, User can input either:
# print("Hello World")
# OR
# msg = "Hello World"
# print(msg)
# and the code would still pass as Completed
# **UNFORTUNATELY, THIS ONLY WORKS WITH STRINGS AND WON'T WORK WHEN THE CODE REQUIRES USER INPUT** However, I'm still proud of it and I still have a lot to learn about python
# ------------------------------------------
def coding_task(description, expected_output): #I just have to put a description and the expected output on the specific coding task and it's good to go

    os.system('cls')
    print("==============================================")
    print("                CODING TASK")
    print("==============================================\n")

    print(f"Task: {description}")
    print(f"Expected output:\n{expected_output}\n")

    print("Type your code below. Type END on a new line when you're done:\n")

    # ------------------------------------------
    # Usually just pressing Enter would submit the code already because of input()
    # But by making it a list, It allows users to make a new line by pressing enter
    # ------------------------------------------
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)

    user_code = "\n".join(code_lines)

    # ------------------------------------------
    # This creates an In-Memory file that stores the user's input, basically like a new file but inside this program
    # ------------------------------------------
    f = io.StringIO()

    # ------------------------------------------
    # Try and Except allows me to handle errors myself without stopping the code entirely
    # In this case, it tells the user that there is an error in their code and needs to try again
    # ------------------------------------------
    try:
        with contextlib.redirect_stdout(f): #<----- This replaces the normal output with the In-Memory file, Instead of showing the user's input on screen, it get's stored in f (A.K.A the In-Memory file)
            exec(user_code)
        output = f.getvalue().strip()
    except Exception as e:
        print("\nYour code caused an error:")
        print(f"Error: {e}") #<----- Tells the user where the error in their code is
        input("\nPress Enter to return...")
        return
    
    # ------------------------------------------
    # This part detects whether the output is the exact same or not
    # If yes, the user passes (Obviously)
    # If not, then... you can figure that out
    # ------------------------------------------
    if output == expected_output.strip():
        print("\nCorrect! the output matches the expected result. Great Job :D")
    else:
        print("\nIncorrect output. You can do better :). Just try again!")
        print(f"\nYour output:\n{output}")
        print(f"\nExpected:\n{expected_output}")

    input("\nPress Enter to return...")

def invalid_input():
    print("\n==============================================")
    print("               INVALID INPUT!                ")
    print("            Please try again.               ")
    print("==============================================\n")


def variable_addition():
    num1 = int(input("Enter any number ---> "))
    num2 = int(input("Enter any number ---> "))
    sum = num1 + num2
    print(sum)

def arithmetic_operators():
    num1 = 6
    num2 = 13

    Addition = num1 + num2
    Subtraction = num1 - num2
    Multiplication = num1 * num2
    Division = num1 / num2
    Modulo = num1 % num2
    Power = num1 ** num2
    floor_division = num1 // num2

    print(Addition)
    print(Subtraction)
    print(Multiplication)
    print(Division)
    print(Modulo)
    print(Power)
    print(floor_division)

def comparison_operators():
    a = 13

    b = 6

    print("a == b =", a == b)
    print("a != b =", a != b)
    print("a > b =", a > b)
    print("a < b =", a < b)
    print("a >= b =", a >= b)
    print("a <= b =", a <= b)

def logical_operators():
    print(True and True)
    print(True and False)
    print(True or False)
    print(not True)

def assignment_operators():
    a = 10
    b = 7
    c = 4
    d = 5
    e = 9
    f = 8
    g = 3
    h = 2

    a = 5
    b += 3
    c -= 2
    d *= 2
    e /= 4
    f %= 2
    g **= 3
    h //= 2

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)

def for_loop():
    for loop in range(1,11,1):
        print(loop,"Hello World!")
        print(loop,"My name is Jahra")

def while_loop():
    isDirty = True
    while isDirty == True:
        wash_again = input("Continue Washing the Clothes? (Y/N) ---> ").lower()

        if wash_again == 'y':
            print("Washing...")
            continue
        else:
            print("Stopping...")
            break

def nested_loop():
    for loop in range(1,11,1):
        for x in range(1,loop,1):
            print(x, end= " ")
        print(loop)

# ========================================
# ==========  GREETING SECTION  ==========
# ========================================
name = input("Hello User! Please tell me your name! ---> ")

while True:
    os.system('cls')

    print("========================================")
    print("         INTERACTIVE MENU PROGRAM       ")
    print("========================================")
    program = input("Would you like to start the program? (Yes/No) ---> ").lower()

    if program == "no":
        print("Ok then! Bye Bye!")
        break

    elif program == "yes":
        while True:
            os.system('cls')

            # ========================================
            # ================  MENU  ================
            # ========================================
            print("==============================================")
            print("        W E L C O M E   T O   T H E ")
            print("      I N T E R A C T I V E   M E N U")
            print("==============================================")
            print("Please select an option:\n")
            print("[1] Printing")
            print("[2] Variables")
            print("[3] Operators")
            print("[4] Conditionals")
            print("[5] Loops")
            print("[6] Lists")
            print("[7] Functions")
            print("[8] Exit")
            print("==============================================")

            option = input("Make your choice here! ---> ")

            # ========================================
            # ========== OPTION 1: PRINTING ==========
            # ========================================
            if option == "1":
                os.system('cls')

                print("==============================================")
                print(f"         PRINTING SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nPrinting in Python means displaying text, numbers, or\n"
                    "results on the screen using the print() function.\n"
                    "It's used to show output to the user or to check values while\n"
                    "the program runs."
                )

                while True:
                    print("\n==============================================")
                    print("        TYPES OF PRINTING IN PYTHON")
                    print("==============================================")
                    print("[1] Simple Printing")
                    print("[2] Printing with Strings & Concatenation")
                    print("[3] Coding Task")
                    print("[4] Back to Menu")
                    print("==============================================")

                    printing = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if printing == "1":
                        print("==============================================")
                        print("             SIMPLE PRINTING EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tprint("Hello!")\n'
                            '\tprint("World!")\n\n'
                            "Output:\n\n"
                            "\tHello!\n"
                            "\tWorld!"
                        )
                        continue

                    elif printing == "2":
                        print("==============================================")
                        print("       STRING CONCATENATION PRINTING EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tprint("Hello " + "World!")\n\n'
                            "Output:\n\n"
                            "\tHello World!\n"
                        )
                        continue

                    elif printing == "3":
                        coding_task(
                            "For your task in this lesson, I want you to simply print 'Hello World', Should be easy enough :)",
                            "Hello World"
                        )

                    elif printing == "4":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # =========== OPTION 2: VARIABLES ==============
            # ==============================================
            if option == "2":
                os.system('cls')

                print("==============================================")
                print(f"         VARIABLES SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nIn Python, a variable is a name that stores a value.\n"
                    "It acts like a container where you can keep data and use it later in your program.\n"
                    "Variables can store different types of information such as numbers, text (strings),\n"
                    "lists, or even more complex objects.\n"
                    "You don’t need to declare a type before using a variable—Python automatically knows\n"
                    "the type based on the value you assign."
                )

                while True:
                    print("\n==============================================")
                    print("         TYPES OF VARIABLES IN PYTHON")
                    print("==============================================")
                    print("[1] String Concatenation")
                    print("[2] Integer Addition")
                    print("[3] Coding Task")
                    print("[4] Back to Menu")
                    print("==============================================")

                    variables = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if variables == "1":
                        print("==============================================")
                        print("           STRING CONCATENATION EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tfirst_name = "Jahra"\n'
                            '\tlast_name = "Fabon"\n'
                            '\tfull_name = first_name + " " + last_name\n'
                            '\tprint(full_name)\n\n'
                            "Output:\n\n"
                            "\tJahra Fabon"
                        )
                        continue

                    elif variables == "2":
                        print("==============================================")
                        print("           INTEGER ADDITION EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tnum1 = int(input("Enter any number ---> "))\n'
                            '\tnum2 = int(input("Enter any number ---> "))\n'
                            '\tsum = num1 + num2\n'
                            '\tprint(sum)\n\n'
                            "Output:"
                        )
                        variable_addition()
                        continue

                    elif variables == "3":
                        coding_task(
                            'For your task in this lesson, I want you to Create two variables, a and b. Assign as a=5 and b=10.\n'
                            'Then swap their values (so that a becomes b and b becomes a) and print them in the format: a=<value>, b=<value>\n',
                            "a=10, b=5"
                        )

                    elif variables == "4":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # ============ OPTION 3: OPERATORS =============
            # ==============================================
            elif option == "3":
                os.system('cls')

                print("==============================================")
                print(f"         OPERATORS SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nIn Python, Operators are symbols that perform operations on values or variables. "
                    "They allow you to do calculations, compare values, or combine data."
                )

                while True:
                    print("\n==============================================")
                    print("           TYPES OF OPERATORS IN PYTHON")
                    print("==============================================")
                    print("[1] Arithmetic Operators")
                    print("[2] Comparison Operators")
                    print("[3] Logical Operators")
                    print("[4] Assignment Operators")
                    print("[5] Coding Task")
                    print("[6] Back to Menu")
                    print("==============================================")

                    operators = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if operators == "1":
                        print("==============================================")
                        print("           ARITHMETIC OPERATORS EXAMPLE")
                        print("==============================================")
                        print(
                            "Legend:\n\n"
                            "+ : Addition\n- : Subtraction\n* : Multiplication\n/ : Division\n% : Modulo\n"
                            "** : Power\n// : Floor Division\n"
                        )
                        print(
                            'Input:\n\n'
                            '\tnum1 = 6\n\tnum2 = 13\n\n'
                            '\tAddition = num1 + num2\n'
                            '\tSubtraction = num1 - num2\n'
                            '\tMultiplication = num1 * num2\n'
                            '\tDivision = num1 / num2\n'
                            '\tModulo = num1 % num2\n'
                            '\tPower = num1 ** num2\n'
                            '\tfloor_division = num1 // num2\n\n'
                            '\tprint(Addition)\n\tprint(Subtraction)\n\tprint(Multiplication)\n'
                            '\tprint(Division)\n\tprint(Modulo)\n\tprint(Power)\n\tprint(floor_division)\n\n'
                            'Output:\n'
                        )
                        arithmetic_operators()
                        continue

                    elif operators == "2":
                        print("==============================================")
                        print("         COMPARISON OPERATORS EXAMPLE")
                        print("==============================================")
                        print(
                            "Legend:\n\n"
                            "== : Is Equal To\n!= : Is Not Equal To\n> : Greater Than\n< : Less Than\n"
                            ">= : Greater Than or Equal To\n<= : Less Than or Equal To\n"
                        )
                        print(
                            'Input:\n\n'
                            '\ta = 13\n\tb = 6\n\n'
                            '\tprint("a == b =", a == b)\n'
                            '\tprint("a != b =", a != b)\n'
                            '\tprint("a > b =", a > b)\n'
                            '\tprint("a < b =", a < b)\n'
                            '\tprint("a >= b =", a >= b)\n'
                            '\tprint("a <= b =", a <= b)\n\n'
                            'Output:\n'
                        )
                        comparison_operators()
                        continue

                    elif operators == "3":
                        print("==============================================")
                        print("           LOGICAL OPERATORS EXAMPLE")
                        print("==============================================")
                        print(
                            "Legend:\n\n"
                            "and : True only if both operands are True\n"
                            "or : True if at least one operand is True\n"
                            "not : True if the operand is False and vice-versa\n"
                        )
                        print(
                            'Input:\n\n'
                            '\tprint(True and True)\n'
                            '\tprint(True and False)\n'
                            '\tprint(True or False)\n'
                            '\tprint(not True)\n\n'
                            'Output:\n'
                        )
                        logical_operators()
                        continue

                    elif operators == "4":
                        print("==============================================")
                        print("        ASSIGNMENT OPERATORS EXAMPLE")
                        print("==============================================")
                        print(
                            "Legend:\n\n"
                            "= : Assignment\n+= : Addition Assignment\n-= : Subtraction Assignment\n"
                            "*= : Multiplication Assignment\n/= : Division Assignment\n%= : Remainder Assignment\n"
                            "**= : Exponent Assignment\n//= : Floor Division Assignment\n"
                        )
                        print(
                            "Input:\n\n"
                            '\ta = 10\n\tb = 7\n\tc = 4\n\td = 5\n\te = 9\n\tf = 8\n\tg = 3\n\th = 2\n\n'
                            '\ta = 5\n\tb += 3\n\tc -= 2\n\td *= 2\n\te /= 4\n\tf %= 2\n\tg **= 3\n\th //= 2\n\n'
                            '\tprint(a)\n\tprint(b)\n\tprint(c)\n\tprint(d)\n\tprint(e)\n\tprint(f)\n\tprint(g)\n\tprint(h)\n\n'
                            'Output:\n'
                        )
                        assignment_operators()
                        continue

                    elif operators == "5":
                        coding_task(
                            "Calculate the final price of a 200 product with a 15% Discount and print it.",
                            "170.0"
                        )


                    elif operators == "6":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # ========== OPTION 4: CONDITIONALS ============
            # ==============================================
            elif option == "4":
                os.system('cls')

                print("==============================================")
                print(f"       CONDITIONALS SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nIn Python, Conditionals are statements that allow a program to make decisions "
                    "and execute different code depending on whether a condition is True or False."
                )

                while True:
                    print("\n==============================================")
                    print("      COMMON CONDITIONAL STATEMENTS IN PYTHON")
                    print("==============================================")
                    print("[1] If Statement")
                    print("[2] If Else Statement")
                    print("[3] Elif Statement")
                    print("[4] Nested If Else Statement")
                    print("[5] Coding Task")
                    print("[6] Back to Menu")
                    print("==============================================")

                    conditionals = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if conditionals == "1":
                        print("==============================================")
                        print("               IF STATEMENT EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tage = 19\n'
                            '\tif age >= 18:\n'
                            '\t\tprint("You are of Legal Age!")\n\n'
                            "Output:\n\tYou are of Legal Age!\n"
                        )
                        continue

                    elif conditionals == "2":
                        print("==============================================")
                        print("            IF ELSE STATEMENT EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tage = 17\n'
                            '\tif age <= 18:\n'
                            '\t\tprint("You cannot access this because you are a minor!")\n'
                            '\telse:\n'
                            '\t\tprint("Access Granted!")\n\n'
                            "Output:\n\tYou cannot access this because you are a minor!\n"
                        )
                        continue

                    elif conditionals == "3":
                        print("==============================================")
                        print("               ELIF STATEMENT EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tage = 20\n'
                            '\tif age <= 12:\n'
                            '\t\tprint("Child")\n'
                            '\telif age <= 19:\n'
                            '\t\tprint("Teenager")\n'
                            '\telif age <= 35:\n'
                            '\t\tprint("Young Adult")\n'
                            '\telse:\n'
                            '\t\tprint("Adult")\n\n'
                            "Output:\n\tYoung Adult\n"
                        )
                        continue

                    elif conditionals == "4":
                        print("==============================================")
                        print("          NESTED IF ELSE STATEMENT EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tage = 63\n'
                            '\tis_member = True\n\n'
                            '\tif age >= 60:\n'
                            '\t\tif is_member:\n'
                            '\t\t\tprint("Senior Members get a 30% Discount!")\n'
                            '\t\telse:\n'
                            '\t\t\tprint("Seniors get a 20% Discount!")\n'
                            '\telse:\n'
                            '\t\tprint("Sorry, but you are not eligible for a Seniors Discount")\n\n'
                            "Output:\n\tSenior Members get a 30% Discount!\n"
                        )
                        continue

                    elif conditionals == "5":
                        coding_task(
                            "Create a variable named 'num' and assign it to 5, Check if 'num' is positive, negative, or zero using conditional statements and print the result.",
                            "Positive"
                        )

                    elif conditionals == "6":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # ============= OPTION 5: LOOPS ================
            # ==============================================
            elif option == "5":
                os.system('cls')

                print("==============================================")
                print(f"            LOOPS SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nIn Python, Loops are used to repeat a block of code multiple times until a condition is met "
                    "or a sequence is exhausted. Loops help avoid writing the same code over and over."
                )

                while True:
                    print("\n==============================================")
                    print("           MAIN TYPES OF LOOPS IN PYTHON")
                    print("==============================================")
                    print("[1] For Loop")
                    print("[2] While Loop")
                    print("[3] Nested Loops")
                    print("[4] Coding Task")
                    print("[5] Back to Menu")
                    print("==============================================")

                    loops = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if loops == "1":
                        print("==============================================")
                        print("                 FOR LOOP EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tfor loop in range(1, 11, 1):\n'
                            '\t\tprint(loop, "Hello World!")\n'
                            '\t\tprint(loop, "My name is Jahra")\n\n'
                            'Output:\n'
                        )
                        for_loop()
                        continue

                    elif loops == "2":
                        print("==============================================")
                        print("                WHILE LOOP EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tisDirty = True\n'
                            '\twhile isDirty == True:\n'
                            '\t\twash_again = input("Continue washing the clothes? (Y/N) ---> ").lower()\n'
                            '\n\t\tif wash_again == "y":\n'
                            '\t\t\tprint("Washing...")\n'
                            '\t\t\tcontinue\n'
                            '\t\telse:\n'
                            '\t\t\tprint("Stopping...")\n'
                            '\t\t\tbreak\n\n'
                            'Output:\n'
                        )
                        while_loop()
                        continue

                    elif loops == "3":
                        print("==============================================")
                        print("               NESTED LOOP EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tfor loop in range(1, 11, 1):\n'
                            '\t\tfor x in range(1, loop, 1):\n'
                            '\t\t\tprint(x, end=" ")\n'
                            '\t\tprint(loop)\n\n'
                            'Output:\n'
                        )
                        nested_loop()
                        continue

                    elif loops == "4":
                        coding_task(
                            "Use a loop to print the first 5 even numbers, each on a new line.",
                            "2\n4\n6\n8\n10"
                        )

                    elif loops == "5":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # ============= OPTION 6: LISTS ================
            # ==============================================
            elif option == "6":
                os.system('cls')

                print("==============================================")
                print(f"             LISTS SECTION — Hello {name}!")
                print("==============================================")
                print(
                    "\nIn Python, a list is a collection of items stored in a single variable. "
                    "Lists can hold multiple values of any type, such as numbers, strings, or even other lists. "
                    "They are ordered, changeable, and allow duplicate values."
                )

                while True:
                    print("\n==============================================")
                    print("        LIST NAVIGATION OPTIONS")
                    print("==============================================")
                    print("[1] List Example")
                    print("[2] List Editing")
                    print("[3] Dictionary Example")
                    print("[4] Coding Task")
                    print("[5] Back to Menu")
                    print("==============================================")

                    lists = input("Please select your choice here! ---> ")
                    os.system('cls')

                    if lists == "1":
                        print("==============================================")
                        print("               LIST EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tSentinels_In_Forsaken = ["Shedletsky", "Two Time", "Guest 1337", "Chance"]\n'
                            '\tprint(Sentinels_In_Forsaken[0])\n\n'
                            'Output:\n\n\tShedletsky'
                        )
                        continue

                    elif lists == "2":
                        print("==============================================")
                        print("               LIST EDITING METHODS")
                        print("==============================================")
                        print(
                            ".append(item) - Adds an item to the end of the list\n"
                            ".insert(index, item) - Adds an item at a specific position\n"
                            ".extend(iterable) - Adds all items from another list or iterable\n"
                            ".remove(item) - Removes the first occurrence of a value\n"
                            ".pop(index) - Removes an item at a specific index (default is last)\n"
                            ".clear() - Removes all items from the list\n"
                            ".index(item) - Returns the index of the first occurrence\n"
                            ".count(item) - Returns how many times an item appears\n"
                            ".sort() - Sorts the list in ascending order\n"
                            ".reverse() - Reverses the order of items\n"
                            ".copy() - Returns a shallow copy of a list\n"
                        )
                        continue

                    elif lists == "3":
                        print("==============================================")
                        print("               DICTIONARY EXAMPLE")
                        print("==============================================")
                        print(
                            'Input:\n\n'
                            '\tSentinels_In_Forsaken = {"Best Sentinel": "Shedletsky", "Good Sentinel": "Two Time", '
                            '"Worst Sentinel": "Guest 1337", "Great Sentinel": "Chance"}\n'
                            '\tprint(Sentinels_In_Forsaken["Worst Sentinel"])\n\n'
                            'Output:\n\n\tGuest 1337\n'
                        )
                        continue

                    elif lists == "4":
                        coding_task(
                            "Create the list [3, 7, 2, 9, 4], find the largest number, and print it.",
                            "9"
                        )
                    
                    elif lists == "5":
                        break

                    else:
                        invalid_input()
                        continue

            # ==============================================
            # ========= OPTION 7: FUNCTIONS ================
            # ==============================================
            elif option == "7":
                os.system('cls')

                print("==============================================")
                print(f"      FUNCTIONS SECTION — Hello {name} !")
                print("==============================================")
                print(
                    "\nIn Python, a function is a reusable block of code that performs a specific task.\n"
                    "Functions help make your programs cleaner, easier to read, and easier to maintain."
                )

                while True:
                    print("\n==============================================")
                    print("         FUNCTION NAVIGATION OPTIONS")
                    print("==============================================")
                    print("[1] Def Function")
                    print("[2] Coding Task")
                    print("[3] Back to Menu")
                    print("==============================================")

                    functions = input("Please Select your choice here! ---> ")
                    os.system('cls')

                    if functions == "1":
                        print("==============================================")
                        print("                DEF FUNCTION")
                        print("==============================================")
                        print("\nHere is an example of defining and calling a function in Python:\n")
                        print("Input:\n")
                        print('\tdef greet(name):')
                        print('\t\tprint(f"Hello {name}! Nice to meet you!")\n')
                        print('\tgreet("Jahra")\n')
                        print("Output:\n")
                        print("Hello Jahra! Nice to meet you!\n")
                        continue

                    elif functions == "2":
                        coding_task(
                            "Create a function calculate_area(width, height) that returns width * height, call it with 5 and 3, then print the result.",
                            "15"
                        )
                    
                    elif functions == "3":
                        break

                    else:
                        invalid_input()
                        continue
            
            elif option == "8":
                break
