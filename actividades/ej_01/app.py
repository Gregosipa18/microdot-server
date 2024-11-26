# Aplicacion del servidor
# Servidor básico para entregar archivos
from boot import initialize_connection
from microdot import Microdot, send_file

# Conexión inicial
initialize_connection()

# Configuración de la aplicación
server = Microdot()

@server.route('/')
async def home(request):
    return send_file('index.html')

@server.route('/<folder>/<filename>')
async def serve_files(request, folder, filename):
    file_path = f"{folder}/{filename}"
    return send_file(file_path)

# Ejecutar servidor en el puerto 80
server.run(port=80)
