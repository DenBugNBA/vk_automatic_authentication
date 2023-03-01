from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from vk_auth_data import vk_login, vk_password


def authenticate_vk():
    options = webdriver.ChromeOptions()

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    )
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://vk.com/")
        # time.sleep(2)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "index_email"))
        )
        email_input.clear()
        email_input.send_keys(vk_login)
        # time.sleep(2)

        email_input.send_keys(Keys.ENTER)
        # time.sleep(2)

        switch_to_password_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "vkc__Bottom__switchToPassword"))
        )
        switch_to_password_button.click()
        # time.sleep(2)

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name = 'password']"))
        )

        # password_input.send_keys(vk_password)
        ActionChains(driver).move_to_element(password_input).send_keys(
            vk_password
        ).perform()
        # time.sleep(2)

        login_button = driver.find_element(
            By.CLASS_NAME,
            "vkuiButton",
        )
        login_button.click()

        time.sleep(10)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    authenticate_vk()
