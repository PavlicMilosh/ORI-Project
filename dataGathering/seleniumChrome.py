import os
import re
from time import sleep, time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dataGathering.Car import Car


def disable_stuff():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    options.add_argument("--disable-application-cache")
    options.add_argument("--incognito")
    return options


if __name__ == '__main__':

    collected_data_location = "..\\data\\cars500.csv"
    cars_number = 60
    years = range(2007, 2018)
    links_visited_all = 0

    models = {
        #"BMW": ["Series 1", "Series 3", "Series 5", "Series 6", "Series 7", "    X1", "    X3", "    X5", "    X6"],
        #"Mercedes-Benz": ["A-Klasse", "B-Klasse", "C-Klasse", "E-Klasse", "S-Klasse", "GLK-Klasse", "ML-Klasse"]
        "Audi": ["A1", "A3", "A4", "A5", "A6", "A7", "A8", "Q3", "Q5", "Q7"]}

    num = re.compile(r'[^\d.]+')
    stopwatch_start = time()


    for make in models.keys():
        for model in models[make]:
            for year in years:
                # driver
                driver = webdriver.Chrome(chrome_options=disable_stuff())
                driver.get("https://www.mobile.de/?lang=en")
                e = driver.find_element_by_id("qsdet")
                e.click()
                mainWindow = driver.current_window_handle

                # select make
                sleep(0.5)
                select = Select(driver.find_element_by_id("selectMake1-ds"))
                select.select_by_visible_text(make)

                # select year
                Select(driver.find_element_by_id("minFirstRegistrationDate-s")).select_by_visible_text(str(year))
                Select(driver.find_element_by_id("maxFirstRegistrationDate-s")).select_by_visible_text(str(year))

                # open file
                carsFile = open(collected_data_location, "a")

                driver.implicitly_wait(5)

                # select model
                Select(driver.find_element_by_id("selectModel1-ds")).select_by_visible_text(model)
                driver.find_element_by_id("dsp-upper-search-btn").send_keys(Keys.CONTROL, Keys.RETURN)

                tabs = driver.window_handles
                driver.switch_to.window(tabs[-1])
                searchWindow = driver.current_window_handle

                # select sorting criteria
                Select(driver.find_element_by_id("so-sb")).select_by_visible_text("Newest ads first")

                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".cBox.cBox--content.cBox--resultList>div>a")))
                except TimeoutException:
                    continue

                links_visited = 0

                while links_visited < cars_number:

                    sleep(2)
                    car_links = driver.find_elements_by_css_selector('.cBox.cBox--content.cBox--resultList>div>a')
                    print("Car links size: " + str(len(car_links)))

                    for car_link in car_links:

                        if links_visited % 20 == 0:
                            print("Visited " + str(links_visited) + " links on the page in " + str(time() - stopwatch_start) + " s")
                            print("Visited " + str(links_visited_all) + " links in " + str(time() - stopwatch_start) + " s")

                        if links_visited > cars_number:
                            break

                        try:
                            car_link.send_keys(Keys.CONTROL, Keys.RETURN)
                        except StaleElementReferenceException:
                            print("\t! Detached link")
                            continue

                        tabs = driver.window_handles
                        driver.switch_to.window(tabs[-1])

                        # collect car data

                        car = Car()
                        car.make = make
                        car.model = model

                        try:
                            WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.ID, "rbt-cubicCapacity-v")))
                            WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.ID, "rbt-mileage-v")))
                            WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.ID, "rbt-firstRegistration-v")))
                            WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.ID, "rbt-power-v")))
                            WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "rbt-prime-price")))
                        except TimeoutException:
                            print("\t! Car attributes exception")
                            driver.close()
                            driver.switch_to.window(searchWindow)
                            continue

                        car.ccm = num.sub('', driver.find_element_by_css_selector("#rbt-cubicCapacity-v").text)
                        car.mileage = num.sub('', driver.find_element_by_css_selector("#rbt-mileage-v").text)
                        car.year = (driver.find_element_by_css_selector("#rbt-firstRegistration-v")).text[3:]
                        car.power = num.sub('', driver.find_element_by_css_selector("#rbt-power-v").text)
                        car.price = num.sub('', driver.find_element_by_css_selector(".rbt-prime-price").text)

                        carsFile.write(car.get_line() + "\n")
                        # print(str(car) )

                        driver.close()
                        driver.switch_to.window(searchWindow)

                        links_visited += 1
                        links_visited_all += 1

                    try:
                        nextPageButton = driver.find_element_by_css_selector("li.pref-next.u-valign-sub > span")
                        href = nextPageButton.get_attribute("data-href")
                        # print(href)
                        driver.get(href)
                    except NoSuchElementException:
                        break

                print("Visited links on the page: " + str(links_visited))
                print("All visited links:         " + str(links_visited_all))
                tabs = driver.window_handles
                driver.switch_to.window(tabs[-1])
                driver.close()
                driver.switch_to.window(mainWindow)

                carsFile.close()
                driver.delete_all_cookies()
                driver.quit()
                sleep(2)
