"""
how are you? i hope you all are well. in this program you will get corona virus latest update from
WHO website. in this program i will use five python mode
1.webbrowser
2.time
3.pyscreenshot
4.os
5.pyautogui
"""
import webbrowser
import pyscreenshot as ImageGrab     #pip install Pillow pyscreenshot
import os
import pyautogui # pip install pyautogui
import os 
import time
def website():
    """
    this function is use to open website.
    """
    url="https://covid19.who.int/region/emro/country/"+ country
    webbrowser.open(url)
def global_update():
    url="https://covid19.who.int"
    webbrowser.open(url)
def due_to_internet():
    """" 
    This is due to the speed of internet in Asia the speed of internet 
    is slow.
    """
    time.sleep(10) #code Sleep for 10 seconds
def screenshot():
    """
    This function is used to save the screenshot
    """
 # for taking screenshot
    localtime = time.asctime( time.localtime(time.time()) )
    filename=f"covid-19 {country} {localtime}.png"
    im = ImageGrab.grab(backend="mss", childprocess=False)    
    im.save(filename)

def scroll_down():
    """
    This function is use to scroll down the wed page.
    """
 # used for scrol down the web page
    pyautogui.press('down',presses=1,interval=0.1)
def get_country():
    ex_country="Enter your country shortcuts for search your country\nlike pk for Pakistan,us for United Sate\ngb for The United Kingdom,in for India etc"
    print(ex_country)
    print(" AND for getting global updates enter g:")
    global country
    country=input()
    country=country.lower()
more_search="y"
while(True):
    if(more_search=="y"):
        get_country()
        if (country=="g"):
            global_update()
            country="Global"
        else:
            website()
        country=country.upper()
        due_to_internet()
        scroll_down()
        screenshot()
        more_search="n"
    else:
        print("Thanks for using ❤️ .\n powered by Amish.")
        break
    print(f"The screenshot of {country.upper()} was save in your working directory.")
    more_search=input("Enter y for checking other country covid-19 data else n:")
