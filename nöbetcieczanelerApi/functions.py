
import requests
from bs4 import BeautifulSoup as bs
import json


def getEczane(il: str = ...) -> str:
    __requests = requests.get(url=f"https://saglikagi.net/eczane/?il={il}")
    liste = []
    if __requests.status_code == 200:
        parse = bs(__requests.content, "lxml").find("div", class_="nkbd-left")
        name = parse.find_all("div", class_="nkbd-in-head")
        address = parse.find_all("div", class_="nkbd-in-body")
        number = parse.find_all("div", class_="nkbd-in-body-right")
        for address, name, phones in zip(address, name, number):
            addressValue = (address.find("p").text)
            nameValue = str(name.text).strip()
            numberValue = str(phones.find_all("a")[1].getText()).strip()
            liste.append(json.loads(json.dumps({
                "address":str(addressValue),
                "name":nameValue,
                "number":str(numberValue)
            },)))
    
    return (liste)



