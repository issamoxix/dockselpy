import os
from pyvirtualdisplay import Display
from selenium import webdriver


BASE_URL = 'https://api.kanye.rest/'


def chrome_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(BASE_URL)
    print(browser.page_source)
    browser.quit()
    display.stop()


if __name__ == '__main__':
    chrome_example()
