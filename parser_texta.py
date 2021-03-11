import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def getInput(digit, message):
    inputt = ""
    while inputt == "" or "," in inputt or "." in inputt or "-" in inputt or int(inputt) < 1 or int(inputt)>50:
        inputt = input(message)
    return inputt


list_numbers=str(input("Использовать числа из списка или из диапазона 0 - диапазон, 1 - список"))
list_n=""
driver=webdriver.Chrome()
driver.get("https://randstuff.ru/number/")
driver.maximize_window()
if list_numbers == "1":
    list_n=str(input("Введите числа через запятую"))
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[2]/label[2]").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[2]/ul/li[2]/textarea").send_keys(f'{list_n}')
else:
    a=str(input("Введите 1 число диапазона"))
    b=str(input("Введите 2 число диапазона"))

    min='/html/body/div[1]/div[2]/div/div[4]/div[2]/ul/li[1]/input[1]'
    max='/html/body/div[1]/div[2]/div/div[4]/div[2]/ul/li[1]/input[2]'
    driver.find_element_by_xpath(min).clear()
    driver.find_element_by_xpath(min).send_keys(f'{a}]')

    driver.find_element_by_xpath(max).clear()
    driver.find_element_by_xpath(max).send_keys(f'{b}]')
count=int(getInput("0123456789","Сколько рандомных чисел тебе необходимо? Введи число от 1 до 50"))

repeat_numbers=input("Исключить повторения?0 - нет, 1 - да")
if repeat_numbers == "0":
    repeat=True
elif repeat_numbers=="1":
    repeat=False







ofset=-135+count*5.3

slider=driver.find_element_by_css_selector("#slider")
ActionChains(driver).drag_and_drop_by_offset(slider,xoffset=ofset,yoffset=0).perform()

if count>1 and repeat==False:
    rep=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[3]/label")
    rep.click()



y=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/button")
y.click()
time.sleep(1)
x=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/span')
print("Рандомные числа в выбранном диапазоне:", x.text)
time.sleep(1)



bool_save=str(input("Сохранить результат 0 - нет, 1 - да"))
if bool_save=="0":
    quit()
elif bool_save=="1":
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/span").click()
    time.sleep(2)
    link=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/p/a").get_attribute("href")

    print(link,"Ссылка доступна в течение часа")
