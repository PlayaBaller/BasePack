from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://habr.com/ru/hub/space/')
# elem = browser.find_element_by_css_selector('#post_486792 > article > h2 > a')
# print(elem)
# elem.click()

searchField = browser.find_element_by_css_selector('#search-form-btn')
searchField.send_keys('Грядущее галактическое столкновение Млечного Пути уже рождает новые звезды')
searchField.submit()
browser.back()
browser.refresh()
browser.quit()

