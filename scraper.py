from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UNWANTED_SHIRTS = ["Documented", "Jung", "Koule", "Restom", "Orvach", "Rakami 4",
                "Wuutax", "Uilboek", "Sonra", "Zig Zag Stone Stand", "Soil Mushroom",
                "Cordialis Aurka", "Stumble", "It's Temporary", "Rodot", "Bug", "Shutterism",
                "Klembo", "Sleeping Guards", "Falt", "Bitten", "Dodecahedron", "Gehoorzaam",
                "Delirium", "Old Biker", "Brian"]

def launchBrowser():
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.kaft.com/en/teemachine")

    return driver

def main():
    driver = launchBrowser()

    driver.implicitly_wait(3)

    driver.find_element(By.XPATH, '//*[@id="cookie-policy-band"]/div/div/div[2]/a').click()
    repeatClick(driver)

    currentShirts = getShirtList(driver)

    incorrectCount = 0
    loop = True
    while loop == True:
        for item in currentShirts:
            print (item)
            if item in UNWANTED_SHIRTS:
                incorrectCount += 1

        if incorrectCount != 0:
            repeatClick(driver)
            currentShirts = getShirtList(driver)
            incorrectCount = 0
        
        else:
            loop = False


def repeatClick(driver):
    driver.find_element(By.XPATH, '//*[@id="tee-machine"]/div[2]/div[1]/div[3]/div[1]').click()
    return

def getShirtList(driver):
    currentShirts = []
    shirtList = driver.find_elements(By.CLASS_NAME, 'title')
    for item in shirtList:
        tShirtName = item.get_attribute("innerHTML").strip() 
        currentShirts.append(tShirtName)

    return currentShirts


if __name__ == "__main__":
    main()