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

    while(inp != 5):
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("Welcome to the member menu! What would you like to do:\n1. Manage Profile \n2. Go to dashboard \n3. Manage Schedule\n4. Manage Exercise Routine \n5. Logout\nEnter selection:  ")

        if(inp == "1"): 
            manageProfile()
        elif(inp == "2"):
            memberDashboard()
        elif(inp == "3"):
            manageSchedule()
        elif(inp == "4"):
            manageExercise()
        else:
            inp = 5

def manageExercise():
    os.system('cls' if os.name == 'nt' else 'clear')
    cur.execute("SELECT routine_name, routine_description, duration FROM exercise_routine WHERE member_username = %s", (userN,))
    result = cur.fetchone()  

    if result:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(result[0] + ":\n" + result[1] + "\nDuration: " + str(result[2]))

        inp = input("Would you like to make a change? Y/N: ")

        if(inp == "Y" or inp== "y"):
            x = input("What would you like to change: \n1. Name\n2. Description\n3. Duration \nEnter your selection: ")
            if(x == "1"):
                name = input("Please enter a new routine name: ")
                
                cur.execute("UPDATE exercise_routine SET routine_name = %s WHERE member_username = %s", (name, userN))
                conn.commit()
            elif(x == "2"):
                desc = input("Please enter a new description: ")

                cur.execute("UPDATE exercise_routine SET routine_description = %s WHERE member_username = %s", (desc, userN))
                conn.commit()           
            elif(x == "3"):
                dur = input("Please enter a new duration: ")
                dur = int(dur)
                cur.execute("UPDATE exercise_routine SET duration = %s WHERE member_username = %s", (dur, userN))
                conn.commit()  
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("No routine found. Would you like to add one? Y/N: ")

        if(inp == "y" or inp == "Y"):
            name = input("Please enter a routine name: ")
            desc = input("Please enter a description: ")
            dur = input("Please enter a duration: ")

            cur.execute("INSERT INTO exercise_routine(member_username, routine_name, routine_description, duration) VALUES (%s, %s, %s, %s)", (userN, name, desc, dur))
            conn.commit()  

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
    inp = input("1. View/Update personal information\n2. Add Fitness Acheivments\n3. Add Health Metrics\n4. Return to previous page\nEnter selection: ")

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
        # ADDING A GOAL
        w = input("Please enter your goal weight (lbs): ")
        d = input("Please enter the date you want to acheive this goal by: ")

        cur.execute("INSERT INTO fitness_acheivments(member_username, goal_weight, goal_deadline) VALUES (%s, %s, %s)", (userN, w, d))
        conn.commit()

    elif(inp == "3"):
        # print("Add some metric")
        # ADDING A METRIC
        metIn = input("Choose a metric to input:\n1.BMI\n2.Height (cm) \n3.Weight (lbs) \nEnter input here: ")
        metric = ""
        if(metIn == "1"):
            metric = "BMI"
        elif(metIn == "2"):
            metric = "Height"
        elif(metIn == "3"):
            metric = "Weight"
        measure = input("Please enter a measure for your metric: ")
        currDate = input("Please enter the current date: ")

        cur.execute("INSERT INTO metrics(member_username, metric_type, metric_measure, date_measured) VALUES (%s, %s, %s, %s)", (userN, metric, measure, currDate))
        conn.commit()

def memberDashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    inp = input("1. Display exercise routine\n2. Display Fitness Achievements\n3. Health Statistics\nEnter selection: ")

    if(inp == "1"):
        cur.execute("SELECT routine_name, routine_description, duration FROM exercise_routine WHERE member_username = %s", (userN,))
        results = cur.fetchall()  

        print("EXERCISE ROUTINES")
        for result in results:
            print(result[0] + ": \nDescription: \n" + result[1] + "\n Duration: " + str(result[2]))
            input("Press enter to continue...")

    elif(inp == "2"):
        cur.execute("SELECT goal_weight, goal_deadline FROM fitness_acheivments WHERE member_username = %s", (userN,))
        results = cur.fetchall()  

        print("FITNESS ACHEIVMENTS")
        for result in results:
            print(str(result[0]) + ": lbs to be acheived by " + str(result[1]))
            input("Press enter to continue...")
    
    elif(inp == "3"): 
        cur.execute("SELECT metric_measure, date_measured FROM metrics WHERE member_username = %s AND metric_type = %s ORDER BY date_measured", (userN, "BMI"))
        results = cur.fetchall()  

        if(results): 
            print("BMI STATISTICS")
            for result in results:
                print(str(result[1]) + ": "  + str(result[0]))

        cur.execute("SELECT metric_measure, date_measured FROM metrics WHERE member_username = %s AND metric_type = %s ORDER BY date_measured", (userN, "Height"))
        results = cur.fetchall()  

        if(results): 
            print("HEIGHT STATISTICS")
            for result in results:
                print(str(result[1]) + ": "  + str(result[0]) + " cm")

        cur.execute("SELECT metric_measure, date_measured FROM metrics WHERE member_username = %s AND metric_type = %s ORDER BY date_measured", (userN, "Weight"))
        results = cur.fetchall()  

        if(results): 
            print("WEIGHT STATISTICS")
            for result in results:
                print(str(result[1]) + ": "  + str(result[0]) + " lbs")
        
        input("Press enter to continue...")

