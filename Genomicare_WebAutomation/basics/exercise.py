#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-20 16:29
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get('http://clinical-portal-snapshot.gene-go.com/#/')
driver.maximize_window()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a/span[text()="登录"]')))
driver.find_element_by_xpath('//a/span[text()="登录"]').click()
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'username')))
driver.find_element_by_id('username').send_keys('haiyu.ma')
driver.find_element_by_id('password').send_keys('password.1')
driver.find_element_by_xpath('//button[@class="btn btn-primary mt-1"]').click()
driver.find_element_by_xpath('//span[text()="患者档案"]').click()
driver.find_element_by_xpath('//span[text()="病程记录"]').click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//button[@style="width: 570px;"]')))
driver.find_element_by_xpath('//button[@style="width: 570px;"]').click()
driver.find_element_by_xpath('//span[contains(text(),"A03037")]').click()
driver.find_element_by_xpath('//span[@jhitranslate="entity.action.confirm"]').click()
# 修改：
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="healthCondition"]//button[@class="btn btn-primary"]')))
driver.find_element_by_xpath('//*[@id="healthCondition"]//button[@class="btn btn-primary"]').click()
# select:
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ecog"]')))
ecog=driver.find_element_by_xpath('//select[@name="ecog"]')
s=Select(ecog)
s.select_by_index(3)
time.sleep(2)
# 方式二：value值
s.select_by_value("4")
# 方式三:文本内容
s.select_by_visible_text("5")
time.sleep(2)
ethnic=driver.find_element_by_xpath('//select[@class="form-control ng-untouched ng-pristine ng-valid"]')
e=Select(ethnic)
e.select_by_index(1)
time.sleep(1)
e.select_by_value("6: 'WWER'")
time.sleep(1)
e.select_by_visible_text("蒙古族")

driver.find_element_by_xpath('//button[@form="ngForm"]').click()
time.sleep(2)
# 删除：
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="healthCondition"]//button[@class="btn btn-danger"]')))
driver.find_element_by_xpath('//*[@id="healthCondition"]//button[@class="btn btn-danger"]').click()
# 确认删除
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//form[@name="deleteForm"]//button[@class="btn btn-danger"]')))
# driver.find_element_by_xpath('//form[@name="deleteForm"]//button[@class="btn btn-danger"]').click()
time.sleep(2)
# 取消删除：
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//form[@name="deleteForm"]//button[@class="btn btn-secondary"]')))
driver.find_element_by_xpath('//form[@name="deleteForm"]//button[@class="btn btn-secondary"]').click()
time.sleep(5)
driver.quit()
