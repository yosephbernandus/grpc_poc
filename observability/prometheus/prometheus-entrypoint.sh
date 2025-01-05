#!/bin/sh
sed -e "s|\${PROMETHEUS_ADDR}|$PROMETHEUS_ADDR|g" \
    -e "s|\${DJANGO_GRPC_ADDR}|$DJANGO_GRPC_ADDR|g" \
    -e "s|\${NODE_EXPORTER_ADDR}|$NODE_EXPORTER_ADDR|g" \
    /etc/prometheus/prometheus.yml.template > /etc/prometheus/prometheus.yml

exec prometheus \
    --config.file=/etc/prometheus/prometheus.yml \
    --storage.tsdb.path=/prometheus \
    --storage.tsdb.retention.time=7d \
    --storage.tsdb.retention.size=1GB

