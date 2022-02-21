from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os

# 1. Khai bao bien browser
urf_file_driver = os.path.join('etc','chromedriver.exe')
browser = webdriver.Chrome(ChromeDriverManager().install())

# 2. Mở thử một trang web
browser.get("https://accounts.google.com/signin/v2/identifier?hl=vi&passive=true&continue=http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F8494%3Fhl%3Dvi%26co%3DGENIE.Platform%253DDesktop&ec=GAZAdQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("kanot78611@ishop2k.com")

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("fwetwt")

# 2b.Submit form

txtPass.send_keys(Keys.ENTER)

# 3. Dừng chương trình 5 giây
sleep(5)

# 4. Đóng trình duyệt
browser.close()