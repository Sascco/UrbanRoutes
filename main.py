import data
from locators import locators
from UrbanRoutesPage import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


#start

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome()  # desired_capabilities = capabilities
        cls.driver.get(data.urban_routes_url)
        cls.driver.implicitly_wait(10)

    #prueba 1 - Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        sleep(5)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.address_from)
        set_route.set_to(data.address_to)
        sleep(5)
        from_1 = set_route.get_from()
        assert from_1 == data.address_from
        set_route.click_book_a_taxi_button()
        sleep(5)

'''
    def test_comfort_fare(self):
        self.driver.get(data.urban_routes_url)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.address_from)
        set_route.set_to(data.address_to)
        comfort_fare = UrbanRoutesPage()
        sleep(3)
        comfort_fare.comfort_fare_button()
        sleep(3)


    def test_fill_phone_number_box(self):  # Rellenar el número de teléfono.
        test_set_location = UrbanRoutesPage(self.driver)
        phone_input = test_set_location.phone_input_box
        phone_input.click()  # Click directly on the web element
        test_set_location.phone_popup_window_input_box(data.phone_number)
        test_set_location.phone_popup_window_input_box_next()
        test_set_location.code_field()
        test_set_location.code_confirm_button()
        sleep(2)

    def test_add_payment_method(self):  # Agregar tarjeta de credito como metodo de pago
        page = UrbanRoutesPage(self.driver)
        sleep(2)
        self.driver.find_element(page.add_cc_button).click()

    def test_special_instruction_for_service(self): # Mensaje para conductor
        test_set_location = UrbanRoutesPage(self.driver)
        test_set_location.message_to_driver_field()
        assert test_set_location.driver.find_element(data.message_for_driver).get_property('value') == data.message_for_driver

    def test_ordering_blanket(self): #Pedir una manta y pañuelos.
        test_set_location = UrbanRoutesPage(self.driver)
        test_set_location.blanket_and_scarves()

    def test_add_icecream(self): # Pedir 2 helados.
        test_set_location = UrbanRoutesPage(self.driver)
        ice_cream_to_order = 2
        test_set_location.click_add_ice_cream_button()
        assert self.driver.find_element(*test_set_location.ice_cream_counter).text == str(ice_cream_to_order)

    def test_waiting_for_taxi_modal(self): # aparece modal para pedir taxi
        test_set_location = UrbanRoutesPage(self.driver)
        self.initial_header = test_set_location.get_waiting_popup_header()
        test_set_location.click_order_taxi_button()
        assert self.driver.find_element(*test_set_location.waiting_popup_header).text == 'Buscar automóvil'
'''
@classmethod
def teardown_class(cls):
    cls.driver.quit()