from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from threading import Thread

target_profile = 'gunther.super'
delay = 10

def auth(browser, username, password):
	try:
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		browser.quit()

def follow(username, password, target):
	options = webdriver.ChromeOptions() 
	options.add_experimental_option("excludeSwitches", ["enable-logging"])

	browser = webdriver.Chrome(options = options, executable_path='chromedriver.exe')
	browser.set_window_size(350, 900)
	auth(browser, username, password)
	try:
		time.sleep(random.randrange(8,10))
		browser.get('https://instagram.com/' + target)
		time.sleep(random.randrange(3,6))
		try:
			browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section').find_element_by_xpath("//*[text()='Message']")
			print(f'[{username}] already follow "{target}"')
			time.sleep(random.randrange(2,4))
			browser.quit()
		except:
			browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section').find_element_by_xpath("//*[text()='Follow']").click()
			time.sleep(random.randrange(3,6))
			browser.get('https://instagram.com/' + target)
			time.sleep(random.randrange(3,6))
			try:
				browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section').find_element_by_xpath("//*[text()='Message']")
				print(f'[{username}] successfully follow "{target}"')
				time.sleep(random.randrange(2,4))
				browser.quit()
			except:
				print(f'[{username}] didnt follow "{target}"')
				time.sleep(random.randrange(2,4))
				browser.quit()
	except Exception as err:
		print(err)
		browser.quit()



f = open('bots.txt', 'r')

for line in f:
	log = line.split(':')
	follow(log[0], log[1], target_profile)
	time.sleep(delay)
	