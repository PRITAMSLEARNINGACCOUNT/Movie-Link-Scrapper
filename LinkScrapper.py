from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# from RefinedLink import Refined_Link

chrome_options = Options()
chrome_options.add_argument("--headless=new")


def Refined_Link(String):
    String_Array = String.split("/")
    # print(String_Array)
    String_Array[2] = "new5.gdtot.dad"
    String = "/".join(String_Array)
    # print(String)
    return String


def FetchingLinks(link):
    Main_Links = []
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    try:
        Elements = driver.find_elements(By.CSS_SELECTOR, ".view-well a")
        if len(Elements) == 0:
            raise Exception

        for i in Elements:
            attribute = i.get_attribute("href")
            if attribute.__contains__("gdtot"):
                attribute = Refined_Link(attribute)
            Main_Links.append(attribute)
        driver.close()
        return Main_Links

    except:
        Element = driver.find_element(By.CSS_SELECTOR, ".submit-captcha button")
        original_window = driver.current_window_handle
        Element.click()
        time.sleep(1)
        driver.switch_to.window(original_window)
        time.sleep(1)

        Elements = driver.find_elements(By.CSS_SELECTOR, ".view-well a")
        # print(Elements)
        for i in Elements:
            attribute = i.get_attribute("href")
            if attribute.__contains__("gdtot"):
                attribute = Refined_Link(attribute)
            Main_Links.append(attribute)
        driver.close()
        return Main_Links


def FindingQuality():
    UserSearch = input("Which Movie Do You Want To Download (Please Mention The Year Name Also)??? \n")
    Links = {
        "480p": [],
        "720p": [],
        "1080p": []
    }

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"https://mlsbd.shop/?s={UserSearch}")
        element = driver.find_element(By.CSS_SELECTOR, ".recent-container")
        link = element.find_element(By.CSS_SELECTOR, ".single-post > .thumb > a").get_attribute("href")
        driver.close()

        time.sleep(1)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)
        ele = driver.find_elements(By.CSS_SELECTOR, ".Dbtn")
        for i in ele:
            # Links.append(i.get_attribute("href"))
            if i.get_attribute("innerHTML").__contains__("480p"):
                Links["480p"].append(i.get_attribute("href"))
            elif i.get_attribute("innerHTML").__contains__("720p"):
                Links["720p"].append(i.get_attribute("href"))
            elif i.get_attribute("innerHTML").__contains__("1080p"):
                Links["1080p"].append(i.get_attribute("href"))
        driver.close()
        time.sleep(1)

        for i in Links:
            print(i)
            if len(Links[i]) == 0:
                continue
            print(FetchingLinks(Links[i][0]))
            # print("\n")

    except:
        print("Some Error Occured")


if __name__ == '__main__':
    # print(FindingQuality())
    FindingQuality()
