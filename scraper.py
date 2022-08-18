from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creates a blacklist of unwanted t-shits
UNWANTED_SHIRTS = ["Documented", "Jung", "Koule", "Restom", "Orvach", "Rakami 4",
                "Wuutax", "Uilboek", "Sonra", "Zig Zag Stone Stand", "Soil Mushroom",
                "Cordialis Aurka", "Stumble", "It's Temporary", "Rodot", "Bug", "Shutterism",
                "Klembo", "Sleeping Guards", "Falt", "Bitten", "Dodecahedron", "Gehoorzaam",
                "Delirium", "Old Biker", "Brian"]

# Launches the browser 
def launchBrowser():
    options = Options()
    options.add_argument("start-maximized")

    # Keeps the browser open when the script has finished
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.kaft.com/en/teemachine")

    return driver

def main():
    driver = launchBrowser()

    # Waits 3 seconds for the browser to load all of the elements
    driver.implicitly_wait(3)

    # Finds the cookies element, which is overlaid on top of the refresh t-shirts button
    driver.find_element(By.XPATH, '//*[@id="cookie-policy-band"]/div/div/div[2]/a').click()
    
    # Clicks the refresh t-shirts button to start the search process
    repeatClick(driver)

    # Gets the names of the three shirts provided by the website
    currentShirts = getShirtList(driver)

    incorrectCount = 0
    
    # Checks if all three of the t-shirts are not in the blacklist, breaks the loop
    # the page if incorrect count = 0, refreshes the page otherwise
    while True:
        for item in currentShirts:
            print (item)
            if item in UNWANTED_SHIRTS:
                incorrectCount += 1

        if incorrectCount != 0:
            repeatClick(driver)
            currentShirts = getShirtList(driver)
            incorrectCount = 0
        
        else:
            break

# Clicks the refresh t-shirts button to start the search process
def repeatClick(driver):
    driver.find_element(By.XPATH, '//*[@id="tee-machine"]/div[2]/div[1]/div[3]/div[1]').click()
    return

# Returns the names of the three t-shirts selected by the website in a list
def getShirtList(driver):
    currentShirts = []
    
    # Finds all of the t-shirt HTML elements by their class
    shirtList = driver.find_elements(By.CLASS_NAME, 'title')
    print (shirtList)
    for shirt in shirtList:
        # Extracts the t-shirt name from the HTML elements
        tShirtName = shirt.get_attribute("innerHTML").strip() 
        currentShirts.append(tShirtName)

    return currentShirts


if __name__ == "__main__":
    main()