def ptReg():
    # input time from hardcoded 
    # check availability table for time
    # if there add pt sesh to table
    # if not there say time/date not avail try again
    os.system('cls' if os.name == 'nt' else 'clear')

    x = input("Please input a date: ")

    timestamp = ""
    inp = input("Please enter choose a time for the data:\n1. 9:00\n2.10:00\n3. 11:00\n4.12:00")
    if(inp == "1"):
        timestamp = x + " 9:00"
    elif(inp == "2"):
        timestamp = x + " 10:00"
    elif(inp == "3"):
        timestamp = x + " 11:00"
    else: 
        timestamp = x + " 12:00"

    cur.execute("SELECT trainer_username, availability_id FROM availability WHERE avail_time = %s", (timestamp,))
    results = cur.fetchall()  

    if(results):
        cur.execute("INSERT INTO pt_sessions(trainer_username, member_username, session_time) VALUES (%s, %s, %s)", (results[0][0], userN, timestamp))
        conn.commit()

        cur.execute("DELETE FROM availability WHERE availability_id = %s", (results[0][1],))
        conn.commit()
    else: 
        print("NO AVAILABLE TIME\n")
        input("Press enter to continue...")

def classReg():
    os.system('cls' if os.name == 'nt' else 'clear')

    cur.execute("SELECT class_name, class_time, class_id FROM group_fitness_classes")
    results = cur.fetchall()  
    
    if results:
        i = 1
        for result in results: 
            print(str(i) + ". " + result[0] + "\nTime: " + str(result[1]))
            i = i + 1
        
        inp = input("Please enter your selection for class: ")

        if(int(inp) < 1 or int(inp) >= i):
            return
        else:
            cur.execute("INSERT INTO group_fitness_participants(member_username, class_id) VALUES (%s, %s)", (userN, results[int(inp)-1][2]))
            conn.commit()

def manageSchedule():
    os.system('cls' if os.name == 'nt' else 'clear')
    inp = input("1. View Schedule\n2. Register for Personal Training \n3. Register for Group Fitness Class")

    if(inp == "1"):
        os.system('cls' if os.name == 'nt' else 'clear')

        cur.execute("SELECT trainer_username, session_time FROM pt_sessions WHERE member_username = %s", (userN,))
        results = cur.fetchall()  

        if(results):
            for result in results:
                tUn = result[0]
                sessionTime = str(result[1])

                cur.execute("SELECT trainer_name FROM trainers WHERE trainer_username = %s", (tUn,))
                result = cur.fetchone()  

                trainerName = result[0]

                print("Session with " + trainerName + " at " + sessionTime)

        cur.execute("SELECT class_id FROM group_fitness_participants WHERE member_username = %s", (userN,))
        classes = cur.fetchall()  

        for fClass in classes: 
            cur.execute("SELECT class_name, trainer_username, class_time FROM group_fitness_classes WHERE class_id = %s", (fClass[0],))
            result = cur.fetchone()

            if(result):
                className = result[0]
                tUn = result[1]
                classTime = result[2]

                cur.execute("SELECT trainer_name FROM trainers WHERE trainer_username = %s", (tUn,))
                r = cur.fetchone()  
                
                trainerName = r[0]

                print(className + " class with " + trainerName + " at " + str(classTime))



        
        input("Press enter to continue...")
    elif(inp == "2"):
        ptReg()
    elif(inp == "3"):
        classReg()

        

