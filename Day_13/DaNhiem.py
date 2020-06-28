
import threading


def insertData():
    print("Starting insert data to the database....")
    for i in range(1, 100):
        print("inserting "+str(i))
    print("successfully insert....")


def sendEmail():
    print("Starting send email to user....")
    for i in range(1, 100):
        print("sending "+str(i))
    print("successfully sent....")


t1 = threading.Thread(target=insertData)
t2 = threading.Thread(target=sendEmail)
t1.start()
t2.start()
