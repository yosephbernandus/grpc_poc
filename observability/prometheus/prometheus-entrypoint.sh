#!/bin/sh
envsubst < /etc/prometheus/prometheus.yml.template > /etc/prometheus/prometheus.yml
exec prometheus \
    --config.file=/etc/prometheus/prometheus.yml \
    --storage.tsdb.path=/prometheus \
    --storage.tsdb.retention.time=7d \
    --storage.tsdb.retention.size=1GB

