import time
import POM
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def testDrop():

    driver = webdriver.Chrome()
    driver.get('https://moodle.com/get-moodle/')
    try:  # entring year
        dd_demo = driver.find_element(By.NAME, "subject")
        dd_select = Select(dd_demo)
        dd_select.select_by_index(2)
        time.sleep(5)
    except:
        print("asdfasdf")
        sys.exit(1)
    try:  # create account button
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "newsletter-gdpr-consent"))).click()
        print('signup button has successful\n')
        time.sleep(5)
    except:
        print("asdfg23")
        sys.exit(1)


def Register(Fname,Lname,Us,Psw):

    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    file = open('details.txt', 'w')
    file1 = open('Res.txt', 'w')
    file.write('-correct details test-\n')

    try:#create account button
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Create new account"))).click()
      file.write('signup button has successful\n')
    except:
      file.write('signup button has faild\n')
      file1.write('Correct details test has not successful')
      sys.exit(1)


    try:#enter First name
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.FirstName))).send_keys(Fname)
        file.write('Firsr name field has successful\n')
    except:
        file.write('cant find First name field\n')
        time.sleep(5)
        file1.write('First name field has not been found')
        sys.exit(1)


    try:#enter Last name
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.LastName))).send_keys(Lname)
        file.write('last name has successful\n')
    except:
        file.write('last name feild have not found\n')
        sys.exit(1)


    try:#enter Reg email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.RegEmail))).send_keys(Us)
        file.write(' Register email has successful\n')
        time.sleep(2)
    except:
        file.write('reg email field has not been successful\n')
        sys.exit(1)

    try:  # enter Reg email confirmation
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.RegEmailConf))).send_keys(Us)
        file.write(' Register email has successful\n')
    except:
        file.write('reg email field has not been successful\n')
        sys.exit(1)

    try:#enter Reg password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.RegPsw))).send_keys(Psw)
        file.write('password has successful\n')
        time.sleep(1)
    except:
        file.write('password feild have not found\n')
        sys.exit(1)


    try:#entering month
        dd_demo = driver.find_element(By.ID,POM.RegMonthid)
        dd_select = Select(dd_demo)
        dd_select.select_by_visible_text(POM.SignupMonth)
        time.sleep(1)

    except:
        file.write("blablabla")


    try:#entring day
        dd_demo = driver.find_element(By.ID,POM.RegDayid)
        dd_select = Select(dd_demo)
        dd_select.select_by_visible_text(POM.SignupDay)
        time.sleep(1)
        file.write("donedondone\n")

    except:
        file.write("blablabla")


    try:#entring year
        dd_demo = driver.find_element(By.ID,POM.RegYearid)
        dd_select = Select(dd_demo)
        dd_select.select_by_visible_text(POM.SignupYear)
        time.sleep(1)

    except:
        file.write("blablabla")

   # try:#gender checkbox
    #  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'sex'))).click()
     # file.write('gender choose succ\n')
      #time.sleep(5)
    #except:
     # file.write('gender choose has not succ\n')
      #file1.write('Correct details test has not successful')
      #sys.exit(1)

    try:#gender checkbox
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'websubmit'))).click()
      file.write('gender choose succ\n')
      time.sleep(5)
    except:
      file.write('gender choose has not succ\n')
      file1.write('Correct details test has not successful')
      sys.exit(1)




def LogToWeb(Us,Psw):
    driver=webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    file=open('details.txt','w')
    file1=open('Res.txt','w')
    file.write('-correct details test-\n')

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.emailbyid))).send_keys(Us)
        file.write('field has successful\n')

    except:
        file.write('cant find the email field\n')
        time.sleep(5)
        file1.write('Correct details test has not successful')
        sys.exit(1)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.passwordbyid))).send_keys(Psw)
        file.write('password has successful\n')

    except:
        file.write('password feild have not found\n')
        file1.write('Correct details test has not successful')
        sys.exit(1)


    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login'))).click()
        file.write('login button has successful\n')
        file1.write('Correct details test has successful')
    except:
        file.write('login button has faild\n')
        time.sleep(10)
        file1.write('Correct details test has not successful')
        sys.exit(1)


    file.write('*****************\n')
    driver.get_screenshot_as_file('Succ.png')
    file.close()
    file1.close()


def FaildIdLogToWeb(Us,Psw):
    driver=webdriver.Chrome()
    driver.get('https://facebook.com')
    file = open('details.txt', 'w')
    file.write('-uncorrect email test-\n')
    file1=open('Res.txt','w')

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.emailbyid))).send_keys(Us)
        file.write('field has successful\n')
    except:
       file.write('cant find the email field')
       time.sleep(5)
       file1.write('unCorrect emial test has not successful')
       sys.exit(1)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.passwordbyid))).send_keys(Psw)
        file.write('passowrd field have successful\n')
        time.sleep(5)
    except:
        file.write('password feild have not found')
        time.sleep(10)
        file1.write('unCorrect emial test has not successful')
        sys.exit(1)
    try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login'))).click()
            file.write('login button has successful\n')
            file1.write('unCorrect emial test has successful')
            time.sleep(10)
    except:
            file.write('Loing button has not found')
            file1.write('unCorrect emial test has not successful')
            sys.exit(1)
    file.write('*****************\n')
    file.close()
    file1.close()

    driver.get_screenshot_as_file('ErriorId.png')


def FaildPswLogToWeb(Us,Psw):
    driver=webdriver.Chrome()
    driver.get('https://facebook.com')
    file = open('details.txt', 'w')
    file.write('-uncorrect password test-\n')
    file1=open('Res.txt','w')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.emailbyid))).send_keys(Us)
        file.write('email field has successful\n')

    except:
        file.write('cant find the email field\n')
        time.sleep(5)
        file1.write('unCorrect password test has not successful')
        sys.exit(1)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, POM.passwordbyid))).send_keys(Psw)
        file.write('passowrd field have successful\n')


    except:
        file.write('password feild have not found\n')
        time.sleep(10)
        file1.write('unCorrect password test has not successful')
        sys.exit(1)
    try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login'))).click()
            file.write('login button has successful\n')
            file1.write('unCorrect password test has successful\n')

    except:
            file.write('Loing button has not found\n')
            time.sleep(10)
            file1.write('unCorrect password test has not successful\n')
            sys.exit(1)
    file.write('*****************\n')
    file1.write('***************\n')
    time.sleep(10)
    driver.get_screenshot_as_file('Erriorpass.png')
    file.close()
    file1.close()


