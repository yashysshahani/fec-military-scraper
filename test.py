import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# %%
# preparing csv file to store parsing result later
writer = csv.writer(open("testing.csv", "w"))
writer.writerow(["name", "job_title", "schools", "location", "ln_url"])

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/")

driver.find_element(By.XPATH, '//a[text()="Sign in"]').click()
sleep(0.5)

# put your linkedin email here
username_input = driver.find_element(By.NAME, "session_key")
username_input.send_keys("yashshahani@live.com")

# put your linkedin password here
password_input = driver.find_element(By.NAME, "session_password")
password_input.send_keys("stanford")
password_input.send_keys(Keys.RETURN)

# click on the sign in button
# we're finding Sign in text button as it seems this element is seldom to be changed

# ------ list linkedin profile
profile_urls = []  # To store the Profile URLs
text = 'site:linkedin.com/in/ AND "python developer" AND "San Francisco"'

query = "https://google.com/search?q=" + text

# Get all linkedin profile url from the first page of google result
response = requests.get(query)
soup = BeautifulSoup(response.text, "html.parser")
for anchor in soup.find_all("a"):
    url = anchor["href"]
    if "https://www.linkedin.com/" in url:
        url = url[7 : url.find("&")]
        profile_urls.append(url)


# visit each profile in linkedin and grab detail we want to get
for profile in profile_urls:
    driver.get(profile)
    sleep(1)

    try:
        soup2 = BeautifulSoup(driver.page_source, "html.parser")

        # get name
        target_name = soup2.find(
            "li", {"class": "inline t-24 t-black t-normal break-words"}
        )
        name = target_name.get_text().strip()

        # get job title
        target_job_title = soup2.find(
            "h2", {"class": "mt1 t-18 t-black t-normal break-words"}
        )
        job_title = target_job_title.get_text().strip()

        # get education
        target_schools = soup2.find_all(
            "li",
            {
                "class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"
            },
        )
        school = ""
        for target_school in target_schools:
            school += target_school.h3.text.strip() + ","

        school = school.rstrip(",")

        # get location
        target_location = soup2.find(
            "li", {"class": "t-16 t-black t-normal inline-block"}
        )
        location = target_location.get_text().strip()

        writer.writerow([name, job_title, school, location, profile])
    except Exception as e:
        pass


driver.quit()
