# instagram-follow-bot
A python script that follow Instagram account with bots

[![GitHub followers](https://img.shields.io/github/followers/Gunthersuper?label=Follow&style=social)](https://github.com/Gunthersuper)
[![streamlabs](https://img.shields.io/badge/Donate-%241-red)](https://streamlabs.com/gunther2/tip)

**Requirements:**
1. Python (+ selenium package)
2. Instagram accounts - bots that will follow a targered instagram profile.

**Installing:**
1. Install Python - https://www.python.org/
2. Install Selenium: open the console (PowerShell or CMD for windows), type: `pip install selenium`
3. Download this repo. Click `Code` -> `Download Zip`. Unpack this to any location.
4. Download the chromedriver from here - https://chromedriver.chromium.org/downloads. Choose your current chrome version. Put downloaded `chromedriver.exe` file to the script folder.
5. Put your bot instagram accounts to `bots.txt`

**Using:**
1. Open `direct_bot.py` using any text editor.
2. Set the targered profile in the `target_profile` parameter.
3. Open the console (powershell or cmd) in the folder with the `direct_bot.py` file
4. Enter in the console: `py direct_bot.py` and wait when all bots will follow the target.

***Using this script you can get such messages:***

``[username] already follows "target"``  if this bot with `username` followed the `target` before.

`` [username] successfully follow "target"``  if bot successfully followed `target` using this script.

`` [username] didnt follow "target"``  if something went wrong. Inscrease delay time between all actions.
