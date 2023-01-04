import datetime
import moodle_locators as locators
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
s=Service(executable_path="chromedriver.exe")

driver=webdriver.Chrome(service=s)
#Fixture methods

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)     #wait browser to load
    driver.get(locators.moodle_url)   #navigate to moodle app site

# Checking that we're on the correct URL address and we're seeing correct title

    if driver.current_url == locators.moodle_url and driver.title == 'Moodle Test Server 3':
        print(f'We\'re at the correct homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Moodle Test Server 3"')
    else:
        print(f'We\'re not at the correct homepage. Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f"---------------------")
        print(f"The test was completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

def log_in(username0,password0):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        driver.find_element(By.ID, 'username').clear()
        sleep(.25)
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, 'username').send_keys(username0)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password0)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url ==locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'Log in "{username0}" successfully. the Dashboard is present')
            else:
                print(f'We\'re not at the Dashboard. Try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'usermenu').click()
    sleep(0.25)
 #   driver.find_element(By.XPATH, '//*[contains(., "Log out")]').click()  # not really act with browser navigation
    driver.find_element(By.LINK_TEXT, 'Log out').click()     #this works too,
#  while the above line By.XPATH is dynamic and search all including html, ccs..
    sleep(1)

    if driver.current_url == locators.moodle_url:
        print(f'Log out successfully at: {datetime.datetime.now()}')

def create_new_user():
    #    driver.find_element(By.XPATH,'//*[contains(., "Site administration")]').click()
        driver.find_element(By.LINK_TEXT,'Site administration').click()

        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Users').click()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Add a new user').click()
        sleep(0.25)
        driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
        sleep(0.25)
        driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.ID, 'id_email').send_keys(locators.email)
        sleep(0.25)
        Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
        sleep(0.25)

        driver.find_element(By.ID,'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
        sleep(0.25)
        driver.find_element(By.ID, 'id_city').send_keys(locators.city)
        sleep(0.25)
    #    breakpoint()

#        Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(f'{locators.country}')
# disabled option

        Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
        sleep(0.25)

        Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
        driver.find_element(By.ID,"id_description_editoreditable").send_keys(locators.desc)
        sleep(1)


        driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
        sleep(1)
        driver.find_element(By.XPATH,'//a[contains(.,"Additional names")]').click()
# or      driver.find_element(By.ID, 'collapseElement-2').click()
        sleep(1)


        driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_first_name)
        sleep(0.25)
        driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_last_name)
        sleep(0.25)


        driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_middle_name)
        sleep(0.25)
        driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_alternate_name)
        sleep(1)
        driver.find_element(By.XPATH,'//a[contains(.,"Interests")]').click()
        for tags in locators.list_of_interests:

            driver.find_element(By.XPATH,'//div[3]/input').click()
            sleep(0.21)
            driver.find_element(By.XPATH,'//div[3]/input').send_keys(tags)
            sleep(.23)
            driver.find_element(By.XPATH,'//div[3]/input').send_keys(Keys.ENTER)
            sleep(.23)

        driver.find_element(By.XPATH,'//a[contains(.,"Optional")]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,'input#id_idnumber').send_keys(locators.id_number)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#id_institution").send_keys(locators.institution)
        sleep(0.3)


        driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone1)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.phone2)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)


        driver.find_element(By.ID, 'id_submitbutton').click()
   #     breakpoint()

def check_user_created():
    if (driver.current_url==locators.moodle_users_main_page):
        assert driver.find_element(By.XPATH,"//h1[text()='Moodle Test Server 3']").is_displayed()
        driver.find_element(By.LINK_TEXT,'Show more...').click()
        # OR:
        #driver.find_element(By.XPATH, '//a[contains(.,"Show more...")]').click()
        if driver.find_element(By.ID,'fgroup_id_email_grp') and \
            driver.find_element(By.NAME,'email'):
            sleep(.25)
            driver.find_element(By.CSS_SELECTOR,"input#id_email").send_keys(locators.email)
            sleep(.3)
            driver.find_element(By.CSS_SELECTOR, "input#id_addfilter").click()
            sleep(.25)
            if driver.find_element(By.XPATH,f'//td[contains(.,"{locators.email}")]'):
                print('for the test scenario: check user created -- pass')
              #  log_out()


def check_new_credentials():
    if driver.current_url==locators.moodle_users_main_page:
        if driver.find_element(By.XPATH,f'//*[contains(.,"{locators.fullname}")]').is_displayed():
            print(f'------------user with the name {locators.fullname }id displayed, hence test passed ')

def change_password():

    print('the url for newly created user page is:'+ driver.current_url)

    if driver.find_element(By.XPATH,f"//*[contains(.,'{locators.fullname}')]").is_displayed():
        print(f'the user is: {locators.fullname}')
        sleep(4)
    else:
        print('the name is not present!')


 #       breakpoint()


    #calling

#Open web browser
setUp()
# Log in
log_in(locators.moodle_username,locators.moodle_password)

create_new_user()
check_user_created()

#log_in(locators.new_username,locators.new_password)
check_new_credentials()

print('logout temporarily to verify username created...')
sleep(1)
log_out()

log_in(locators.new_username,locators.new_password)
change_password()
log_out()

log_in(locators.moodle_username,locators.moodle_password)

# Log out
log_out()

# Close the web browser
tearDown()
