from gettext import translation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

print("How many words you want to translate: ")
numberOfTranslation = input()

#CSV is located
csv_data = pd.read_csv("csv file path here")
csvList = csv_data.values.tolist()


#csv is merged in a one big string with commas seperating them
keywordList = []

for i in csvList:
    #print(i)
    for x in i:
        x = "the " + x
        keywordList.append(x.strip(";"))

firstXKeyword = keywordList[:int(numberOfTranslation)-1]
#print(firstTenKeyword)
#print(keywordList)

#Google Chrome Driver Initialization
PATH = "file path here"
driver = webdriver.Chrome(PATH)
driver.get("translation website link here")


#enters the input(english) word to Google Translate
def search_and_type(html_element, search_keyword, wait_time, answer_html, output_list):
    search_bar = driver.find_element(By.TAG_NAME, html_element)
    search_bar.send_keys(search_keyword)

    try:
        answer_element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, answer_html))
        )
        
        output_list.append(answer_element.text) 
        driver.back()

    except:
        print("error")


translation_list = ["the car"]
endDict = {}


#loops through the input LIST and matches them in a DICTIONARY
for i in range(len(firstXKeyword)):
    search_and_type("textarea", firstXKeyword[i], 20, "ryNqvb", translation_list)
    print(translation_list)
    time.sleep(5)

    endDict[firstXKeyword[i]] = translation_list[i]

#print(translation_list)
print("\n")
print(endDict)
print("\n")

#creates a dataframe from the end product DICTIONARY
end_datas = pd.DataFrame.from_dict(endDict, orient='index')
print(end_datas)
os.makedirs("output path here", exist_ok=True)
end_datas.to_csv("output path here")

driver.quit()

