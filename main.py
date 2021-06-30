from fake_useragent import UserAgent
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

ua = UserAgent()
def bypass_proxy_detection(data):
    try:
        proxies = {
        "http": "socks5://" + str(data.get("ip")) + ":" + str(data.get("port")),
        "https": "socks5://" + str(data.get("ip")) + ":" + str(data.get("port"))
        }
        print("User-Agent:", ua.random)
        req = requests.get("https://haughtydropszoology.com/p137bpr9?key=dcdd242a0f4bf11fbe5cc2bce9d1673f", proxies=proxies, headers={"User-Agent": ua.random})
        print(req.text)
        if req.text == "<a href = 'http://terraclicks.com/anonymous/' target='_blank'>Anonymous Proxy detected, click here.</a>" or "500 Internal Server Error" in req.text:
            return
        else:
            print("Working:", str(data.get("ip")) + ":" + str(data.get("port")), str(data.get("country_code")))
            command(data)
    except:
        print("Passed!")
        pass
def proxy():
    tam = {}
    req = requests.get("https://www.proxyscan.io/api/proxy?type=socks5&type=elit&limit=10&last_check=500").json()
    for t in req:
        tam["ip"] = str(t.get("Ip"))
        tam["port"] = str(t.get("Port"))
        tam["country_code"] = str(t.get("Location")["countryCode"])
    yield tam
def command(ata):
                    options = webdriver.FirefoxOptions()
                    #options.add_argument("--headless")
                    profile = webdriver.FirefoxProfile()
                    profile.set_preference("browser.privatebrowsing.autostart", 1)
                    #webdriver.DesiredCapabilities.FIREFOX["proxy"] = {
                    #"proxyType": "manual",
                    #"httpProxy": ip_str,
                    #"ftpProxy": ip_str,
                    #"sslProxy": ip_str
                    #}
                    profile.set_preference("network.proxy.type", 1)
                    profile.set_preference("network.proxy.socks", str(ata.get("ip")))
                    profile.set_preference("network.proxy.socks_port", int(ata.get("port")))
                    profile.set_preference("general.useragent.override", ua.random)
                    profile.update_preferences()
                    driver = webdriver.Firefox(options=options, firefox_profile=profile)
                    k = time.localtime()
                    #http://tun.fast-page.org/?to=https://haughtydropszoology.com/p137bpr9?key=dcdd242a0f4bf11fbe5cc2bce9d1673f&view=2
                    #https://haughtydropszoology.com/p137bpr9?key=a969ca5c9ad2611762f11b79a526e2d2&submetric=15548089
                    driver.get("http://tun.fast-page.org/?to=https://haughtydropszoology.com/p137bpr9?key=dcdd242a0f4bf11fbe5cc2bce9d1673f&view=2")
                    driver.delete_all_cookies()
                    print("User-Agent:", driver.execute_script("return navigator.userAgent;"))
                    print(driver.page_source)
                    time.sleep(5)
def get():
    for _81l1nm1y0r_ in proxy():
        print("Selected ip address:", str(_81l1nm1y0r_.get("ip")) + ":" + str(_81l1nm1y0r_.get("port")))
        bypass_proxy_detection(_81l1nm1y0r_)
while True:
    get()
