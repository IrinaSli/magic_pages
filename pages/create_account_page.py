from selenium.webdriver.common.by import By
from pages.base_page import BasePage


firstname_loc = (By.ID, "firstname")
last_name_loc = (By.ID, "lastname")
email_input_loc = (By.ID, "email_address")
psw_input_loc = (By.ID, "password")
psw_confirmation_input_loc = (By.ID, "password-confirmation")
create_an_account_button_loc = (By.CSS_SELECTOR, 'button.action.submit.primary')
email_address_error_loc = (By.ID, "email_address-error")
psw_error_loc = (By.ID, "password-error")
last_name_error_loc = (By.ID, "lastname-error")


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"


    def fill_create_form(self, firstname, lastname, email, psw, psw_confirmation):
        firstname_input = self.find(firstname_loc)
        last_name_input = self.find(last_name_loc)
        email_input = self.find(email_input_loc)
        psw_input = self.find(psw_input_loc)
        psw_confirmation_input = self.find(psw_confirmation_input_loc)
        create_an_account_button = self.find(create_an_account_button_loc)
        firstname_input.send_keys(firstname)
        last_name_input.send_keys(lastname)
        email_input.send_keys(email)
        psw_input.send_keys(psw)
        psw_confirmation_input.send_keys(psw_confirmation)
        create_an_account_button.click()


    def check_email_address_error_is_displayed(self):
        email_error = self.find(email_address_error_loc)
        assert email_error.is_displayed()


    def check_password_format_error_is_displayed(self):
        psw_requirements_text = 'Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.'
        psw_error_text = self.find(psw_error_loc).text
        assert psw_requirements_text == psw_error_text


    def check_lastname_is_required(self):
        last_name_error = self.find(last_name_error_loc)
        assert last_name_error.is_displayed()
