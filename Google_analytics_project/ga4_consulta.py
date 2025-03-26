from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2 import service_account

# Ruta al JSON de la cuenta de servicio
KEY_PATH = 'C:\\Users\\acer nitro\\Downloads\\cuenta-servicio-analytics.json'

# ID de tu propiedad GA4 (sin guiones)
PROPERTY_ID = '483578249'

# Crear cliente
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = BetaAnalyticsDataClient(credentials=credentials)

# Crear solicitud
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="country")],
    metrics=[Metric(name="activeUsers")],
    date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
)

response = client.run_report(request)

if not response.rows:
    print("No se devolvieron resultados. Puede que no haya datos recientes.")
else:
    for row in response.rows:
        print(f"{row.dimension_values[0].value}: {row.metric_values[0].value}")
