from prometheus_client.core import GaugeMetricFamily, REGISTRY
from django.db.utils import ProgrammingError


class ModelRowsCollector:
    def __init__(self):
        pass

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


# Register the collector
REGISTRY.register(ModelRowsCollector())