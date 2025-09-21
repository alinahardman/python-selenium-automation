from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ProductDetailsPage(BasePage):

    COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

    def open_target(self):
       self.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
       sleep(5)


    def click_and_verify_colors(self):
        expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
        actual_colors = []

        colors = self.driver.find_elements(*self.COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        print(colors)

        for c in colors:
            c.click()
            # for visibility only:
            sleep(0.5)

            selected_color = self.driver.find_element(*self.SELECTED_COLOR).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
