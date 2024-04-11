import psycopg2 #importing library
import os

#Connecting to the server
conn = psycopg2.connect(database="ClubManagementSystem",
                        user="postgres",
                        password="postgres",
                        port="5432")
cur = conn.cursor()

trainerN = ""

def trainerControl(trainer):
    global trainerN
    trainerN = trainer

    inp = -1

    while(inp != 5):
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("Welcome to the trainer menu! What would you like to do:\n1. View Availability\n2. Add availability \n3. Remove availability \n4. Member Search \n5. Logout\nEnter selection:  ")

        if(inp == "1"):
            viewAvail()
        elif(inp == "2"): 
            addAvail()
        elif(inp == "3"):
            removeAvail()
        elif(inp == "4"):
            memberSearch()
        else: 
            inp = 5


def viewAvail():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("YOUR AVAILABILITY:\n")


    cur.execute("SELECT avail_time FROM availability WHERE trainer_username = %s ORDER BY avail_time", (trainerN,))
    results = cur.fetchall()  

    if(results):
        for result in results: 
            print(str(result[0]))
    
    input("Press enter to continue...")

    return

def addAvail():
    os.system('cls' if os.name == 'nt' else 'clear')

    d = input("Please enter a data for your availability: ")
    inp = input("Please choose a time: \n1. 9:00 \n2. 10:00 \n3. 11:00 \n4. 12:00 ")

    timestamp = ""
    if(inp == "1"):
        timestamp = d + " 9:00"
    elif(inp == "2"):
        timestamp = d + " 10:00"
    elif(inp == "3"):
        timestamp = d + " 11:00"
    else: 
        timestamp = d + " 12:00"
    
    #check if this availability already exists #IF - say it does IF NOT - add avail
    cur.execute("SELECT trainer_username, availability_id FROM availability WHERE avail_time = %s ", (timestamp,))
    result = cur.fetchone()  

    if result: 
        print("An availability for the given time already exists")
        input("Press enter to continue...")
    else:
        cur.execute("INSERT INTO availability(trainer_username, avail_time) VALUES (%s, %s)", (trainerN, timestamp))
        conn.commit()       

    viewAvail()

def removeAvail():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("CURRENT AVAILABILITY:\n")


    cur.execute("SELECT avail_time, availability_id FROM availability WHERE trainer_username = %s ORDER BY avail_time", (trainerN,))
    results = cur.fetchall()  

    max = 0

    print(results)

    if(results):
        for result in results: 
            print((str(result[1])) + ". " + str(result[0]))
            if(int(result[1]) > max):
                max = int(result[1])

        inp = input("Please choose an availability to remove: ")

        if(int(inp) < 1 or int(inp) > max):
            input("Invalid choice...")
        else:
            cur.execute("DELETE FROM availability WHERE availability_id = %s", (inp,))
            conn.commit()
            viewAvail()

def memberSearch():
    os.system('cls' if os.name == 'nt' else 'clear')

    name = input("Please enter a member's name (Enter 1 to receive a list of member names): ")

    if(name == "1"):
        os.system('cls' if os.name == 'nt' else 'clear')
        cur.execute("SELECT member_name FROM members")
        results = cur.fetchall()  

        index = 1

        if(results):
            for result in results: 
                print(str(index) + ". " + result[0])
                index = index + 1

            inp = input("Select a member from the list (type the corresponding number): ")
            inp = int(inp)
            if(inp > 0 and inp < index):    
                name = results[inp - 1][0]


    os.system('cls' if os.name == 'nt' else 'clear')
    cur.execute("SELECT member_username, member_name, current_weight, current_height FROM members WHERE member_name = %s", (name,))
    results = cur.fetchall()  

    if(results):
        
        i = 1

        for result in results:
            print(str(i) + ". " + result[0])
            i = i + 1
        
        select = input("Please select a user: ")

        if(int(select) >= 1 and int(select) < i):     
            os.system('cls' if os.name == 'nt' else 'clear')

            print(results[int(select) - 1][1] + "'s Profile:")
            print("Current Weight: " + str(results[int(select) - 1][2]))
            print("Current Height: " + str(results[int(select) - 1][3]))

            input("\nPress enter to continue...")
        else: 
            input("Your selection was not valid. Press enter to continue...")
