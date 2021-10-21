from ChromeAutomation import Chrome
import http.client as http
import time
import os
from PrintAffects import inform, warning, successful, error


def internet_active() -> bool:
    connection = http.HTTPConnection("www.google.com", timeout=5)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except:
        connection.close()
        return False


def main():

    # This enables colors on windows machines.
    if os.name == 'nt':
        os.system('color')

    while not internet_active():
        warning('Can\'t connect to the internet... trying again in 15 seconds.')
        time.sleep(15)

    creds = {
        "username": "YOUR USERNAME",
        "password": "YOUR PASSWORD"
    }

    inform('Creating browser session...')
    browser_options = ['--headless', '--disable-notifications']
    browser = Chrome(r'D:\PyCharm\BootcampAutomation\WebDriver\chromedriver.exe', browser_options)

    inform('Signing into bootcampspot...')
    browser.get_page('https://bootcampspot.com/login')
    browser.enter_text('/html/body/div/section/div/div[2]/input[1]', creds['username'])
    browser.enter_text('/html/body/div/section/div/div[2]/input[2]', creds['password'])
    browser.press_button('/html/body/div/section/div/div[2]/button')
    time.sleep(3)

    if browser.get_current_url() != 'https://bootcampspot.com/':
        error('Sign in was unsuccessful. Exiting script...')
        browser.close()
        exit(1)
    successful('Sign in was successful!')

    check_in_status = browser.get_text('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]')
    if check_in_status == 'Check In begins 45 minutes before Class':
        warning('Class does not start yet. Exiting script...')
        browser.close()
        exit(0)
    elif check_in_status == 'Check In To Class':
        browser.press_button('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]/a')
    check_in_status = browser.get_text('/html/body/div/main/div/section/div/div[3]/div/div[3]/ul/li[2]')
    if check_in_status == 'You are currently checked in as present':
        successful(check_in_status)
        if 'y' in input('[?] Would you like to join class? (y/n): ').lower():
            url = browser.get_element_url('/html/body/div/main/div/section/div/div[2]/div/div/div/a')
            os.startfile(url)
    else:
        error('Unable to check in! \'Check in\' element not found.')
        exit(1)

    browser.close()
    exit(0)


if __name__ == '__main__':
    main()
