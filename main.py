from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import time
driver = webdriver.Chrome('./chromedriver')
driver.get('https://hoc22.ebssw.kr/sso/loginView.do?loginType=onlineClass')
driver.find_element_by_name('j_username').send_keys('your_id')
driver.find_element_by_name('j_password').send_keys('your_pw')
driver.find_element_by_class_name('img_type').click()
time.sleep(0.5)
driver.get('https://hoc22.ebssw.kr/20sr205/hmpg/hmpgBbsListView.do?menuSn=411966&bbsId=BBSID_000399096')
driver.find_element_by_class_name('class_nm_ellipsis').click()
text=driver.find_elements_by_tag_name('p')
word=text[5].text
word=word[10:word.find('\n')]
driver.find_element_by_tag_name('textarea').send_keys('20509 박민준 '+word)
driver.find_element_by_class_name('submit').click()
da = Alert(driver)
da.accept()