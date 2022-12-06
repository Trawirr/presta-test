from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import string

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://127.0.0.1")

for i in range(10):
	categories = driver.find_elements_by_class_name("dropdown-item")
	categories = [c for c in categories if c.text]

	if i < 5:
		categories[0].click()
	else:
		categories[1].click()
	products = driver.find_elements_by_class_name("product-title")

	if i < 5:
		print(f"Added product {products[i].text}")
		products[i].click()
	else:
		print(f"Added product {products[i-5].text}")
		products[i].click()

	# Add to cart
	add_btn = driver.find_element_by_class_name("add-to-cart")
	add_btn.click()

	time.sleep(1)
	driver.get("http://127.0.0.1")
	continue

time.sleep(2)
cart_counter = driver.find_element_by_class_name("cart-products-count")
print("Items:", cart_counter.text)

cart_btn = driver.find_element_by_class_name("header")
cart_btn.click()

print("Deleting 1 item")

remove_btn = driver.find_element_by_class_name("remove-from-cart")
remove_btn.click()
time.sleep(2)
cart_counter = driver.find_element_by_class_name("cart-products-count")
print("Items:", cart_counter.text)

driver.get("http://localhost/index.php?controller=order")

# Mr
mr = driver.find_element_by_id("field-id_gender-1")
mr.click()
print("Mr", mr.is_selected())

# Random string
letters = string.ascii_lowercase
rand_str = ''.join(random.choice(letters) for i in range(8))

print("User fields:")

# First Name
first = driver.find_element_by_id("field-firstname")
first.click()
first.send_keys(rand_str)
print("First:", first.get_attribute("value"))

# Last Name
last = driver.find_element_by_id("field-lastname")
last.click()
last.send_keys(rand_str)
print("Last:", last.get_attribute("value"))

# Email
email = driver.find_element_by_id("field-email")
email.click()
email.send_keys(f"{rand_str}@biznes.com")
print("Email:", email.get_attribute("value"))

# Password
password = driver.find_element_by_id("field-password")
password.click()
password.send_keys("qwerty")
print("Password:", password.get_attribute("value"))

# Checkboxes
c1 = driver.find_element_by_name("customer_privacy")
c1.click()
c2 = driver.find_element_by_name("psgdpr")
c2.click()

continue_btn = driver.find_element_by_name("continue")
continue_btn.click()
time.sleep(2)

# Address
addr = driver.find_element_by_id("field-address1")
addr.send_keys("Mikolaja Reja 1")

# Postal code
pcode = driver.find_element_by_id("field-postcode")
pcode.send_keys("82-300")

# City
city = driver.find_element_by_id("field-city")
city.send_keys("Gdansk")

continue_btn = driver.find_element_by_name("confirm-addresses")
continue_btn.click()

# Delivery - zmienic opcje?
delivery = driver.find_element_by_id("delivery_option_1")
#delivery.click()
driver.execute_script("arguments[0].click()", delivery)

continue_btn = driver.find_element_by_name("confirmDeliveryOption")
continue_btn.click()

# Payment - zmienic opcje?
payment = driver.find_element_by_id("payment-option-2")
driver.execute_script("arguments[0].click()", payment)

# Terms
terms = driver.find_element_by_id("conditions_to_approve[terms-and-conditions]")
driver.execute_script("arguments[0].click()", terms)

# Place order
div = driver.find_element_by_id("payment-confirmation")
order_btn = div.find_element_by_tag_name("button")
order_btn.click()

driver.get("http://localhost/index.php?controller=history")
rows = driver.find_elements_by_css_selector("tr")
print("Orders:")
for row in rows:
	print(row.text)

driver.quit()
