from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResults(Page):
    SEARCH_FIELD = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULT = (By.CSS_SELECTOR, "a[aria-label*='SkinnyPop']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[aria-label*='SkinnyPop']")

    def __init__(self, driver):
        super().__init__(driver)
        self.app = None

    def verify_search_results(self, expected_item):
        # self.app.search_results.search(expected_search)
        # verify_search_text = WebDriverWait(self.driver, 5).until(
         #   EC.presence_of_element_located((By.CSS_SELECTOR, *self.SEARCH_RESULT))
        #)
        actual_text = self.driver.find_element(*self.SEARCH_FIELD).text
        assert expected_item in actual_text, f'Error: Text {expected_item} not in {actual_text}'

    def verify_item_in_cart(self):
        self.click(*self.ADD_TO_CART)

    # def verify_url_page(self, expected_url):
    #     self.app.search_results_page.verify_partial_url(expected_url)
