from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_add_to_basket_button(browser):
	browser.get(link)
	#for visual checking that language has changed
	#time.sleep(30)
	button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
	assert button, "Should be present 'add to basket' button"
