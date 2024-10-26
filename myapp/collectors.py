from prometheus_client.core import GaugeMetricFamily, REGISTRY


class ModelRowsCollector:
    def __init__(self):
        pass

    def collect(self):
        # This method is called each time the metrics endpoint is hit
        from myapp.models import MyModel  # Import here to avoid circular imports

        g = GaugeMetricFamily(
            'data_inserted',
            'number of rows',
            value=MyModel.objects.count()
        )
        yield g


# Register the collector
REGISTRY.register(ModelRowsCollector())
