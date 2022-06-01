from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from measurements import ABpackages,sku
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
usernameStr = "asupport@davislegend.com"
passwordStr = "Chicago1932!"
url = 'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F'
usernameDef = 'azhang@sharkrack.com'
passwordDef = 'sharkrack123'
usernameS1 = 'asupport@davislegend.com'
passwordS1 = 'Diehl2580!'
usernameS2 = 'sales@platintl.com'
passwordS2 = 'Diehl2580d!'

#Sign in to Ebay and 2 Shippo
driver.get(url)
# driver.switch_to.new_window('tab')

# Log In to Shippo 1
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# driver.get('https://apps.goshippo.com/login')
# email = driver.find_element(By.CSS_SELECTOR, 'div.mb-6 > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
# email.send_keys(usernameS2)
# passwordS = driver.find_element(By.CSS_SELECTOR, 'div.mb-6 > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')
# passwordS.send_keys(passwordS2)
# logIn = driver.find_element(By.CSS_SELECTOR, '.css-125mcs5')
# logIn.click()
# driver.switch_to.window(driver.window_handles[0])


time.sleep(20) #Time to do the captcha
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.default_content()
username = driver.find_element(By.ID,'userid')
username.send_keys(usernameStr)
nextButton = driver.find_element(By.NAME,'signin-continue-btn')
nextButton.click()
time.sleep(2)
password = driver.find_element(By.ID,'pass')
password.send_keys(passwordStr)
signIn = driver.find_element(By.ID,'sgnBt')
signIn.click()

# change url to https://www.ebay.com/sh/ord later
# test: https://www.ebay.com/sh/ord/?filter=status:PAID_SHIPPED
time.sleep(3)
driver.get('https://www.ebay.com/sh/ord/?filter=status:PAID_SHIPPED')
elems = driver.find_elements(By.CLASS_NAME,'order-details [href]')
orders = [elem.get_attribute('href') for elem in elems] 
print(orders[0])

#driver.find_element(By.ID, 'gh-la').send_keys(Keys.CONTROL + 't')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://v2.deftship.com/login')
usernameD = driver.find_element(By.ID, 'email')
usernameD.send_keys(usernameDef)
passwordD = driver.find_element(By.ID,'password')
passwordD.send_keys(passwordDef)
signInD = driver.find_element(By.CSS_SELECTOR, 'button.w-full')
signInD.click()
time.sleep(2)

