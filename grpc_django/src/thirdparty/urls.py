from django.urls import path

from thirdparty import metrics

urlpatterns = [
    path("", metrics.metrics_view, name="metrics"),
]
