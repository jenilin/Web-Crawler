import requests
import time
from bs4 import BeautifulSoup

def get_web_page(url):
    resp = requests.get(url = url)

    if resp.status_code != 200: # HTTP status code 200 OK 請求成功
        print("fail to get:", resp.url)
        return None
    else:
        return resp.text



def get_car(dom):
    
    # 解析 html dom 架構
    soup = BeautifulSoup(dom, "html.parser")
    # print(soup.prettify())
    results = soup.find_all("div","msgbox")
    ohno = "<div class=\"msgbox\">目前尚未有任何限量特惠!!!!!</div>"
    car = True
    for result in results:
      # print(result)
      # print(ohno)
      if str(result) == ohno:
        # print(ohno)
        car = False
        break
    return car

def line_notify(car):

    msg = ""

    if car:
        msg = "欸欸有車了快訂！！ https://www.avis-taiwan.com/limited-offer.php"
    else:
        msg = "哭哭，還是搭高鐵吧！"
    
    headers = {
    "Authorization": "Bearer " + "line notify token",
    "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
    print(r.status_code)



while (True):
    
    webPage = get_web_page('https://www.avis-taiwan.com/limited-offer.php')
    car = get_car(webPage)
    line_notify(car)
    
    time.sleep(300)