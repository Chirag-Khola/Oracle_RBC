import pyautogui as pt
from time import sleep
import pyperclip
import random
import os
print("Working dir:", os.getcwd())
print("Files in here:", os.listdir("."))

sleep(3)

position1 = pt.locateOnScreen("smiley (2).png", confidence=.6)
x = position1[0]
y = position1[1]

#gets message
def get_message():
    global x,y

    postion = pt.locateOnScreen("smiley (2).png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 171, y - 90, duration=.5)
    # pt.tripleClick()
    
    
    pt.rightClick()
    copyy = pt.locateOnScreen("copy.jpg", confidence=.6)
    pt.moveTo(copyy)
    pt.moveRel(0,-30)
    pt.click()
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)
    print(whatsapp_message)

    return whatsapp_message

#posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley (2).png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

#process response
def process_response(message):
    random_no = random.randrange(3)

    if "?"in str(message).lower():
        return "Interesting question, I'll talk to you about that later - ORACLE"

    else:
        if "hi"in str(message).lower():
            return "Hey, a bit busy right now. just drop a message ill talk to you later- ORACLE"
        elif "happy new year"in str(message).lower():
            return "Wishing you and your family a very Happy New Year! ✨.May this year bring joy and happiness in your life! - ORACLE "
        elif "good morning"in str(message).lower():
            return "Good Morning! Have a great day"
        elif "good night"in str(message).lower():
            return "Good Night! Sleep tight"
        elif "knock knock"in str(message).lower():
            return "Who's There"
        elif "how"in str(message).lower():
            return "Chirag cannot take your message right now, but am sure he's fine :) - ORACLE"
        elif "class" in str(message).lower():
            return"Here's the class schedule for Chirag as of today:- \n (9:30 AM-10:30 AM) \n (10:30AM-11:30AM) \n (11:30AM-12:30PM) \n (1:40PM-3:35PM) \n -ORACLE "
        elif "where" in str(message).lower():
            return "Sorry , Chirag cannot take your message right now. \n Here's the class schedule for Chirag as of today:- \n (9:30 AM-10:30 AM) \n (10:30AM-11:30AM) \n (11:30AM-12:30PM) \n (1:40PM-3:35PM) \n -ORACLE"
        else :
            return "Hello! Dear Sir/Madam, Chirag is currently unavailable to reply. Do drop your messages. - ORACLE"


#new messages check
def check_for_new_messages():
    pt.moveTo(x + 400, y - 90, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("greencir.jpg", confidence = .7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = process_response(get_message())
                
                post_response(processed_message)
                sleep(10)

            else:
                print("No messages")
                sleep(10)

        except(Exception):
            print("No new messages")





check_for_new_messages()
#processed_message = process_response(get_message())
#post_response(processed_message)
