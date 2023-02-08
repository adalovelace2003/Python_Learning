from selenium import webdriver

# Start the browser
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://en.wikipedia.org/wiki/Hello")

# Get the current height of the page
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the page to load
    driver.implicitly_wait(20)

    # Get the new height of the page
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Check if the height has changed, if not break the loop
    if new_height == last_height:
        break
    last_height = new_height

# Get the HTML source code
html = driver.page_source

# Close the browser
driver.quit()

# Print the HTML source code
print(html)
with open("data.txt","w") as file:
    file.write(html)
