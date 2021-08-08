from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username="typeYourUsernameHere"
password="typeYourPasswordHere"
# create instance of Chrome webdriver
driver = webdriver.Chrome() 
driver.get("https://twitter.com/login")

# find the element where we have to 
# enter the xpath
# fill the number or mail
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
 
# find the element where we have to 
# enter the xpath
# fill the password
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
  
# find the element log in 
# request using xpath 
# clicking on that element 
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()

time.sleep(2)

tweet = driver.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div''')
tweet.send_keys("""test-tweet - 3.08.2021""")
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()


