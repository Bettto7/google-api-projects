from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date, timedelta

# Ruta al archivo de cuenta de servicio
KEY_PATH = 'C:\\Users\\acer nitro\\Downloads\\cuenta-servicio-gsc.json'

# Tu dominio verificado en GSC (¡con "https://"!)
SITE_URL = 'https://ejemplo.com/'


# Crear credenciales y servicio
creds = service_account.Credentials.from_service_account_file(KEY_PATH, scopes=[
    'https://www.googleapis.com/auth/webmasters.readonly'])

service = build('searchconsole', 'v1', credentials=creds)

# Definir fechas
end_date = date.today()
start_date = end_date - timedelta(days=7)

# Ejecutar consulta
request = {
    'startDate': str(start_date),
    'endDate': str(end_date),
    'dimensions': ['query'],
    'rowLimit': 10
}

response = service.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()

# Mostrar resultados
if 'rows' in response:
    for row in response['rows']:
        query = row['keys'][0]
        clicks = row['clicks']
        impressions = row['impressions']
        print(f"{query}: {clicks} clics, {impressions} impresiones")
else:
    print("No hay datos.")
