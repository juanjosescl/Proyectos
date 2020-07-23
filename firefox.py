from selenium import webdriver
from time import sleep

browser = webdriver.Firefox(executable_path=r"C:\Users\jolate\Desktop\Proyectos\geckodriver-v0.26.0-win64\geckodriver.exe")
browser.get("https://www.google.com")

print(browser)

# def prueba():w
#     webdriver driver
#     System.setProperty("webdriver.gecko.driver","C:\Users\jolate\Desktop\Proyectos\geckodriver-v0.26.0-win64\geckodriver.exe");
#     driver = new FirefoxDriver()
#     driver.get('https://youtube.com')



# prueba()





