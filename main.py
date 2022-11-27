#link, dynamic name, picture, or ducuments
import pandas as pd
import webbrowser as web
import time
import pyautogui as pg

#*****************************************
def message():
    "set the message need to send here"
    new_line()
    pg.typewrite("I am Shreyas KB, IT Quiz Event Lead")
    new_line()
    new_line()
    pg.typewrite("Congratulations. You have successfully registered for IT Quiz Event. for more communication regarding the event I request you to join this group.")
    new_line()
    pg.typewrite("If you are already joined the group please ignore this message or else join with this link https://chat.whatsapp.com/KAYuC6bLqa93vucj9S7z5G")
    pg.typewrite("Have a grate day,")
    #pg.typewrite("") #text out put
    #mail.google.com  #open gmail
#*****************************************
def paste():
    "paste the text form clipboard"
    pg.keyDown("ctrl")
    pg.press("v")
    pg.keyUp("ctrl")

def tab_close():
    "to close the tab in web"
    pg.keyDown("ctrl")
    pg.press("w")
    pg.keyUp("ctrl")

def tab_switch():
    "to stich tab form whatsApp API to website"
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")

def new_line():
    "to start a new line on the whatsApp"
    pg.keyDown("shift")
    pg.typewrite(["enter"])
    pg.keyUp("shift")

def watermark():
    "to set bot watermark on the end of message"
    pg.typewrite("_(bot message no need to replay)_")
    pg.typewrite("                    -Bot(4.1v)🤖")

# to read the the message from csv file
data = pd.read_csv("leads.csv")
data_dict = data.to_dict('list')
leads = data_dict['PhNumber']
messages = data_dict['Message']
combo = zip(leads, messages)

# start spaming the message one by one
for leads, messages in combo:
    web.open("https://api.whatsapp.com/send?phone="+leads+"&text="+messages)
    time.sleep(10)

    #added for two times inorder to remove run time error
    web.open("https://api.whatsapp.com/send?phone="+leads+"&text="+messages)
    time.sleep(8)

    # take cursure at the end of the line
    pg.click(1290, 710)
    time.sleep(1)

    #start the content of message
    message()
    watermark()

    #send the message
#    pg.typewrite(["enter"])
#    time.sleep(5)

    # switch whatsApp to webbrowser
    tab_switch()
    # first redirect tab close
    tab_close()
    time.sleep(1)
    # second tab closed
    tab_close()
    time.sleep(5)
    #final sleep of iteration