from addresses import email_remetente, senha_email
print (email_remetente)
print (senha_email)

import io
from pywhatkit import sendwhatmsg_instantly
import pyautogui


phone_no = "+55 11949614147"

message = io.open("personalized_messages/Letícia.txt", mode="r", encoding="utf-8").read()
sendwhatmsg_instantly(phone_no, message, wait_time = 20, tab_close = True, close_time = 60)
