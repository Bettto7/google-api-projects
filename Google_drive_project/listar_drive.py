from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo de credenciales
SERVICE_ACCOUNT_FILE = 'C:\\Users\\acer nitro\\Downloads\\cuenta-servicio-drive.json'

# Permisos que vamos a usar
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# Crear credenciales con cuenta de servicio
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# Inicializar servicio
service = build('drive', 'v3', credentials=creds)

# Obtener lista de archivos
results = service.files().list(
    pageSize=10,
    fields="files(id, name)"
).execute()

items = results.get('files', [])

if not items:
    print('No se encontraron archivos.')
else:
    print('Archivos encontrados:')
    for item in items:
        print(f"{item['name']} ({item['id']})")
