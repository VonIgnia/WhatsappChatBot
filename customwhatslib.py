import time
import webbrowser as web
from datetime import datetime
from typing import Optional
from urllib.parse import quote

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()

def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhatmessage_tomultiplenumbers(
    phone_list: list,
    #message_list: list,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
    message: str = "Oi, Gi aqui, ~tô testando o script de envio automático de mensagem~ , essa mensagem *foi* enviada automáticamente, *Testes ainda são necessários*",
):
    for contact in phone_list:
        web.open(f"https://web.whatsapp.com/send?phone={contact}&text={quote(message)}")
        time.sleep(4)
        pg.click(core.WIDTH / 2, core.HEIGHT / 2)
        time.sleep(wait_time)
        pg.press("enter")
        #log.log_message(_time=time.localtime(), receiver=contact, message=message)
        time.sleep(4)
    if tab_close:
        core.close_tab(wait_time=close_time)

