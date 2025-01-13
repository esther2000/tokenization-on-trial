from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tqdm

driver = webdriver.Chrome()
MAX_PAGES = 103

for lang in ["kl-GL", "da"]:
    links = []
    print(f"Working on language: {lang}")
    driver.get(f"https://nalunaarutit.gl/search?sc_lang={lang}")
    time.sleep(1)
    elems = driver.find_elements(By.TAG_NAME, "a")
    links.append([elem.get_attribute("href") for elem in elems])

    for i in tqdm.tqdm(range(1, 102)):
        next = driver.find_element(By.LINK_TEXT, str(i+1))
        next.click()
        time.sleep(2)
        elems = driver.find_elements(By.TAG_NAME, "a")
        links.append([elem.get_attribute("href") for elem in elems])

    with open(f"links-{lang}.txt", "w+") as outfile:
        for l in [l for xl in links for l in xl]:
            outfile.write(f"{l}\n")
