from linkedin_scraper import actions, Company,Person
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
email = "sivaannamalai169@gmail.com"
password = "sivacool"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
print("Login Successful.")

company = Company("https://www.linkedin.com/company/gaius-networks/", driver=driver, scrape=True)
print("Company details fetched successfully.")
driver.quit()

driver = webdriver.Chrome()
actions.login(driver, email, password)
persons = []

for employee in company.employees: 
    if(employee and employee['linkedin_url']):
        driver.get(employee["linkedin_url"])
        content = driver.find_element(By.CLASS_NAME, "text-heading-xlarge")
        persons.append({"name": content.text})
print(persons)
driver.quit()