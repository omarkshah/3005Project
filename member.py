import psycopg2 #importing library
import os

#Connecting to the server
conn = psycopg2.connect(database="ClubManagementSystem",
                        user="postgres",
                        password="postgres",
                        port="5432")
cur = conn.cursor()

userN = ""

def memberControl(user):

    global userN
    userN = user

    inp = -1

    while(inp != 4):
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("Welcome to the member menu! What would you like to do:\n1. Manage Profile \n2. Go to dashboard \n3. Manage Schedule\n4. Logout \nEnter selection:  ")

        if(inp == "1"): 
            manageProfile()

def register():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("------------\nWELCOME TO REGISTERATION")
   
    unique = 0
    username = ""
    while(unique == 0):
        username = input("Enter a username: ")

        cur.execute("SELECT username FROM users WHERE username = %s", (username,))
        result = cur.fetchone()  

        if result: 
            print("That username has already been taken please try a new one")
        else: 
            unique = 1
   
   
    name = input("What is your name: ")

    currentWeight = input("Please enter your current weight (lbs) : ")
    currentHeight = input("Please enter your current height (cm) : ")

    cur.execute("INSERT INTO members(member_username, member_name, current_weight, current_height) VALUES (%s, %s, %s, %s)", (username, name, currentWeight, currentHeight))
    conn.commit()  


    cur.execute("INSERT INTO users(username, user_role) VALUES (%s, %s)", (username, "Member"))
    conn.commit()

    return username, "Member"
    

def manageProfile():
    os.system('cls' if os.name == 'nt' else 'clear')
    inp = input("1. View/Update personal information\n2. View Fitness Acheivments\n3. Health Metrics\n4. Return to previous page\nEnter selection: ")

    if(inp == "1"):
        cur.execute("SELECT member_name, current_weight, current_height FROM members WHERE member_username = %s", (userN,))
        result = cur.fetchone()  

        print(str(result[0]) + "'s Profile:")
        print("Current Weight: " + str(result[1]))
        print("Current Height: " + str(result[2]))
        
        x = input("\nPress Enter to Continue...")

        x = input("\nWould you like to make changes: Y/N ")

        if(x == "Y" or x == "y"):
            x = input("Would you like to change:\n1. Name\n2. Goal Weight\n3. Current Height\n4. Exit\n Enter selection: ")
            if(x == "1"):
                name = input("Please enter a new name: ")
                result =  cur.execute("UPDATE members SET member_name = %s WHERE member_username = %s", (name, userN))
                
                print(result) 
                conn.commit()

                print("Updated Profile: \n")
                cur.execute("SELECT member_name, current_weight, current_height FROM members WHERE member_username = %s", (userN,))
                result = cur.fetchone()  

                print(str(result[0]) + "'s Profile:")
                print("Current Weight: " + str(result[1]))
                print("Current Height: " + str(result[2]))

                x = input("Press Enter to continue...")
            elif(x == "2"):
                weight = input("Please enter a weight: ")
                cur.execute("UPDATE members SET current_weight = %s WHERE member_username = %s", (weight, userN))
                conn.commit()

                print("Updated Profile: \n")
                cur.execute("SELECT member_name, current_weight, current_height FROM members WHERE member_username = %s", (userN,))
                result = cur.fetchone()  

                print(str(result[0]) + "'s Profile:")
                print("Current Weight: " + str(result[1]))
                print("Current Height: " + str(result[2]))
                
                input("Press Enter to continue...")
            elif(x == "3"):
                deadline = input("Please enter a new height: ")
                cur.execute("UPDATE members SET current_height = %s WHERE member_username = %s", (deadline, userN))
                conn.commit()

                print("Updated Profile: \n")
                cur.execute("SELECT member_name, current_weight, current_height FROM members WHERE member_username = %s", (userN,))
                result = cur.fetchone()  

                print(str(result[0]) + "'s Profile:")
                print("Current Weight: " + str(result[1]))
                print("Current Height: " + str(result[2]))

                input("Press Enter to continue...")

    elif(inp == "2"):
        print("YOU HAVE NO FITNESS ACHEIVEMENTS")
        # ADDING A GOAL
        w = input("Please enter your goal weight (lbs): ")
        d = input("Please enter the date you want to acheive this goal by: ")

        cur.execute("INSERT INTO fitness_acheivments(goal_weight, goal_deadline) VALUES (%s, %s)", (w, d))
        conn.commit()

    elif(inp == "3"):
        # print("Add some metric")
        # ADDING A METRIC
        metIn = input("Choose a metric to input:\n1.BMI\n2.Height (cm) \n3.Weight (lbs) \n Enter input here: ")
        metric = ""
        if(metIn == "1"):
            metric = "BMI"
        elif(metIn == "2"):
            metric = "Height"
        elif(metIn == "3"):
            metric = "Weight"
        measure = input("Please enter a measure for your metric: ")
        currDate = input("Please enter the current date: ")

        cur.execute("INSERT INTO metrics(member_username, metric_type, metric_measure, date_measured) VALUES (%s, %s, %s, %s)", (username, metric, measure, currDate))
        conn.commit()

