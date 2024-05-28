import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller

# Replace these with your own Instagram credentials and the path to your video folder
username = 'talha.developer.01@gmail.com'
password = 'Your Password'
video_folder = 'C:\\Users\\talha\\PycharmProjects\\video_automation\\output\\'
base_filename = 'Demon Slayer 2 Part '  # Base filename without the clip number
extension = '.mp4'
caption_text = '#DemonSlayer #KimetsuNoYaiba #DemonSlayerSeason2 #Anime #AnimeClip #AnimeLover #Tanjiro #Nezuko #Zenitsu #Inosuke #Hashira #DemonSlayerAnime #AnimeCommunity #AnimeFans #AnimeEdit #DemonSlayerEdit #AnimeArt #Otaku #Manga #AnimeLife #AnimeWorld #AnimeFanatic #Cosplay #AnimeInspiration #AnimeCulture #AnimeAddict #AnimeDaily #AnimeMoments #DemonSlayerFans #Ufotable #KNY'

# Initialize the WebDriver
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

keyboard = Controller()

try:
    # Open Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(4)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

    # Locate the email/username input field and input the username
    email_input = driver.find_element(By.NAME, 'username')
    email_input.send_keys(username)

    # Locate the password input field and input the password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    # Locate the login button and click it
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(10)

    # Install Chrome extension
    driver.get('https://chromewebstore.google.com/detail/easyload-upload-video-pho/elnnmjddaleoeklbolbfhagpikikkkin?hl=en')
    time.sleep(3)
    extension_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/main/div[1]/section[1]/section/div[2]/div/button')
    extension_button.click()
    time.sleep(5)

    # Reload Instagram profile page
    driver.get("https://www.instagram.com/normalguy2252/")
    time.sleep(10)

    # Loop through all video files in the folder
    for clip_number in range(60, 309):  # Adjust the range according to the number of clips you have
        video_path = os.path.join(video_folder, f"{base_filename}{clip_number}{extension}")

        # Upload video
        upload_button = driver.find_element(By.CLASS_NAME, 'inst_upldr_upload_icon')
        upload_button.click()
        time.sleep(2)

        upload_video = driver.find_element(By.CLASS_NAME, 'upload_to_video_btn')
        upload_video.click()
        time.sleep(2)

        keyboard.type(video_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)

        # Enter caption
        text_area = driver.find_element(By.ID, "inst_upldr_post_textarea")
        text_area.click()
        text_area.send_keys(caption_text)
        time.sleep(5)

        # Click share button
        share_button = driver.find_element(By.CLASS_NAME, "inst_upldr_upload_share")
        share_button.click()
        time.sleep(32)

        # Close the modal
        close_button = driver.find_element(By.CLASS_NAME, "inst_upldr_modal_close")
        close_button.click()
        time.sleep(5)

finally:
    # Close the browser
    driver.quit()
