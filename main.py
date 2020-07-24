from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.reddit.com/")

fname = input("enter the name of your file with .txt :")

input("login to reddit and press enter:")

f = open(fname, "r")
sublist = []

for x in f:
	sublist = f.readlines()

for i in sublist:
	search = driver.find_element_by_xpath("//*[@id='header-search-bar']")
	search.clear()
	search.send_keys(i)
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[1]/div/a/div[3]/button").click()
	print("joined: {} ".format(i))



