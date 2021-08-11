# stock-boards
 a stock checker for longboard parts 🛹
 
 ## Pre-requisites
 ---
 * python3 🐍
 * `pip install requests`
* `pip install python-pushover`
* an OCI account (optional)
* a raspberry pi (optional)

## Installation
---
#### Install the packages via Docker 🐳

1. Run an interactive python 3.8 container (search it up)

2. Run `pip install requests`

3. Run `pip install python-pushover`

#### Configure the files ⚙️

1. Replace the user token and application token with your
actual pushover user token and pushover application token in the python files

1a. If you would rather not use pushover you may delete the `sendMessage()` function
all mentions of it, and `import python-pushover` without any issues

2. Go to the python files and configure your inventory checker by
using inspect element on your desired pages and finding the difference between
an in stock item and an out of stock one (see the files for examples)

2a. If all items on a page are out of stock or you simply can't find the out of stock mention, download
the html of the website and use `HTMLread()` to check if the html file is different (check files for example)
**(note: this might cause you to get unwanted notifications)**

#### RUN IT 🏃‍♂️
1. Run `python3 <filename>`, and press CTRL+C to terminate it once finished

#### Running Remotely
1. You can run this on a Raspberry Pi to not use your PC constantly OR
2. You can use a free cloud instance to run it (I use OCI, which is my preferred cloud compute service)
