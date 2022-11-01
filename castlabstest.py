import time

from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setting up logs and driver
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome('C:/Users/grayb/Desktop/castlabs/chromedriver.exe', desired_capabilities=d)

"""
1) Go to demo.castlabs.com
"""
driver.get("https://demo.castlabs.com/")

"""
2) Play 'HLS - HLS Clear' by clicking on the stream.
3) The browser opens with the details of the video.
"""
hls_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='HLS']")))
hls_button.click()

"""
4) Seek to 70% of the video duration.
"""
#Sleep before player will start playing
time.sleep(1)

#Clicking on player to reveal the timeline
player = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "player-container")))
player.click()

#Finding the timeline and slider
timeline = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "pp-ui-clickable")))
slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                              "3]/div/div[1]/div/div[4]")))


#Getting the slider width and performing drag and drop slider from the starting position to 70% (0,7 of width)
ActionChains(driver).drag_and_drop_by_offset(slider, 0.7 * timeline.size['width'], 0).perform()

"""
5) Validate the "Player state Change" in the console logs.
"""
assert "seeking" in str(driver.get_log('browser'))

"""
6) Click the option button (three dots), click 'Videos'.
"""
#Clicking on option button
options = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                              "1]/button[4]")))
options.click()

#Clicking on 'Videos'
video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div/div["
                                              "2]/div[3]/div[1]")))
video.click()

"""
7) Select any video value eg: '960x540 @ 2.48 Mbps' and Validate the selection.
"""
#Sleep before the list unfolds
time.sleep(1)

#Selecting 960x540 @ 2.48 Mbps
video_value = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div/div[2]/div[3]/div[2]/div[4]")))
video_value.click()

#Selection validating:
assert "ratechange" in str(driver.get_log('browser'))

print("Passed!")

driver.quit()