#Add loop for every item
currentWindow = 1
for order in orders:
    driver.execute_script('''window.open("http://bings.com","_blank");''')
    driver.switch_to.window(driver.window_handles[currentWindow+1])
    driver.get(order)
    infos = driver.find_elements(By.ID, "-help")
    details = [info.get_attribute("innerText") for info in infos]
    print(details)
    item = driver.find_element(By.CLASS_NAME,'item-title').get_attribute('innerText')
    print(item)
    orderNum = driver.find_element(By.CLASS_NAME,'order-details-title').get_attribute('innerText')
    orderNum = orderNum[13:]
    print(orderNum)
    quantity = driver.find_element(By.CSS_SELECTOR, 'td.quantity > span:nth-child(1)').get_attribute('innerText')
    print(quantity)
    userID = driver.find_element(By.CLASS_NAME, 'user-id').get_attribute('innerText')
    driver.switch_to.window(driver.window_handles[currentWindow])

    #Information sort
    name = details[3]
    address2 = ""
    address3 = ""
    if len(details) == 11:
        n=0
    elif len(details) == 12:
        n=1
        address2 = details[n+4]
    else:
        n=2
        address2 = details[n+3]
        address3 = details[n+4]
    phone = details[n+9]
    address = details[4]
    city = details[n+5]
    state = details[n+6]
    zip = details[n+7]


    # Enter Shipping Information
    # newShipment = driver.find_element(By.CSS_SELECTOR, 'div.justify-center:nth-child(2) > button:nth-child(2)')
    # newShipment.click()
    shipName = driver.find_element(By.CSS_SELECTOR,'#receiver-name > div > div > div.flex.flex-grow.items-stretch.focus-within\:z-10 > input')
    shipName.send_keys(name)
    shipAttention = driver.find_element(By.ID, 'attention')
    shipAttention.send_keys(name)
    shipPhone = driver.find_element(By.XPATH,'//*[@id="main-wrapper"]/main/div/form/div/div[2]/div[2]/div[2]/div/div[3]/input')
    shipPhone.send_keys(phone)   
    shipAddress = driver.find_element(By.ID,'street-1')
    shipAddress.send_keys(address)
    if(len(address2)>0):
        shipAddress2 = driver.find_element(By.ID, 'street-2')
        shipAddress2.send_keys(address2)
    if(len(address3)>0):
        shipAddress3 = driver.find_element(By.ID, 'street-3')
        shipAddress3.send_keys(address3)
    shipZip = driver.find_element(By.ID, 'zip')
    zip = zip[:5]
    shipZip.send_keys(zip)
    shipState = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div/form/div/div[2]/div[2]/div[2]/div/div[10]/div/div/div')
    # shipState.click()
    # shipState.send_keys(state + u'\ue007')
    time.sleep(2)
    shipCity = driver.find_element(By.CSS_SELECTOR, '#city')
    shipCity.clear()
    shipCity.send_keys(city)
    validate = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div/form/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/button')

    # Enter Package Information
    currentItem = ['','','','','','']
    packageB = ['','','','','','']
    i = 0
    while(i < int(quantity)):
        for package in range(len(ABpackages)-1):
            if item.__contains__(ABpackages[package][0]):
                currentItem = ABpackages[package]
                packageB = ABpackages[package+1]
                break
        for package in sku:
            if item.__contains__(package[0]):
                currentItem = package
                break
        print(currentItem)
        if(currentItem[0] == ''):
            break
        weight = driver.find_element(By.ID, 'weight_' + str(i))
        weight.send_keys(currentItem[5])
        length = driver.find_element(By.ID, 'length_' + str(i))
        length.send_keys(currentItem[2])
        width = driver.find_element(By.ID, 'width_' + str(i))
        width.send_keys(currentItem[3])
        height = driver.find_element(By.ID, 'height_' + str(i))
        height.send_keys(currentItem[4])
        reference2 = driver.find_element(By.ID, 'reference_2_' + str(i))
        reference2.send_keys(orderNum + '-' + userID)
        descript = driver.find_element(By.ID, 'description_' + str(i) + '_0')
        descript.send_keys(currentItem[1])
        skuPackage = driver.find_element(By.ID, 'sku_' + str(i) + '_0')
        skuPackage.send_keys(currentItem[1])
        if packageB[0] != "":
            i += 1
            newPackage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/form/div/div[2]/div[3]/div[2]/div[2]/div/a')
            newPackage.click()
            weight = driver.find_element(By.ID, 'weight_' + str(i))
            weight.send_keys(packageB[5])
            length = driver.find_element(By.ID, 'length_' + str(i))
            length.send_keys(packageB[2])
            width = driver.find_element(By.ID, 'width_' + str(i))
            width.send_keys(packageB[3])
            height = driver.find_element(By.ID, 'height_' + str(i))
            height.send_keys(packageB[4])
            reference2 = driver.find_element(By.ID, 'reference_2_' + str(i))
            reference2.send_keys(orderNum + '-' + userID)
            descript = driver.find_element(By.ID, 'description_' + str(i) + '_0')
            descript.send_keys(packageB[1])
            skuPackage = driver.find_element(By.ID, 'sku_' + str(i) + '_0')
            skuPackage.send_keys(packageB[1])
        i += 1
        if(i < int(quantity)):
            newPackage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/form/div/div[2]/div[3]/div[2]/div[2]/div/a')
            newPackage.click()
    driver.switch_to.window(driver.window_handles[currentWindow+1])
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
    currentWindow += 1
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[currentWindow])
    driver.get('https://v2.deftship.com/login')
time.sleep(100000)
    # getQuotes = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/main/div/form/div/div[2]/div[4]/div/button')
#div.copy-item:nth-child(4) > dd:nth-child(2) > span:nth-child(1) > span:nth-child(1) > div:nth-child(1) > button:nth-child(1)