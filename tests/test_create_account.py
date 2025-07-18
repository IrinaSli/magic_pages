def test_email_format_validation(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_create_form('name', "lastname", "test_email", "te123456", "te123456")
    create_account_page.check_email_address_error_is_displayed()


def test_password_format(create_account_page):
    psw_requirements_text = 'Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.'
    create_account_page.open_page()
    create_account_page.fill_create_form('name', "lastname", "test_email", "te", "te")
    create_account_page.check_password_format_error_is_displayed(psw_requirements_text)


def test_lastname_is_required(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_create_form("name", "", "test_email", "te123456", "te123456")
    create_account_page.check_lastname_is_required()
