from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def UrlGenerator(size,type,name):
    #Shoe size
    base = 530
    shoeSize = (size -4) * 20
    final = base + shoeSize
    Url = "https://www.adidas.com/us/" + name + "/" + type + "html?forceSelSize=" + type + "_" + str(final)
    print(Url)

def UrlProductGenerator(name,type):
    url = "https://www.adidas.com/us/" + name + "/" + type + ".html"
    return url


def stock(myUrl,type):
    try:
        driver = webdriver.Chrome()
        driver.get(myUrl)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add-to-bag___3wgQk")))
        username = driver.find_element_by_class_name('sizes___3Stmf wide-sizes___3shqN fractions-decoration-reset___22Rwq')
        options = username.find_element_by_tag_name('option')
        optionsList = []
        for option in options:
            optionsList.append(option.get_attribute('innerHTML'))
        for sizes in optionsList:
            if sizes.isdigit():
                print("Size " + sizes + " for " + type + " is available ")
    finally:
        driver.quit()

url = UrlProductGenerator("nmd_r1-shoes","G55575")
stock(url,"G55575")
size = int(input("Please enter your size "))
UrlGenerator(11,"G55575","nmd_r1-shoes")