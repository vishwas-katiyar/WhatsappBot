'''import pymongo
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://Whatsapp_Analyser_DB:Whatsapp_Analyser_DB@cluster0.brk0t.mongodb.net/Whatsapp_Analyser_DB?retryWrites=true&w=majority")
mydb = myclient["Whatsapp_Analyser_DB"]
admin_colection=mydb['Admin_DB']
colection = mydb["Generaldiscussiongroup"]
admin_colection = mydb["Admin_Collection"]


# admin_update = list(colection.find())

# print(admin_update)
# df=colection.find({})
df = pd.DataFrame(list(colection.find()))
    
print(df)

'''

# from twilio.rest import Client

# account_sid = os.environ['ACCOUNT_SID']
# auth_token =  os.environ['auth_token']
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                                     body='Hello there!',
#                                     from_='whatsapp:+14155238886',
#                                     # body='loll',
#                                     to='whatsapp:+7898869692'
#                                 )

# print(message.sid)

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")

browser=webdriver.Chrome(
    options=gChromeOptions)

browser.get("https://www.python.org/")
time.sleep(3)
a=browser.get_screenshot_as_base64()
print(a)
print(type(a))
browser.close()