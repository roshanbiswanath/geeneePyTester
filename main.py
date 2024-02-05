from selenium import webdriver
import subprocess
from fastapi import FastAPI
# Setup Firefox webdriver
# cap = DesiredCapabilities.FIREFOX
# cap["marionette"] = True
# browser = webdriver.Firefox(capabilities=cap, executable_path='path_to_geckodriver')
browser = webdriver.Firefox()
service = webdriver.FirefoxService(log_output=subprocess.STDOUT)

# Counter for refreshes
count = 0

# Open the website
browser.get('localhost:5173/tryon/')



# while True:
#     # Wait for the console log message
#     # while True:
#     #     for entry in browser.get_log('browser'):
#     #         print(entry)
#     #         if 'Done Loading' in entry['message']:
#     #             break
#     #     else:
#     #         continue
#     #     break
#     # Print the message
#     print('Done')

#     # Refresh the page
#     browser.refresh()
#     refresh_count += 1

#     # Print the refresh count
#     print(f'Refresh count: {refresh_count}')

#     # Wait a bit before next iteration
#     time.sleep(100)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/refresh")
def refresh():
    global count
    count += 1
    print(f'Refresh count: {count}')
    browser.refresh()
    return {"Refresh count": count}
