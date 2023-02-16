from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://****/wordpress/wp-login.php"
driver = webdriver.Chrome()
driver.get(url)


try:
    # driver.find_element("name","log").send_keys("admin")
    driver.find_element(By.NAME, "log").send_keys("admin")

    driver.find_element("id", "user_pass").send_keys("admin")
    driver.find_element("name", "wp-submit").click()

    title = driver.title
    # print(title)
    if (title == "Dashboard ‹ School — WordPress"):
        print("Logged In Successfully")``
    else:
        print("Username or Passwrod Error!")

    driver.execute_script("alert('Day 58 Of Learning Python ')")

except :
    print("Error Occur. Check your code")

input("Press enter to quit the browser")
driver.quit()





