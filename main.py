#link, dynamic name, picture, or ducuments
import pandas as pd
import webbrowser as web
import time
import pyautogui as pg

#*****************************************
Images = True
Addmore = True
ImageName = "TECHUTSAV posters_merged.jpg"
def message():
    "set the message need to send here"
    new_line()
    new_line()
    pg.typewrite("This is the content of bot")
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
    new_line()
    new_line()
    pg.typewrite("_(this is bot automated message no need to replay)_")
    new_line()
    # pg.typewrite("                                  -Bot(4.1v) 🤖 ")
    paste()
def img_click(image):
    if pg.locateOnScreen(image, confidence=0.8)!= None:
        pic = pg.locateOnScreen(image, confidence=0.8)
        x1 = pic.left
        y1 = pic.top
        print("I can see "+image+" in "+str(x1)+" "+str(y1))
        pg.moveTo(x1 + 28, y1 + 15)
        time.sleep(2)
        pg.click()
        print("Click completed...!")
        time.sleep(3)
    else:
        print("image "+image+" is not found")
        time.sleep(1)

def add_img(image):
    print("looking for target icon")
    img_click('BPpin.png')
    img_click('BPfile.png')
    pg.click()
    time.sleep(4)
    if pg.locateOnScreen('file.png', confidence=0.8) != None:
        pg.typewrite(image)
    pg.typewrite(["enter"])
    time.sleep(5)

def additional(n):
    print("looking for target icon")
    img_click('Add.png')
    time.sleep(3)

    pg.typewrite(n)
    time.sleep(1)
    pg.typewrite(["enter"])

count = 1
# to read the the message from csv file
data = pd.read_csv("victim.csv")
data_dict = data.to_dict('list')
number = data_dict['PhNumber']
messages = data_dict['Message']
combo = zip(number, messages)
print("Data is fetching...")

# start spaming the message one by one
for number, messages in combo:
    print("starting messages sequence")
    web.open("https://api.whatsapp.com/send?phone="+number+"&text="+messages)
    time.sleep(10)

    #added for two times inorder to remove run time error
    web.open("https://api.whatsapp.com/send?phone="+number+"&text="+messages)
    time.sleep(8)

    # take cursure at the end of the line
    pg.click(1290, 710)
    time.sleep(1)

    #start the content of message
    message()
    watermark()
    if Images == True:
        add_img(ImageName)
    if Addmore == True:
        additional(str(count)+".pdf")
    time.sleep(3)
    if pg.locateOnScreen('End.png', confidence=0.8) != None:
        img_click('send.png')

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
    count = count + 1