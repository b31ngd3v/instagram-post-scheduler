import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui


x = 0

def post():
    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')  # Find the username bar
    passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

    username = 'USERNAME'  # Enter your username here
    password = 'PASSWORD'  # Enter your password here
    file_path = r"C:\Users\P Sinha\Desktop\Capture.png"  # File Path Where Pic/Vid is Stored That You Want To Upload

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    cncel_btn = browser.find_element_by_class_name('cmbtv')  # Cancel Button

    cncel_btn.click()

    time.sleep(2)

    not_now_btn = browser.find_element_by_class_name('mt3GC')  # Not Now button

    not_now_btn.click()

    time.sleep(1)

    upld_pic_btn = browser.find_element_by_xpath(
        '//div[@class="q02Nz _0TPg"] [@data-testid="new-post-button"] [@role="menuitem"] [@tabindex="0"]')  # New Post Button
    upld_pic_btn.click()

    time.sleep(5)

    pyautogui.write(file_path)
    pyautogui.press('enter')

    time.sleep(7)

    #expnd_btn = browser.find_element_by_class_name('pHnkA')
    #expnd_btn.click()

    #time.sleep(1)

    nxt_btn = browser.find_element_by_class_name('UP43G')
    nxt_btn.click()

    time.sleep(2)

    caption = 'Hi There, P Sinha this side !'  # Write Your Caption Here

    cptn = browser.find_element_by_class_name('_472V_')
    cptn.send_keys(caption)
    pst_btn = browser.find_element_by_class_name('UP43G')
    pst_btn.click()

    time.sleep(15)  # Upload Time, it depends on your file size and internet speed

    browser.quit()

    print('''
    Successfully Uploaded!

    Python Program by
      ___   ___ _      _         
     | _ \ / __(_)_ _ | |_  __ _ 
     |  _/ \__ \ | ' \| ' \/ _` |
     |_|   |___/_|_||_|_||_\__,_|

    Follow me on Instagram @sinha.py 
    
    Github @sinhapy
    ''')
    x += 1


timee = "21:44"  # Specific Time When The Post will be Posted

schedule.every().day.at(timee).do(post)

try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    print('')
