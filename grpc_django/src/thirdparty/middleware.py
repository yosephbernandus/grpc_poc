import time
import logging
from prometheus_client import Counter, Histogram

from thirdparty.metrics import REQUEST_COUNT, REQUEST_LATENCY

logger = logging.getLogger("django")


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


class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(
            f"API Request: {request.method} {request.path} - Headers: {dict(request.headers)}"
        )
        response = self.get_response(request)
        return response
