import time
import mechanize
from mechanize import Browser
import re
import os

#Captive Portal or Login URL of your WiFi
while(True):
    url = 'http://192.168.70.1:8002/index.php?zone=mitrc&redirurl=http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204' 

    br = Browser()
    status = br.open(url).code
    # print(status)

    if (status==200):
        print("Captive Portal loaded successfully \nResponse code: 200")

    else:
        print("\nSomething went wrong \n Response Code :",status)


    pg=mechanize.Browser()
    pg.set_handle_robots(False)
    r=pg.open(url)
    
    #form id
    pg.select_form(nr=0)
    
    #Your username and password
    pg.form["auth_user"] = input("Username: ")
    pg.form["auth_pass"] = input("Password: ")
    
    pg.method="POST"
    r=pg.submit()
    pageAsaString = str(r.read())



    match = re.search('Logout',pageAsaString)
    if match:                      
        print ("\nYo're Connected to WiFi\n===============Enjoy Wifi==============")
    else:
        print ("\nIncorrect username or password !")

    #Clear Screen Function
    def clear():
     if os.name == 'nt':
        _ = os.system('cls')
     else:
        _ = os.system('clear')

    # Time in Seconds (In howmuch time you want to auto re-login)
    t = '10'

    # Define function
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Auto Re-Login in: ",timer, end="\r")
            time.sleep(1)
            t -= 1
    #  Function call
    countdown(int(t))

    time.sleep(5)
    clear()
