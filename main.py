from ChromeAutomation import Chrome
import http.client as http
import time
import os
from PrintEffects import inform, warning, successful, error

# Please run 'pip install -r requirements.txt' in the terminal to install the
# proper modules.

# Must be the same version as the chrome version installed on your system.
# https://chromedriver.chromium.org/downloads
chrome_driver = "PATH_TO_CHROME_DRIVER"

creds = {
        "username": "YOUR USERNAME",
        "password": "YOUR PASSWORD"
    }
def internet_active() -> bool:
    connection = http.HTTPConnection("www.google.com", timeout=5)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except:
        connection.close()
        return False


def sign_in(browser: Chrome, username: str, password: str):
    browser.get_page('https://bootcampspot.com/login')
    browser.enter_text('/html/body/div/section/div/div[2]/input[1]', username)
    browser.enter_text('/html/body/div/section/div/div[2]/input[2]', password)
    browser.press_button('/html/body/div/section/div/div[2]/button')
    time.sleep(4)


def complete_survey(browser: Chrome):
    browser.press_button('/html/body/div/main/div/section/div/div/div/button')
    time.sleep(1)
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[1]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[2]/fieldset/div/label[3]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[3]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[4]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[5]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[6]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[7]/fieldset/div/label[5]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[8]/fieldset/div/label[6]/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/ol/li[9]/fieldset/div/ul/li[5]/label/input')
    browser.press_button('/html/body/div/main/div/section/div/div/form/div/div/button')


def main():

    # This enables colors on windows machines.
    if os.name == 'nt':
        os.system('color')

    while not internet_active():
        warning('Can\'t connect to the internet... trying again in 15 seconds.')
        time.sleep(15)

    inform('Creating browser session...')
    browser_options = ['--headless', '--disable-notifications']
    browser = Chrome(chrome_driver, browser_options)

    inform('Signing into bootcampspot...')
    sign_in(browser, creds['username'], creds['password'])

    current_url = browser.get_current_url()
    if current_url == 'https://bootcampspot.com/login':
        error('Sign in was unsuccessful. Exiting script...')
        browser.close()
        exit(1)

    successful('Sign in was successful!')

    if 'feedback' in current_url.lower():
        inform('Completing the weekly survey.')
        complete_survey(browser)
        browser.get_page('https://bootcampspot.com/')
        time.sleep(4)

    check_in_status = browser.get_text('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]')
    if check_in_status == 'Check In begins 45 minutes before Class':
        warning('Class does not start yet. Exiting script...')
        browser.close()
        exit(0)
    elif check_in_status == 'Check In To Class':
        browser.press_button('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]/a')
        time.sleep(1)
        check_in_status = browser.get_text('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]')

    if check_in_status == 'You are currently checked in as present':
        successful(check_in_status)
        if 'y' in question('Would you like to join class? (y/n): ').lower():
            url = browser.get_element_url('/html/body/div/main/div/section/div/div[2]/div/div/div/a')
            os.startfile(url)
            inform(url)
    else:
        error('Unable to check in! \'Check in\' element not found.')

    browser.close()
    exit(0)


if __name__ == '__main__':
    main()
