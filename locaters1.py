from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('/home/prashant/Documents/Browser_Driver/chromedriver')
driver = webdriver.Chrome(service=s)
url='https://www.facebook.com/'
driver.get(url)
driver.maximize_window()

driver.find_element(By.ID, "email").send_keys("pdb.bhole@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("pra07089@@")
driver.find_element(By.NAME, "login").click()
# driver.find_element(By.CSS_SELECTOR, "[=royal_pass]").click()
# driver.find_element(By.XPATH, '''//*[@id="mount_0_0_qL"]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/div/*[name()="svg"]/*[name()="g"]/*[name()="image"]''').click()
driver.find_element(By.XPATH, "//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l lzcic4wl oo9gr5id q9uorilb']/div//*[name()='svg']//*[name()='g']//*[name()='image']").click()
driver.find_element(By.XPATH, "(//span[normalize-space()='Log Out'])[1]").click()
# driver.find_element(By.CSS_SELECTOR, "div[data-nocookies='true'] div[role='button'] div[class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr nnctdnn4'] div[class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz qt6c0cv9 rz4wbd8a a8nywdso jb3vyjys du4w35lb bp9cbjyn ns4p8fja btwxx1t3 l9j0dhe7'] div[class='gs1a9yip ow4ym5g4 auili1gw rq0escxv j83agx80 cbu4d94t buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz rz4wbd8a a8nywdso l9j0dhe7 du4w35lb rj1gh0hx pybr56ya f10w8fjw'] div span[class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn hrzyx87i jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m']").click()





