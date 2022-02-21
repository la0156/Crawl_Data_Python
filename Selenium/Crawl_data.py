from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os

def LoginServer():
    urf_file_driver = os.path.join('etc','chromedriver.exe')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("")

    txtUser = browser.find_element_by_id("email")  #id của tài khoản
    txtUser.send_keys("kanot78611@ishop2k.com")    #thông tin tài khoản

    txtPass = browser.find_element_by_id("pass")    #id của mật khẩu
    txtPass.send_keys("fwetwt")                     #mật khẩu trang web cần crawl
# 2b.Submit form
    txtPass.send_keys(Keys.ENTER)
# 3. Dừng chương trình 5 giây

def crawl_data():
    LoginServer()
    driver.switch_to.frame(1)
    target = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div")  #xpath của cái phần crawl
    for data in target:
        cities = data.find_elements_by_class_name("city")
        totals = data.find_elements_by_class_name("total")
        todays = data.find_elements_by_class_name("daynow")
        deads = data.find_elements_by_class_name("die")

    list_cities = [city.text for city in cities]
    list_total = [total.text for total in totals]
    list_today = [today.text for today in todays]
    list_dead = [dead.text for dead in deads]

    for i in range(len(list_cities)):
        row = "{},{},{},{}\n".format(list_cities[i], list_total[i], list_today[i], list_dead[i])
        data_save_file_csv.append(row)
    
    today_ = (datetime.datetime.now()).strftime("%Y%m%d")
    filename = f"{today_}.csv"
    with open(os.path.join("data", filename), 'w+', encoding='utf-8') as f:
        f.writelines(data_save_file_csv)
    
    driver.close()
    

