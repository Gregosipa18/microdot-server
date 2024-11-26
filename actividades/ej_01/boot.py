# Configuración de red para conexión inicial
def initialize_connection():
    import network
    wifi_interface = network.WLAN(network.STA_IF)

    if not wifi_interface.isconnected():
        print('Intentando conectar a la red...')
        wifi_interface.active(True)
        wifi_interface.connect('Cooperadora Alumnos', '')
        
        while not wifi_interface.isconnected():
            continue  # Espera activa hasta conectarse

    print('Configuración de red establecida:', wifi_interface.ifconfig())
