import psycopg2 #importing library
from member import *
from trainer import *
from admin import *

#Connecting to the server
conn = psycopg2.connect(database="ClubManagementSystem",
                        user="postgres",
                        password="postgres",
                        port="5432")
cur = conn.cursor()

def signIn():

    valid = 0
    while(valid == 0):
        print("------------\nWELCOME TO LOGIN")
        username = input("Please enter in a valid userName: (type 1 to register as a member instead) ")

        cur.execute("SELECT username, user_role FROM users WHERE username = %s", (username,))
        result = cur.fetchone()  

        if result: 
            valid = 1
            return result[0], result[1]
        else:
            if(username == "1"): 
                return register()
            else: 
                print("Username not found. Please try again.")

import time
print("Welcome to the Health and Fitness Club Management System")
username, userRole = signIn()

print(userRole)
if(userRole == "Member"):
    print("WELCOME: " + username)
    memberControl(username)
elif(userRole == "Trainer"):
    trainerControl(username)
elif(userRole == "Admin"):
    adminControl(username)

    


# cur.execute("SELECT member_name, goal_weight, goal_deadline FROM members WHERE member_username = %s", (username,))
# rows = cur.fetchone() #from the execution result getting all the tuples
# conn.commit()
# for row in rows: #printing
#     print(row)


cur.close()
conn.close()
