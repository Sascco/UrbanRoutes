
from selenium.webdriver.common.by import By

class locators:                                                                                              # Localizadores usados:

    from_field = (By.ID, 'from')                                                                                    #Casilla para ingrear dirección de origen
    to_field = (By.ID, 'to')                                                                                        #Casilla para ingrear direccion de destino
    book_a_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')                #Boton para pedir taxi
    comfort_fare = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')                  #Icono para seleccionar la tarifa comfort
    phone_input_box = (By.CLASS_NAME, "np-button")                                                                  #Casilla para ingresar telefono en menu inicial
    add_phone_input_box = (By.ID, "phone")                                                                          #Casilla para ingresar No. de Telefono en ventana emergente
    next_button_phone_popup_window = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')      #Boton Siguiente en ventana emergente para ingresar telefono
    add_SMS_input_box = (By. XPATH, '//*[@id="code"]')                                                              #Casilla para ingrear el codigo SMS despues de ingresar telefono
    add_sms_code = (By.ID, "code")                                                                                  #Casilla para ingresar SMS y terminar registro telefono
    confirm_button_sms = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')               #Boton de confirmar el codigo en la ventana para ingresar SMS
    payment_method_box = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[2]')                #Boton para agregar medio de pago
    add_cc_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div')                 #Boton signo "+" para agregar tarjeta como medio de pago
    click_cc_input_number = (By.CLASS_NAME, 'card-number-input')
    add_cc_number = (By.ID, "number")                                                                               #Casilla para agregar tarjeta en ventana emergente
    add_code_input_box = (By.XPATH, "(//input[@id='code'])[2]")                                                     #Casilla para agregar código de tarjeta de credito
    add_payment_method_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')        #Boton para agregar tarjeta como medio de pago
    exit_payment_popup_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/button')                       #Boton para cerrar ventana emergente para agregar tarjeta como medio de pago
    click_message_box = (By.ID, "comment")                                                                          #Casilla para ingresar mensaje para el conductor, se importa desde data.py
    order_requirements_menu = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]')
    blanket_and_scarves_request = (By.XPATH, "(//span[@class='slider round'])[1]")                                                   #Toggle para seleccionar manta y pañuelos como requerimiento para el viaje
    add_ice_cream_button = (By.XPATH, "(//div[@class='counter-plus'])[1]")                                          #Counter for icecream - terminar localizadores y revisar metodos y funciones.
    book_service = (By.XPATH, "(//button[@type='button']//span)[1]")