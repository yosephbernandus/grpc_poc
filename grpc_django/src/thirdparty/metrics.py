from prometheus_client import Counter, Histogram, Gauge, generate_latest
from prometheus_client.core import CollectorRegistry
from django.http import HttpResponse
import psutil  # system metrics memory and CPU usage
import time

# Create a registry
registry = CollectorRegistry()

# Define metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"],
    registry=registry,
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["endpoint"],
    registry=registry,
)

# CURRENT_ACTIVE_USERS = Gauge(
#     "active_users_count", "Number of active users", registry=registry
# )

CPU_USAGE = Gauge(
    "system_cpu_usage_percent", "CPU usage in percentage", registry=registry
)

MEMORY_USAGE = Gauge(
    "system_memory_usage_percent", "Memory usage in percentage", registry=registry
)


def metrics_view(request):
    """Expose metrics for Prometheus scraping."""
    # Example of updating gauge metrics
    CPU_USAGE.set(psutil.cpu_percent())  # CPU usage
    MEMORY_USAGE.set(psutil.virtual_memory().percent)  # Memory usage

    # from django.contrib.sessions.models import Session
    #
    # CURRENT_ACTIVE_USERS.set(Session.objects.count())
    #
    # Generate and return metrics
    data = generate_latest(registry)
    return HttpResponse(data, content_type="text/plain")
