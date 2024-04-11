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

    while(inp != 4):
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("Welcome to the trainer menu! What would you like to do:\n1. View Availability\n2. Add availability \n3. Remove availability \n4. Member Search \nEnter selection:  ")

        if(inp == "1"):
            viewAvail()
        elif(inp == "2"): 
            addAvail()
        elif(inp == "3"):
            removeAvail()
        elif(inp == "4"):
            memberSearch()

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
    return

def memberSearch():
    return