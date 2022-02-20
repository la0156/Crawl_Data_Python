from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime 
import os, time

if __name__ == "__main__":
    data_save_file_csv = []
    urf_file_driver = os.path.join('etc','chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://covid19.gov.vn/")

    driver.switch_to.frame(1)
    target = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div")
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