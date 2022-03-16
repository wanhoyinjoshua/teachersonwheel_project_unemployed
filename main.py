# This script will extract three data points from google search page.
#1, first name , last name and email contact
# google query string seek+unemployed+ site:www.linkedin.com/in


from selenium import webdriver
from selenium.webdriver.common.by import By
import re

import time
import csv



def extractname(title):
    x = title.split("-")

    y=x[0]
    z=y.split(" ")

    for i in range(len(z)):
        if z[i]== '':
            z.pop(i)


    firsstname= z[0]
    lastname=z[-1]


    return ([firsstname,lastname])

def extractemail(str):
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str)
    return match

driver = webdriver.Chrome()

driver.get("https://www.google.com/search?q=yahoo.com+looking+OR+seeking+OR+unemployed+site%3Anz.linkedin.com&rlz=1C1CHBF_enHK879HK879&biw=1229&bih=531&ei=sYwxYteKOf-TseMPmJyD2AQ&ved=0ahUKEwiXp9iIicr2AhX_SWwGHRjOAEsQ4dUDCA4&uact=5&oq=gmail.com+looking+OR+seeking+OR+unemployed+site%3Alinkedin.com&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQgxFYuBNgmitoA3AAeACAAdYBiAHqA5IBBTAuMi4xmAEAoAEBwAEB&sclient=gws-wiz&num=100")

time.sleep(5)



masterlist=[]
def reset (i):
    i=0;
    find(i)


def find(i):
    time.sleep(10)
    while True :

        i += 1
        print(i)

        try:
            blob = driver.find_element(By.XPATH,"(//div[@id='search']//a)[{0}]/parent::div/parent::div/following-sibling::div//div[last()]".format(i)).text
        except:
            blob = "placeholder"


        try:

            title = driver.find_element(By.XPATH,"(//div[@id='search']//a)[{0}]//h3".format(i)).text


            name=extractname(title)
            email1=extractemail(title)

            if(email1==[]):
                email1=extractemail(blob)


            firstname=name[0]
            lastname=name[1]



            details=[firstname,lastname, email1]
            print(details)
            if firstname == 'Images':
                i+=12
                continue

            masterlist.append(details)






        except Exception:
            #could be error
            try:
                driver.find_element(By.XPATH, "(//div[@id='search']//a)[{0}]//h3".format(i+1)).text
                print("error index{}".format(i+1))
                continue
            except:
                try:
                    driver.find_element(By.XPATH, "(//div[@id='search']//a)[{0}]//h3".format(i + 2)).text
                    continue
                except:
                    #click page
                    try:
                        driver.find_element(By.XPATH, "(//div[@id='search']//a)[{0}]//h3".format(i + 3)).text
                        continue
                    except:


                        try:
                            button = driver.find_element(By.XPATH,"//table//td[last()]//span[last()][normalize-space() = 'Next']")
                            #target text value
                            button.click();
                            reset(0);


                        except:
                            #format masterlist into cvs and for download
                            fields=['firstName','lastname','Email']
                            rows= masterlist
                            print(rows)

                            with open('nzyahoommail.csv', 'w',encoding='UTF8', newline='') as f:

                                # using csv.writer method from CSV package
                                write = csv.writer(f)

                                write.writerow(fields)
                                write.writerows(rows)

                            break


time.sleep(50)#give me time to complete captcha as I did not set up proxy servers to rotate ip addresses.
reset(0)








