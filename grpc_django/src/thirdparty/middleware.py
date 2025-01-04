import time
from prometheus_client import Counter, Histogram

from thirdparty.metrics import REQUEST_COUNT, REQUEST_LATENCY


class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Start the timer
        start_time = time.time()

        # Count the request
        REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()

        response = self.get_response(request)

        # Measure latency
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)

        return response
