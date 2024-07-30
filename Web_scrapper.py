from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

myurl = 'https://www.shoppersstop.com/men-clothing/c-A1010'
driver.get(myurl)

time.sleep(5)

containers = driver.find_elements(By.CSS_SELECTOR, "li.pro-box")

filename = "shoppersstop_mens_clothing.csv"
with open(filename, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Product Code", "Price", "Sizes"])

    for container in containers:
        title = container.get_attribute("data-product-name")
        product_code = container.get_attribute("data-product-code")
        price = container.get_attribute("data-product-price")
        sizes = container.get_attribute("data-product-sizes")

        if sizes is not None:
            sizes = sizes.strip("[]")
            sizes_list = [size.strip() for size in sizes.split(",")]
            sizes_str = ", ".join(sizes_list)
        else:
            sizes_str = ""

        writer.writerow([title, product_code, price, sizes_str])

print("Data has been written to shoppersstop_mens_clothing.csv")

driver.quit()
