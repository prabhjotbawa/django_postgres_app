from prometheus_client.core import GaugeMetricFamily, REGISTRY
from django.db.utils import ProgrammingError

# Flag to track if the collector has been registered
COLLECTOR_REGISTERED = False


class ModelRowsCollector:
    def collect(self):
        from myapp.models import MyModel  # Import here to avoid circular imports

        try:
            count = MyModel.objects.count()
        except ProgrammingError:
            # Table doesn't exist yet (e.g. during migrations)
            count = 0

        g = GaugeMetricFamily(
            'data_inserted',
            'number of rows',
            value=count
        )
        yield g


# Function to register the collector if it hasn't been registered yet
def register_model_rows_collector():
    global COLLECTOR_REGISTERED
    if not COLLECTOR_REGISTERED:
        REGISTRY.register(ModelRowsCollector())
        COLLECTOR_REGISTERED = True
