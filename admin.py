import psycopg2 #importing library
import os

#Connecting to the server
conn = psycopg2.connect(database="ClubManagementSystem",
                        user="postgres",
                        password="postgres",
                        port="5432")
cur = conn.cursor()

adminN = ""

def adminControl(user):

    global adminN
    adminN = user

    inp = -1

    while(inp != 6):
        os.system('cls' if os.name == 'nt' else 'clear')
        inp = input("Welcome to the admin menu! What would you like to do:\n1. View bookings \n2. Book a Room \n3. Equipment Maintanence Monitoring \n4. Update Class Schedule\n5. View Billings\n6. Create a Billing\n7. Logout \nEnter selection:  ")

        if(inp == "1"):
            viewBookings()
        elif(inp == "2"): 
            bookRoom()
        elif(inp == "3"):
            monitorMaint()
        elif(inp == "4"):
            updateClassSched()
        elif(inp == "5"):
            viewBills()
        elif(inp == "6"):
            createBill()
        else:
            inp = 6

def viewBookings(): 
    os.system('cls' if os.name == 'nt' else 'clear')

    
    cur.execute("SELECT admin_name FROM admins WHERE admin_username = %s", (adminN,))
    name = cur.fetchone()[0]

    print(name + "'s Bookings: \n")

    cur.execute("SELECT room_number, booking_time FROM room_bookings WHERE booker_username = %s", (adminN,))
    results = cur.fetchall()  

    i = 1
    if results: 
        for result in results:
            print(str(i) + ". Room: " + str(result[0]) + " Booked At: " + str(result[1]))
    
    input("Press enter to continue...")

def bookRoom():
    os.system('cls' if os.name == 'nt' else 'clear')
    # get time stamp
    d = input("Please enter a date for your room booking: ")
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

    print("All available rooms: ")
    cur.execute("SELECT rooms.room_number, rooms.room_capacity FROM rooms LEFT JOIN room_bookings ON rooms.room_number = room_bookings.room_number WHERE room_bookings.room_number IS NULL;")
    results = cur.fetchall()  




    os.system('cls' if os.name == 'nt' else 'clear')
    i = 1
    if(results):
        for result in results:
            print(str(i) + ". " + str(result[0]) + " Capcity: " + str(result[1]))
            i = i + 1
    
        inp = input("Please select a room by choosing its corresponding number: ")
        inp = int(inp)
        if(inp >= 1 and inp < i):
            #add result[inp -1][0] and timestamp and adminusername to room_booking
            cur.execute("INSERT INTO room_bookings(room_number, booker_username, booking_time) VALUES (%s, %s, %s)", (results[inp - 1][0], adminN, timestamp))
            conn.commit()  

            viewBookings()

    else: 
        input("NO AVAILABLE ROOMS...")

def monitorMaint():
    os.system('cls' if os.name == 'nt' else 'clear')
    inp = input("Would you like to:\n1. View Maintenance Logs\n2. Log a new Equipment Maintenance\nEnter selection: ")

    if(inp == "1"):
        os.system('cls' if os.name == 'nt' else 'clear')

    
        cur.execute("SELECT equipment_name, cost, maintenance_date FROM equipment_maintenance")
        results = cur.fetchall()

        print("MAINTENANCE LOGS")
        print('---')

        if results:
            for result in results:
                print(result[0] + "\nCost: $" + str(result[1]) + "\nDate: " + str(result[2]))
                print('---')
        else:
            print("Nothing to display...")
        input("Press enter to continue...")

    elif(inp == "2"): 

        equipName = input("Please enter the equipment name: ")
        cost = input("Please enter the cost of maintenance: ")
        mainDate = input("Please enter the date the maintenance was done: ")

        cur.execute("INSERT INTO equipment_maintenance(equipment_name, cost, maintenance_date) VALUES (%s, %s, %s)", (equipName, int(cost), mainDate))
        conn.commit()  

def updateClassSched():
    os.system('cls' if os.name == 'nt' else 'clear')
    inp = input("Do you want to:\n1. Add a class \n2. Cancel a class\nEnter a selection: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    #adding a schedule to classes
    #pick a data time + class name
        # if there is a trainer with availability during datetime then add class to classes table
    if(inp == "1"):
       
    # get time stamp
        d = input("Please enter a date for your class: ")
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

        cur.execute("SELECT trainer_username, availability_id FROM availability WHERE avail_time = %s ", (timestamp,))
        result = cur.fetchone() 

        cName = input("Please enter a name for the class: ")

        if(result): 
            cur.execute("INSERT INTO group_fitness_classes(class_name, trainer_username, class_time) VALUES (%s, %s, %s)", (cName, result[0], timestamp))
            conn.commit()  

            cur.execute("DELETE FROM availability WHERE availability_id = %s", (result[1],))
            conn.commit()

        else:
            input("No trainers with this availability...")


    #removing a class (cancelling) 
    # get classId from classes table
    # remove all particiapnt in classID from participants table
    # remove classId from classes table
    elif(inp == "2"): 
        
        cur.execute("SELECT class_name, trainer_username, class_time, class_id FROM group_fitness_classes")
        results = cur.fetchall()

        i = 0
        if(results):
            for result in results:
                print(str(i) + ". " + result[0] + "with " + result[1] + " at " + str(result[2]))
                i = i + 1

            x = input("Enter the class you would like to cancel (number): ")
            x = int(x)
            if(x >= 1 and x < i):
                classId = results[x - 1][3]

                cur.execute("DELETE FROM group_fitness_participants WHERE class_id = %s", (classId,))
                conn.commit()

                cur.execute("DELETE FROM group_fitness_classes WHERE class_id = %s", (classId,))
                conn.commit()

                print("NEW SCHEDULE")
                cur.execute("SELECT class_name, trainer_username, class_time, class_id FROM group_fitness_classes")
                results = cur.fetchall()

                i = 1
                if(results):
                    for result in results:
                        print(str(i) + ". " + result[0] + "with " + result[1] + " at " + str(result[2]))
                        i = i + 1

                input("Press enter to continue...")

def viewBills():
    cur.execute("SELECT member_username, amount, billing_description, billing_date FROM billings")
    results = cur.fetchall()

    if(results):
        for result in results: 
            print("$" + str(result[1]) + " billed to " + result[0] + " for " + result[2] + " on " + str(result[3]))
    else:
        print("NO BILLINGS FOUND")
    
    input("Press enter to continue...")

def createBill():

    memUser = input("Enter the member's username that you want to charge: ")
    amount = input("Enter the amount you want to change: ")
    descr = input("Enter the billing description: ")
    billing_date = input("Enter the current date: ")

    cur.execute("INSERT INTO billings(member_username, amount, billing_description, billing_date) VALUES (%s, %s, %s, %s)", (memUser, amount, descr, billing_date))
    conn.commit()  