from selenium import webdriver
from selenium.webdriver.common.by import By
import time


while True:
	num = input("Выберите номер теста: 1(успешный тест) или 2(тест с ошибкой) = ")
	if num in ('1', '2'):
		break	

try:
	browser = webdriver.Chrome()
	browser.get(f"http://suninjuly.github.io/registration{num}.html")


	elem_1 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[1]/input").send_keys("Agent")
	elem_2 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[2]/input").send_keys("007")
	elem_3 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[3]/input").send_keys("Agent@007.ru")
	elem_4 = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[1]/input").send_keys("666")
	elem_5 = browser.find_element(By.XPATH, '//html/body/div/form/div[2]/div[2]/input').send_keys("Kremlin")


	button = browser.find_element(By.XPATH, "//html/body/div/form/button").click()

finally:
	time.sleep(2)
	browser.quit()