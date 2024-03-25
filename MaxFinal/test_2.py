from testpage import OperationsHelper, get, post, get_post, login
import logging
import time
import yaml


with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)

# # Step 1: Login with invalid data
# def test_step_1(browser):
#     logging.info("Test 1 starting")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login('test')
#     testpage.enter_pass('test')
#     testpage.click_login_button()
#     assert testpage.get_error_text() == str(test_data['login_error'])
#
# # Step 2: Login with valid data
# def test_step_2(browser):
#     logging.info("Test 2 starting")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(test_data['login'])
#     testpage.enter_pass(test_data['password'])
#     testpage.click_login_button()
#     assert testpage.get_login_enter_text() == test_data['login_word']
#
# # Step 3: Press 'About' button and check page title
# def test_step_3(browser):
#     logging.info("Test 3 starting")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(test_data['login'])
#     testpage.enter_pass(test_data['password'])
#     testpage.click_login_button()
#
#     testpage.click_about_button()
#     time.sleep(test_data['sleep_time'])
#     assert testpage.get_about_text() == test_data['about_title']
#
#

## Step 4: Check front size in page title
def test_step4(browser):

    logging.info("Test 4 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()

    testpage.click_about_button()
    time.sleep(test_data['sleep_time'])
    assert testpage.take_title_font_size() == test_data["font_size"]