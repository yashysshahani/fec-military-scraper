from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
from parsel import Selector


# last name checked: freakly, benjamin c.
# note kowalski, james
# %%

# linkedin login
USERNAME = ""
PASSWORD = ""

# TAGS
army_tags = [
    r"army",
    r"usarmy",
    r"soldier",
    r"bde",
    r"usa",
    r"us arm",
    "retire",
    "retired",
]
air_force_tags = [
    r"air force",
    r"usaf",
    r"airforce",
    r"u s a f",
    r"afb",
    r"air guard",
    "retire",
    "retired",
]

# %%
# CREATE FULL NAMES LIST
file = (
    "/Users/yashshahani/Desktop/Stanford Summer 23/fec selenium/FullGenDataClean - use for FEC.xlsx - FullGenDataCl"
    "ean.csv"
)
df = pd.read_csv(file)
df = df.dropna(subset=["user_name"])
df.reset_index(drop=True, inplace=True)
df = df.fillna("")
print(df)

# name lists
first_names = [f_name for f_name in df["First"]]
middle_initials = [mi for mi in df["MI"]]
last_names = [l_name for l_name in df["Last"]]

# occupation lists
army_occupations = army_tags
air_force_occupations = air_force_tags

# full names list
full_names = []
for index in enumerate(first_names):
    full_name = ""
    if middle_initials[index[0]] != "":
        full_name = f"{last_names[index[0]]}, {first_names[index[0]]} {middle_initials[index[0]]}"
    else:
        full_name = f"{last_names[index[0]]}, {first_names[index[0]]}"
    full_names.append(full_name)
    full_name_df = pd.DataFrame(full_names)

print(full_names)

# %%
#
url = "https://www.fec.gov/data/receipts/individual-contributions/?min_date=01%2F01%2F2000&max_date=12%2F31%2F2024"

download_folder = "/Users/yashshahani/Desktop/Stanford Summer 23/fec selenium/fec files"
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}

chrome_options.add_experimental_option("prefs", prefs)

driver = Chrome(chrome_options)

# log in to linkedin
linkedin = "https://www.linkedin.com/uas/login"
driver.get(linkedin)
email = driver.find_element(By.ID, "username")
email.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)
time.sleep(3)
sel = Selector(driver.page_source)


for index in range(100, len(full_names)):
    # collect last occupation and employer from linkedin
    linkedin = df["Linkedin"][index]
    response = requests.get(linkedin)
    time.sleep(3)

    # find experience
    driver.get(linkedin)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    wait = WebDriverWait(driver, 10)
    occupation_element = soup.find(
        "h2", {"class": "mt1 t-18 t-black t-normal break-words"}
    )
    occupation = occupation_element.get_text().strip()
    if occupation:
        occupation.strip()
    print(occupation)

    employer = sel.xpath(
        '//*[starts-with(@class,"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()'
    ).extract_first()
    print(employer)
    if employer:
        employer.strip()
    print(employer)

    # fec stuff
    driver.get(url)
    search_input = driver.find_element(By.ID, "contributor_name")
    occupation_input = driver.find_element(By.ID, "contributor_occupation")
    employer_input = driver.find_element(By.ID, "contributor_employer")
    service = df["Service"][index]

    search_input.clear()
    search_input.send_keys(full_names[index])
    search_input.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    if service == "Army":
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "contributor_occupation")))
        for occupation in army_occupations:
            occupation_input.clear()
            occupation_input.send_keys(occupation)
            occupation_input.send_keys(Keys.RETURN)
        occupation_input.send_keys(employer)
        occupation_input.send_keys(Keys.RETURN)
        occupation_input.send_keys(occupation)
        occupation_input.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollTo(0, 0);")
        input()
        driver.get(url)

        wait.until(EC.element_to_be_clickable((By.ID, "contributor_name")))
        search_input = driver.find_element(By.ID, "contributor_name")
        occupation_input = driver.find_element(By.ID, "contributor_occupation")
        employer_input = driver.find_element(By.ID, "contributor_employer")

        search_input.clear()
        search_input.send_keys(full_names[index])
        search_input.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        for occupation in army_occupations:
            wait.until(EC.element_to_be_clickable((By.ID, "contributor_employer")))
            employer_input.send_keys(occupation)
            occupation_input.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollTo(0, 0);")
        input()

        driver.implicitly_wait(5)

    elif service == "Air Force":
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "contributor_occupation")))
        for occupation in air_force_occupations:
            occupation_input.clear()
            occupation_input.send_keys(occupation)
            occupation_input.send_keys(Keys.RETURN)
        occupation_input.send_keys(employer)
        occupation_input.send_keys(Keys.RETURN)
        occupation_input.send_keys(occupation)
        occupation_input.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollTo(0, 0);")
        input()
        driver.get(url)
        wait.until(EC.element_to_be_clickable((By.ID, "contributor_name")))

        search_input = driver.find_element(By.ID, "contributor_name")
        occupation_input = driver.find_element(By.ID, "contributor_occupation")
        employer_input = driver.find_element(By.ID, "contributor_employer")

        search_input.clear()
        search_input.send_keys(full_names[index])
        search_input.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        for occupation in air_force_occupations:
            wait.until(EC.element_to_be_clickable((By.ID, "contributor_employer")))
            employer_input.send_keys(occupation)
            occupation_input.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollTo(0, 0);")
        input()

        driver.implicitly_wait(5)

driver.get(url)
