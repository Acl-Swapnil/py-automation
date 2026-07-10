import time
import pytest

@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
])
def test_add_products_to_cart(logged_in_page, product_name):
    page = logged_in_page
    item = page.locator(".inventory_item", has_text=product_name)
    item.locator("button").click()
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.is_visible()


def test_simulated_slow_task_1():
    time.sleep(2)
    assert True


def test_simulated_slow_task_2():
    time.sleep(2)
    assert True


def test_simulated_slow_task_3():
    time.sleep(2)
    assert True