Instagram Post Scheduler
========
<a href="https://www.instagram.com/sinha.py/"><img src="https://miro.medium.com/max/1400/1*zR-cuwIFJOpQjLHExqrFkA.png" alt="Auto Post"/></a>

## IMPORTANT NOTES

* If Your Photo Does Not Fit to the screen, You Can Use This Feature Called expand, to Use This Feature Just Unmute Below Lines:

1)  `#expnd_btn = browser.find_element_by_class_name('pHnkA')` [line:55]

2)  `#expnd_btn.click()` [line:56]

3)  `#time.sleep(1)` [line:58]

## Before Running `scheduler.py`

* Open scheduler.py File and Edit The Following Lines:

1) `username = 'USERNAME'  # Enter your username here` [line:23]

2) `password = 'PASSWORD'  # Enter your password here` [line:24]

3) `file_path = r"C:\Users\P Sinha\Desktop\Capture.png"  # File Path Where Pic/Vid is Stored That You Want To Upload` [line:25]

4) `timee = "21:44"  # Specific Time When The Post will be Posted` [line:92]

5) `caption = 'Hi There, P Sinha this side !'  # Write Your Caption Here` [line:65]

Ensure that you have Chrome installed and the
[`chromedriver` ](https://chromedriver.chromium.org/downloads) that matches
your Chrome version available on your `$PATH`. You may have to update this from time to time.

## Requirements
 
* [Python](https://www.python.org/)
* `python` on the PATH
* [The Requests Library](http://python-requests.org) for Python: `pip install requests`
* Install Selenium:

```bash
pip install selenium
```
* Install Schedule:

```bash
pip install schedule
```
* Install pyautogui:

```bash
pip install PyAutoGUI
```

## Run

* Run the program using:

```bash
python scheduler.py
```

Buy Me a Coffee
----

<a href="https://www.buymeacoffee.com/b31ngD3v" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height=60px width=217px></a>
