from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import sys

count = 11070

def createPosDataSet():
    f = open(r"cancerous genes mod.csv", "r")
    lines = f.readlines()
    f.close()

    arr = []
    i=0

    for line in lines:
        if i==0:
            i+=1
            continue
        arr.append(line[line.index(',')+1:].strip())

    arr.sort()
    print arr



def crawlDataForAllHSProteins(arr):
    global count
    chromedriver = "C:\Chrome Driver\chromedriver"
    driver = webdriver.Chrome(chromedriver)
    wait = WebDriverWait(driver, 30)

    z = 1

    for protein in arr:
        if count > 12915:
            break
        if z < count:
            z+=1
            continue
        driver.get("http://www.ebi.ac.uk/QuickGO/GProtein?ac="+protein)
        time.sleep(3)

        process = ""
        function = ""

        try:
            k = 0
            i=3
            header = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentsarea"]/div[4]/div[3]/form/div[2]/table/tbody[2]/tr[1]/td/div')))
            while(True):
                t = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentsarea"]/div[4]/div[3]/form/div[2]/table/tbody[2]/tr['+str(i)+']')))
                if t.text == "Function":
                    k = 1
                    i+=2
                    continue
                elif t.text == "Component":
                    break

                if k == 0:
                    process+= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentsarea"]/div[4]/div[3]/form/div[2]/table/tbody[2]/tr['+str(i)+']/td[6]'))).text+"\n"
                elif k == 1:
                    function+= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentsarea"]/div[4]/div[3]/form/div[2]/table/tbody[2]/tr['+str(i)+']/td[6]'))).text+"\n"

                i+=1

        except:
            process = "No Process"
            function = "No Function"

        f = open("C:\\Users\\atifh\\Desktop\\Summer Internship\\Positive Data Set Attributes\\"+protein+".txt", "w")
        f.write(process)
        f.write("\n")
        f.write(function)
        f.close()
        
        count+=1
        z+=1


def mapStRINGtoUNIPROTKB(filepath):
    f = open(filepath, "r")
    lines = f.readlines()
    f.close()

    proteins = []
    
    for line in lines:
        arr = line.split()
        if arr[0] == "9606":
            proteins.append(line[line.index('\t')+1:line.index('|')])

    return proteins


#createPosDataSet()
arr = mapStRINGtoUNIPROTKB("C:\\Users\\atifh\\Desktop\\Summer Internship\\All Proteins Database\\full_uniprot_2_string.04_2015.tsv")
try:
    crawlDataForAllHSProteins(arr)
except:
    print count
