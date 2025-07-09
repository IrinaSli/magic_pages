def test_add_to_compare(product_page):
    product_page.open_page()
    product_page.add_to_compare()
    selected_item, product_name = product_page.add_to_compare()
    assert selected_item == product_name


def test_remove_all_from_compare(product_page):
    product_page.open_page()
    product_page.add_to_compare()
    product_page.remove_all_from_compare()
    expected_message = "You cleared the comparison list."
    assert product_page.get_alert_text() == expected_message


def test_product_actions_are_displayed(product_page):
    product_page.open_page()
    product_page.check_product_actions_is_displayed()
    assert product_page.add_to_compare.is_displayed()
    assert product_page.add_to_cart_btn.is_displayed()
    assert product_page.add_to_wishlist.is_displayed()
