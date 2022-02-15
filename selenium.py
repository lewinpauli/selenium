import logging
import yaml

from yaml.loader import SafeLoader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from sys import platform
from selenium.webdriver.common.by import By

myoptions = Options()

if platform == "win32" or platform == "win64":
    configfile_location = R"\configfile.yaml"

if platform == "linux": #for Selenium/Ubuntu Container
    configfile_location = R"./configfile.yaml"

if platform == "darwin":
    configfile_location = R"./configfile.yaml"




######## Importing configfile.yml ########

with open(configfile_location, "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=SafeLoader)

####

if platform == "linux": #for Selenium/Ubuntu Container or maybe Linux Desktop User
    chromedriver_location = cfg["container_environment"].get("chromedriver_location")
    myoptions.binary_location = cfg["container_environment"].get("chrome_location")
    pdftest_location = cfg["container_environment"].get("pdftest_location")
    website_url = cfg["container_environment"].get("website_url")
    mylogfile = cfg["container_environment"].get("logfile_location")
    logging_level = cfg["container_environment"].get("logging_level")
    isheadless = cfg["container_environment"].get("headless")
    close_chrome_at_the_end = cfg["container_environment"].get("close_chrome_at_the_end")


if platform == "darwin": #MacOS
    chromedriver_location = cfg["darwin_environment"].get("chromedriver_location")
    myoptions.binary_location = cfg["darwin_environment"].get("chrome_location")
    pdftest_location = cfg["darwin_environment"].get("pdftest_location")
    website_url = cfg["darwin_environment"].get("website_url")
    mylogfile = cfg["darwin_environment"].get("logfile_location")
    logging_level = cfg["darwin_environment"].get("logging_level")
    isheadless = cfg["darwin_environment"].get("headless")
    close_chrome_at_the_end = cfg["darwin_environment"].get("close_chrome_at_the_end")


if platform == "win32" or platform == "win64": #Windows
    chromedriver_location = cfg["windows_environment"].get("chromedriver_location")
    myoptions.binary_location = cfg["windows_environment"].get("chrome_location")
    pdftest_location = cfg["windows_environment"].get("pdftest_location")
    website_url = cfg["windows_environment"].get("website_url")
    mylogfile = cfg["windows_environment"].get("logfile_location")
    logging_level = cfg["windows_environment"].get("logging_level")
    isheadless = cfg["windows_environment"].get("headless")
    close_chrome_at_the_end = cfg["windows_environment"].get("close_chrome_at_the_end")


#####

username = cfg["superadmin"].get("mail")
password = cfg["superadmin"].get("password")

#####

testusermail = cfg["testuser"].get("mail")
testpassword = cfg["testuser"].get("password")
testphone = cfg["testuser"].get("phone")
testname = cfg["testuser"].get("name")
testregistrationnr = cfg["testuser"].get("registrationnr")




myoptions.add_argument('--no-sandbox') #against "DevToolsActivePort file doesn't exist"
myoptions.add_argument('--disable-dev-shm-usage') #against "DevToolsActivePort file doesn't exist"

myoptions.add_argument('--ignore-certificate-errors')

myoptions.add_argument("--window-size=1920,1080")
myoptions.add_argument("--start-maximized")
myoptions.add_argument("--disable-gpu")

if isheadless is True:
    myoptions.add_argument("--headless")#starting browser without UI


#myoptions.add_argument('silent') #Reduce unneccessary Chrome Logs in Terminal
#myoptions.add_argument('log-level=3') #Reduce unneccessary Chrome Logs in Terminal
myoptions.add_experimental_option("excludeSwitches", ["enable-logging"]) #MOST Important to Reduce unneccessary Chrome Logs in Terminal


myservice = Service(chromedriver_location)


driver = webdriver.Chrome(service=myservice, options=myoptions)
driver.get(website_url) #Opening Website


loggingmodes = ['debug' , 'info', 'warning', 'error', 'critical']

if logging_level not in loggingmodes:

    logging.info("variable logging_level in " + configfile_location + " has not an accepted value")
    logging.info("quiting the website test")
    driver.quit()
    raise


if logging_level == "debug":
    logging.basicConfig(level=logging.DEBUG, filename=mylogfile, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

if logging_level == "info":
    logging.basicConfig(level=logging.INFO, filename=mylogfile, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

if logging_level == "warning":
    logging.basicConfig(level=logging.WARNING, filename=mylogfile, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

if logging_level == "error":
    logging.basicConfig(level=logging.ERROR, filename=mylogfile, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

if logging_level == "critical":
    logging.basicConfig(level=logging.CRITICAL, filename=mylogfile, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")



logging.info("################")
logging.info("################")
logging.info("################")
logging.info("starting new website test with selenium")
logging.info("################")
logging.info("current configfile:")
logging.info(cfg)






################ Defining functions ############

def search_id(idname):    #only search an ID on the website
    try:
        driver.find_element(By.ID, idname)

        logging.info("successfully found element with ID " + idname)

    except:
        logging.info("could NOT find element with ID " + idname)
        logging.info("quiting the website test")
        driver.quit()
        raise

###################################

def search_id_and_input(idname, inputtext):    #search ID on the website an enter text/key at that field
    try:
        field = driver.find_element(By.ID, idname)
        field.send_keys(inputtext)

        logging.info("found element with ID " + idname + " and entered the text: " + inputtext + " successfully")

    except:
        logging.info("could NOT find element with ID " + idname + " and so could NOT enter the text: " + inputtext)
        logging.info("quiting the website test")
        driver.quit()
        raise
#################################

def search_id_and_click(idname):    #search ID on the website an click that field
    try:
        driver.find_element(By.ID, idname).click()


        logging.info("found element with ID " + idname + " and clicked it successfully")

    except:
        logging.info("could NOT find element with ID " + idname + " and so could NOT click it")
        logging.info("quiting the website test")
        driver.quit()
        raise

##################################

def search_class_and_input(classname, inputtext):    #search class on the website an enter text/key at that field
    try:
        field = driver.find_element(By.CLASS_NAME, classname)
        field.send_keys(inputtext)

        logging.info("found element with class " + classname + " and entered it successfully")

    except:
        logging.info("could NOT find element with class " + classname + " and so could NOT enter it")
        logging.info("quiting the website test")
        driver.quit()
        raise

################################

def search_class_and_click(classname):
    try:
        driver.find_element(By.CLASS_NAME, classname).click()


        logging.info("found element with classname " + classname + " and clicked it successfully")

    except:
        logging.info("could NOT find element with classname " + classname + " and so could NOT click it")
        logging.info("quiting the website test")
        driver.quit()
        raise

###############################

def search_url_and_input(urlname, inputtext):    #search url on website an enter it
    try:
        field = driver.find_element(By.XPATH, '//a[@href="'+ urlname +'"]')
        field.send_keys(inputtext)

        logging.info("found element with url " + urlname + " and entered it successfully")

    except:
        logging.info("could NOT find element with url " + urlname + " and so could NOT enter it")
        logging.info("quiting the website test")
        driver.quit()
        raise



##############################

def search_link_text_and_input(linktext, inputtext):    #search url on website an enter it
    try:
        field = driver.find_element(By.LINK_TEXT, linktext)
        field.send_keys(inputtext)

        logging.info("found element with linktext " + linktext + " and entered it successfully")

    except:
        logging.info("could NOT find element with linktext " + linktext + " and so could NOT enter it")
        logging.info("quiting the website test")
        driver.quit()
        raise

##############################

def search_name_and_input(name, inputtext):    #search name on website an enter it
    try:
        field = driver.find_element(By.NAME, name)
        field.send_keys(inputtext)

        logging.info("found element with name " + name + " and entered the text '" + inputtext + "' successfully")

    except:
        logging.info("could NOT find element with name " + name + " and so could NOT enter it")
        logging.info("quiting the website test")
        driver.quit()
        raise

##############################

def search_dropdownname_and_select_optiontext(dropdownname, optiontext):
    try:
        field = driver.find_element(By.NAME, dropdownname)

        driver.execute_script("arguments[0].setAttribute('style','display: yes;')", field)

        select = Select(field)

        select.select_by_visible_text(optiontext)

        logging.info("found dropdownname " + dropdownname + " and selected " + optiontext + " successfully")

    except:
        logging.info("Could NOT find dropdownname " + dropdownname + " and Could NOT select " + optiontext)
        logging.info("quiting the website test")
        driver.quit()
        raise

###########################

def search_insert_and_upload_file(sourcefile):
    try:

        driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(sourcefile)

        logging.info("found input element and uploaded file " + sourcefile + " successfully")

    except:
        logging.info("Could NOT find input element or Could NOT find sourcefile " + sourcefile)
        logging.info("quiting the website test")
        driver.quit()
        raise

###########################

def search_text(text):
    try:
        field = driver.find_element(By.XPATH, '//*[text()="'+ text +'"]')


        logging.info("Sucessfully found " + field.text)

    except:
        logging.info("Could not find " + field.text)
        logging.info("quiting the website test")
        driver.quit()
        raise

############################

def search_type_and_input(type, input):
    try:
        driver.find_element(By.XPATH,'//*[@type="'+ type +'"]').send_keys(input)

        logging.info("Sucessfully found type " + type + " and entered input: " + input)

    except:
        logging.info("Could NOT find type " + type + " and so could not enter input: " + input)
        logging.info("quiting the website test")
        driver.quit()
        raise

############### Start of the tests ################



search_id_and_input("login_user", username)

search_id_and_input("login_pwd", password)

search_class_and_input("login__submit", Keys.ENTER)

logging.info("superadmin login successful")

#############


search_url_and_input("/dashboard", Keys.ENTER)

search_url_and_input("/roles/index", Keys.ENTER)

search_url_and_input("/configurations/index", Keys.ENTER)

search_url_and_input("/cloudsight/index", Keys.ENTER)

search_url_and_input("/resources/index", Keys.ENTER)

logging.info(R"text \ue007 = Enter Button")




search_id_and_input("userDropdown", Keys.ENTER)



search_link_text_and_input("Account info", Keys.ENTER)


search_id_and_input("userDropdown", Keys.ENTER)

search_link_text_and_input("Edit password", Keys.ENTER)



######## Creating test account #########


logging.info("creating test account...")

search_url_and_input("/users/staff", Keys.ENTER)

search_url_and_input("/users/staff_edit", Keys.ENTER)

search_name_and_input("row[username]", testusermail)

search_id_and_input("userPassword", testpassword)

search_id_and_click("check_changepassword")

search_dropdownname_and_select_optiontext("row[roles][]","Superadmin")

search_name_and_input("row[code]", testregistrationnr)

search_name_and_input("row[tel_int]", testphone)

search_name_and_input("row[name]", testname)

search_name_and_input("row[surname]", testname)

search_name_and_input("row[tel]", testphone)

search_name_and_input("row[email]", testusermail)

search_type_and_input("submit",Keys.ENTER)




logging.info("logging out to test the new user account")

search_id_and_input("userDropdown", Keys.ENTER)

search_link_text_and_input("Logout", Keys.ENTER)


search_id_and_input("login_user", testusermail)

search_id_and_input("login_pwd", testpassword)

search_class_and_input("login__submit", Keys.ENTER)

try:
    search_url_and_input("/resources/index", Keys.ENTER)#checking login with this link

    logging.info("testuser login successful")

except:
    logging.info("could NOT login with testuser account")
    logging.info("quitting website test")
    driver.quit()
    raise


########### Drag and drop resource ##############

logging.info("trying to upload test resource/file")

search_url_and_input("/resources/index", Keys.ENTER)

search_url_and_input("/resources/edit", Keys.ENTER)

search_insert_and_upload_file(pdftest_location)


#### selecting resource role & user

search_dropdownname_and_select_optiontext("row[roles][]","Superadmin")

search_dropdownname_and_select_optiontext("row[users][]","test test")


#### pressing submit button

search_id_and_input("btn_upload", Keys.ENTER)

#### searching file upload

search_text("pdftest.pdf")

logging.info("uploaded test resource/file successfully")

logging.info("selenium test finished successfully")



if close_chrome_at_the_end is False:

    while(True): #needed so chrome dont close
        pass
