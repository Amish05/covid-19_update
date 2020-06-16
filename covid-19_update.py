"""
how are you? i hope you all are well. in this program you will get corona virus latest update from
WHO website. in this program i will use five python module
1.webbrowser
2.time
3.pyscreenshot
4.os
5.pyautogui
"""
def website():
    """
    this function is use to open website.
    """
    import webbrowser
    url="https://covid19.who.int/region/emro/country/"+ country
    webbrowser.open(url)
def due_to_internet():
    """" 
    This is due to the speed of internet in Asia the speed of internet 
    is slow.
    """
    import time
    time.sleep(10) #code Sleep for 10 seconds
def screenshot():
    """
    This function is used to save the screenshot
    """
    import os # import os for remove the existing file
    #pip install Pillow pyscreenshot
    import pyscreenshot as ImageGrab # for taking screenshot
    filename="covid-19 "+country+".png"
    im = ImageGrab.grab(backend="mss", childprocess=False)
    if os.path.exists(filename):
        os.remove(filename)
    im.save(filename)
def scroll_down():
    """
    This function is use to scroll down the wed page.
    """
    # pip install pyautogui
    import pyautogui # used for scrol down the web page
    pyautogui.press('down',presses=1,interval=0.1)
def get_country():
    ex_country="Enter your country shortcuts for search your country\nlike pk for Pakistan,us for United Sate\ngb for The United Kingdom,in for India etc:"
    print(ex_country)
    global country
    country=input()
    country=country.lower()
more_search="y"
while(True):
    if(more_search=="y"):
        get_country()
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
