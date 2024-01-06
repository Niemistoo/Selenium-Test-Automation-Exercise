from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json

# Load user_data from file
with open('test_user.json') as fp:
    test_user = json.load(fp)

# Register User
def Test_Case_1():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find signup / login button and click it
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Find Signup form. Fill Name, Email Address and submit
    name_form = driver.find_element(By.NAME, 'name')
    name_form.send_keys(test_user["username"])

    email_form = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
    email_form.send_keys(test_user["email"])

    signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    signup_button.click()

    # Verify that 'New User Signup!' is visible
    driver.find_element(By.XPATH, '//h2["New User Signup!"]')

    # Fill Account information form. Title, Name, Email, Password, Date of birth
    title_form = driver.find_element(By.ID, 'uniform-id_gender1')
    title_form.click()

    # Check that 'ENTER ACCOUNT INFORMATION' text is visible
    driver.find_element(By.XPATH, '//b["Enter Account Information"]')

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(test_user["password"])

    select_day = Select(driver.find_element(By.ID, 'days'))
    select_day.select_by_index(1)
    select_month = Select(driver.find_element(By.ID, 'months'))
    select_month.select_by_index(1)
    select_year = Select(driver.find_element(By.ID, 'years'))
    select_year.select_by_index(10)

    # Check sign up newsletter
    select_newsletter = driver.find_element(By.NAME, 'newsletter')
    select_newsletter.location_once_scrolled_into_view
    select_newsletter.click()

    select_special_offers = driver.find_element(By.NAME, 'optin')
    select_special_offers.click()

    # Fill Address Information
    first_name_form = driver.find_element(By.NAME, 'first_name')
    first_name_form.send_keys(test_user["first_name"])

    last_name_form = driver.find_element(By.NAME, 'last_name')
    last_name_form.send_keys(test_user["last_name"])

    company_form = driver.find_element(By.NAME, 'company')
    company_form.send_keys(test_user["company"])

    address_form_1 = driver.find_element(By.NAME, 'address1')
    address_form_1.send_keys(test_user["address1"])

    address_form_2 = driver.find_element(By.NAME, 'address2')
    address_form_2.send_keys(test_user["address2"])

    select_country = Select(driver.find_element(By.NAME, 'country'))
    select_country.select_by_index(1)

    state_form = driver.find_element(By.NAME, 'state')
    state_form.send_keys(test_user["state"])

    city_form = driver.find_element(By.NAME, 'city')
    city_form.send_keys(test_user["city"])

    zipcode_form = driver.find_element(By.NAME, 'zipcode')
    zipcode_form.send_keys(test_user["zipcode"])

    mobile_numer_form = driver.find_element(By.NAME, 'mobile_number')
    mobile_numer_form.send_keys(test_user["phone_number"])

    # Create Account
    create_account_button = driver.find_element(By.XPATH, '//button[@data-qa="create-account"]')
    create_account_button.location_once_scrolled_into_view
    create_account_button.click()

    #Check that 'ACCOUNT CREATED!' text is visible
    driver.find_element(By.XPATH, '//b["Account Created!"]')

    # Press continue button
    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.location_once_scrolled_into_view
    continue_button.click()

    # Check that 'Logged in as username' is visible
    driver.find_element(By.XPATH, f'//b["{test_user["username"]}"]')

    # Delete Account
    delete_account_button = driver.find_element(By.LINK_TEXT, 'Delete Account')
    delete_account_button.location_once_scrolled_into_view
    delete_account_button.click()

    # Check that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    driver.find_element(By.XPATH, '//b["Account Deleted!"]')

    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.click()

    driver.quit()

    print("Test Case 1 Success")


# Login User with correct email and password
def Test_Case_2():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find login link
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Verify 'Login to your account' is visible
    driver.find_element(By.XPATH, '//h2["Login to your account"]')

    # Fill Login info and press Login
    login_email = driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
    login_email.send_keys(test_user["email"])

    login_password = driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
    login_password.send_keys(test_user["password"])

    login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
    login_button.location_once_scrolled_into_view
    login_button.click()

    # Verify that 'Logged in as username' is visible
    driver.find_element(By.XPATH, f'//b["{test_user["username"]}"]')

    # Delete Account
    delete_account_button = driver.find_element(By.LINK_TEXT, 'Delete Account')
    delete_account_button.location_once_scrolled_into_view
    delete_account_button.click()

    # Verify that 'ACCOUNT DELETED!' is visible
    driver.find_element(By.XPATH, '//b["Account Deleted!"]')

    driver.quit()

    print("Test Case 2 Success")

# Login User with incorrect email and password
def Test_Case_3():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find login link
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Verify 'Login to your account' is visible
    driver.find_element(By.XPATH, '//h2["Login to your account"]')

    # Fill Login info and press Login
    login_email = driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
    login_email.send_keys("incorrect@mail.com")

    login_password = driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
    login_password.send_keys("incorrect input")

    login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
    login_button.location_once_scrolled_into_view
    login_button.click()

    # Verify error 'Your email or password is incorrect!' is visible
    driver.find_element(By.XPATH, '//p["Your email or password is incorrect!"]')

    driver.quit()

    print("Test Case 3 Success")

