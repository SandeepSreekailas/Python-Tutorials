# def greet(name):
#     return f"Hello, {name}!"

# def greet1(name):
#     return f"Hiii, {name}!"


# def greet3(name):
#     return f"Hola, {name}!"



# def a():
#     num=int(input("enter a number"))
#     if num>0:
#         print("entered number is positive")
#     elif num==0:
#         print("Zero")
#     else:
#         print("entered number is negative")


import main2

print("Square root:", main2.square_root(9))

print("2 to the power of 3:", main2.power(2, 3))

print("Area of a circle with radius 5:", main2.circle_area(5))


# from bs4 import BeautifulSoup 
# import requests 

# page = requests.get("https://instagram.com")  
# soup = BeautifulSoup(page.content, 'html.parser') 

# # Title
# print("Title:", soup.title.text)

# # Body content
# print("Body:", soup.body.text)  

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time

# service = Service()
# options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.bmw.com/en/index.html")
# time.sleep(5)  # wait for JavaScript and images to load

# images = driver.find_elements(By.TAG_NAME, "img")
# for img in images:
#     print(img.get_attribute("src"))

# driver.quit()


# import pandas as pd

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#          'Age': [25, 26, 27],
#          'City': ['New York', 'Chicago', 'Los Angeles']}
# df = pd.DataFrame(data)
# print(df)



  