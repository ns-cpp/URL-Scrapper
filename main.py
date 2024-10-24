from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import time


search = input("searhing dork? ( example.'details.php?id=') : ")

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # fullscreen browser 
service = Service('chromedriver.exe') 
driver = webdriver.Chrome(service=service, options=chrome_options)



driver.get("https://www.google.com")
searchBox = driver.find_element(By.NAME, "q")
searchBox.send_keys(search)
searchBox.send_keys(Keys.RETURN)
time.sleep(3)


links = []


for _ in range(5):  # Number of pages to visit
    
    search_results = driver.find_elements(By.XPATH, "//span[@jscontroller='msmzHf']/a")
    print(f"{len(search_results)} link found.")
    
    for result in search_results:
        link = result.get_attribute("href")
        if link:  
            links.append(link)
    
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  
    
    
    try:
        next_page_button = driver.find_element(By.ID, "pnnext")
        next_page_button.click()
        time.sleep(3)  
    except:
        print("Last page.")
        break


with open("links.txt", "w") as f:
    for link in links:
        f.write(link + "\n")


driver.quit()

print(f"{len(links)} link(s) saved.")