# Logout User
def Test_Case_4():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find login link
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Verify 'Login to your account' is visible
    driver.find_element(By.XPATH, '//h2["Login to your account"]')

    # Fill Login info and press Login
    login_email = driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
    login_email.send_keys(test_user["email"])

    login_password = driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
    login_password.send_keys(test_user["password"])

    login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
    login_button.location_once_scrolled_into_view
    login_button.click()

    # Verify that 'Logged in as username' is visible
    driver.find_element(By.XPATH, f'//b["{test_user["username"]}"]')

    logout_button = driver.find_element(By.LINK_TEXT, 'Logout')
    logout_button.click()

    # Verify that user is navigated to login page
    driver.find_element(By.XPATH, '//title["Automation Exercise - Signup / Login"]')

    driver.quit()

    print("Test Case 4 Success")

def Test_Case_5():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find signup / login button and click it
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Verify that 'New User Signup!' is visible
    driver.find_element(By.XPATH, '//h2["New User Signup!"]')

    # Find Signup form. Fill Name, Email Address and submit
    name_form = driver.find_element(By.NAME, 'name')
    name_form.send_keys(test_user["username"])

    email_form = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
    email_form.send_keys(test_user["email"])

    signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    signup_button.click()

    driver.find_element(By.XPATH, '//p["Email Address already exist!"]')

    driver.quit()

    print("Test Case 5 Success")

# Function to create user for tests if not exists
def create_user():
    driver = webdriver.Chrome()

    # Open website
    driver.get("http://automationexercise.com/")

    driver.implicitly_wait(2)

    # Find signup / login button and click it
    sign_up_link = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    sign_up_link.click()

    # Find Signup form. Fill Name, Email Address and submit
    name_form = driver.find_element(By.NAME, 'name')
    name_form.send_keys(test_user["username"])

    email_form = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
    email_form.send_keys(test_user["email"])

    signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    signup_button.click()

    # Check that 'New User Signup!' text is visible
    driver.find_element(By.XPATH, '//h2["New User Signup!"]')

    # Fill Account information form. Title, Name, Email, Password, Date of birth
    title_form = driver.find_element(By.ID, 'uniform-id_gender1')
    title_form.click()

    # Check that 'ENTER ACCOUNT INFORMATION' text is visible
    driver.find_element(By.XPATH, '//b["Enter Account Information"]')

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(test_user["password"])

    select_day = Select(driver.find_element(By.ID, 'days'))
    select_day.select_by_index(1)
    select_month = Select(driver.find_element(By.ID, 'months'))
    select_month.select_by_index(1)
    select_year = Select(driver.find_element(By.ID, 'years'))
    select_year.select_by_index(10)

    # Check sign up newsletter
    select_newsletter = driver.find_element(By.NAME, 'newsletter')
    select_newsletter.location_once_scrolled_into_view
    select_newsletter.click()

    select_special_offers = driver.find_element(By.NAME, 'optin')
    select_special_offers.click()

    # Fill Address Information
    first_name_form = driver.find_element(By.NAME, 'first_name')
    first_name_form.send_keys(test_user["first_name"])

    last_name_form = driver.find_element(By.NAME, 'last_name')
    last_name_form.send_keys(test_user["last_name"])

    company_form = driver.find_element(By.NAME, 'company')
    company_form.send_keys(test_user["company"])

    address_form_1 = driver.find_element(By.NAME, 'address1')
    address_form_1.send_keys(test_user["address1"])

    address_form_2 = driver.find_element(By.NAME, 'address2')
    address_form_2.send_keys(test_user["address2"])

    select_country = Select(driver.find_element(By.NAME, 'country'))
    select_country.select_by_index(1)

    state_form = driver.find_element(By.NAME, 'state')
    state_form.send_keys(test_user["state"])

    city_form = driver.find_element(By.NAME, 'city')
    city_form.send_keys(test_user["city"])

    zipcode_form = driver.find_element(By.NAME, 'zipcode')
    zipcode_form.send_keys(test_user["zipcode"])

    mobile_numer_form = driver.find_element(By.NAME, 'mobile_number')
    mobile_numer_form.send_keys(test_user["phone_number"])

    # Create Account
    create_account_button = driver.find_element(By.XPATH, '//button[@data-qa="create-account"]')
    create_account_button.location_once_scrolled_into_view
    create_account_button.click()

    #Check that 'ACCOUNT CREATED!' text is visible
    driver.find_element(By.XPATH, '//b["Account Created!"]')

    # Press continue button
    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.location_once_scrolled_into_view
    continue_button.click()

if __name__ == "__main__":
    #create_user()
    Test_Case_1()
    #Test_Case_2()
    #Test_Case_3()
    #Test_Case_4()
    #Test_Case_5()