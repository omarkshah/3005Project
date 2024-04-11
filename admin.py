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
    return

def updateClassSched():
    return

def viewBills():
    return

def createBill():
    return
