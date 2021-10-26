from selenium import webdriver
import pyautogui
from time import sleep
from tkinter import *
#Tkinter
excelN=''
prot=''
def myClick():
    global excelN
    global prot
    excelN=excelE.get()
    prot=protE.get()
    root.destroy()
    return excelN,prot
#GUI
root = Tk()
root.title('Nir Yad2 Bot')

#Slots
protE = Entry(root,width=50,borderwidth=2)
protE.grid(row=0,column = 1)
excelE = Entry(root,width=50,borderwidth=2)
excelE.grid(row=1,column = 1)
#Labels
label1 = Label(root,text='Proteins: ')
label2= Label(root,text='Excel name: ')
label1.grid(row=0,column = 0)
label2.grid(row=1,column = 0)
#Button
b = Button(root,text = "Run",command = myClick)
b.grid(row=2,column = 2)

root.mainloop()

#selenium
driver = webdriver.Chrome(r'C:\Users\NS\Downloads\PYTHON\chromedriver.exe')
driver.get('https://david.ncifcrf.gov/tools.jsp')
driver.maximize_window()
driver.implicitly_wait(300)
driver.find_element_by_id('LISTBox').send_keys(prot)
identifier = driver.find_element_by_id('Identifier')
identifier.click()
identifier.send_keys('uu')
driver.find_element_by_name('rbUploadType').click()
driver.find_element_by_name('B52').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]').click()
driver.find_element_by_name('Clear All').click()
driver.find_element_by_id('Gene_Ontologytd').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/ul/li[2]/ul/li/table/tbody/tr[7]/td[1]/input').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/ul/li[2]/ul/li/table/tbody/tr[15]/td[1]/input').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/ul/li[2]/ul/li/table/tbody/tr[23]/td[1]/input').click()
driver.find_element_by_id('Pathwaystd').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/ul/li[6]/ul/li/table/tbody/tr[3]/td[1]/input').click()
driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table[3]/tbody/tr[2]/td[1]/button').click()
driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
driver.find_element_by_xpath(
    '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/form/table[2]/tbody/tr/td[2]/font/a').click()
sleep(2)
pyautogui.click()
#Saving
pyautogui.hotkey('ctrl', 's')
sleep(1)
pyautogui.write(excelN)
#pyautogui.press('enter')

#Protein list example
"""
prot = [''''  Q4KML4,
Q6ZQ06,
Q3TDD9,
P56565,
P05366,
P27786,
Q62433,
P12790,
Q8CHH9,
P56392,
G5E829,
P32848,
Q61285,
Q9D154,
P13412,
E9QMW4,
Q60590,
Q19LI2,
Q60953,
Q9DBB9,
P27661,
Q3ULW8,
Q64339,
Q9EPL9,
A8DUK4,
Q91XV3,
Q8VDW0,
Q9D8Y1,
B2RX12,
Q8C6K9,
P11087,
Q01149,
Q8K2C7,
P62631,
Q99NB1,
P14602,
O08528,
P47934,
Q7TQ48,
Q9DBE0,
A2ABU4,
O88990,
O35900,
Q64FW2,
Q62270,
P26450,
P81117,
O08915,
Q8K2H2,
A2AKX3,
O88783,
Q9CPT5,
P23780,
P47877,
F6RWR5,
Q8BH04,
Q8BSI6,
P08905,
Gsk3b
''']
"""
