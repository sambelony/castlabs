import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/grayb/Desktop/castlabs/chromedriver.exe"
driver = webdriver.Chrome(PATH)

"""
1) Go to demo.castlabs.com
"""
driver.get("https://demo.castlabs.com/")

try:
    """
    2) Play 'HLS - HLS Clear' by clicking on the stream.
    3) The browser opens with the details of the video.
    """
    hls_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[text()='HLS']")))
    hls_button.click()

    """
    4)Seek to 70% of the video duration.
    """
    time.sleep(1)
    player = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "player-container")))
    player.click()
    timeline = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pp-ui-clickable")))
    knob = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                                  "3]/div/div[1]/div/div[4]")))
    ActionChains(driver).drag_and_drop_by_offset(knob, 0.7*timeline.size['width'], 0).perform()

    """
    5) Validate the "Player state Change" in the console logs.
    """
    logs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[text()='Logs ']")))
    logs.click()

    """
    6) Click the option button (three dots), click 'Videos'.
    """
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                                  "1]/button[4]")))
    options.click()
    video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div/div["
                                                  "2]/div[3]/div[1]")))
    video.click()

    """
    7) Select any video value eg: '960x540 @ 2.48 Mbps' and Validate the selection.
    """
    time.sleep(1)
    video_value = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div/div[2]/div[3]/div[2]/div[4]")))
    video_value.click()

except:
    driver.quit()