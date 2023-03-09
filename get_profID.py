from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1258")

# find show more button
# load_more = driver.find_element(
#     By.XPATH, "//*[@id='root']/div/div/div[4]/div[1]/div[1]/div[4]/button")

# each time the button is clicked 8 more professors are loaded
# can stop the loop after some number of iterations

# while {some condition}:
# load_more.click()
# driver.implicitly_wait(0.5)

# soup = bs(driver.page_source, "html.parser")
# profs = soup.find_all("div", {"class": lambda x: x and x.startswith("TeacherCard")})
# ids = []
# for prof in profs:
#     link = prof["href"]
#     ids.append(link[link.find("?tid=")+4:])
