import data
import locators
from UrbanRoutesPage import UrbanRoutesPage
from selenium import webdriver
from time import sleep


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()  # desired_capabilities = capabilities
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.driver.implicitly_wait(10)

    #prueba 1 - Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        from_1 = set_route.get_from()
        assert from_1 == data.ADDRESS_FROM
        set_route.click_book_a_taxi_button()                        #OK

    #prueba 2  Seleccionar la tarifa Comfort.
    def test_comfort_fare(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.comfort_fare_button() #OJO   Metodo para confirmar tarifa Comfort
        sleep(2)
        set_route.order_requirements()
        assert set_route.comfort_menu() == 'Helado'                 #OK


    # prueba 3 - Rellenar el número de teléfono
    def test_fill_phone_number_box(self):  # Rellenar el número de teléfono.
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.set_phone_input_box()
        set_route.phone_popup_input_box()
        set_route.phone_popup_next()
        set_route.sms_code_inputbox()
        set_route.code_confirm_button()
        assert set_route.customers_phone() == data.PHONE_NUMBER   #OK

    #prueba 4 Agregar una tarjeta de crédito.
    def test_add_payment_method(self):  # Agregar tarjeta de credito como metodo de pago
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.payment_method_selector()
        set_route.click_on_add_new_cc()
        set_route.add_credit_card_number()
        set_route.cc_code_field()
        set_route.exit_payment_popup()
        assert set_route.user_payment_method() == data.CARD_NUMBER            #OK

    #prueba 5 Escribir un mensaje para el controlador.
    def test_special_instruction_for_service(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.comfort_fare_button()
        sleep(1)
        set_route.click_message_box_input()
        assert set_route.message_sent_to_driver() == data.MESSAGE_FOR_DRIVER   #OK

    # prueba 6 Pedir una manta y pañuelos.
    def test_ordering_blanket(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.comfort_fare_button()
        set_route.blanket_and_scarves()
        ## assert ######

    # # prueba 7 Pedir 2 helados.
    def test_add_icecream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        #sleep(1)
        set_route.comfort_fare_button()
        set_route.order_requirements()
        set_route.click_add_ice_cream_button()
        set_route.click_add_ice_cream_button()
        ## assert ######

    def test_waiting_for_taxi_modal(self):                                 # aparece modal para pedir taxi
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.comfort_fare_button()
        set_route.set_phone_input_box()
        set_route.phone_popup_input_box()
        set_route.phone_popup_next()
        set_route.sms_code_inputbox()
        set_route.code_confirm_button()
        set_route.click_order_taxi()
        sleep(10)
        ## assert ######

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()