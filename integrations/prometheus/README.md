# Prometheus

This example demonstrates how to export INNORIX transfer metrics for Prometheus.

## Overview

The exporter retrieves transfer information from the INNORIX Platform and exposes metrics through a Prometheus-compatible `/metrics` endpoint.

## Exported Metrics

- Total Transfers
- Queued Transfers
- Running Transfers
- Completed Transfers
- Failed Transfers
- Paused Transfers
- Cancelled Transfers
- Retry Transfers
- Skipped Transfers

## Workflow

```text
INNORIX Platform
        │
Transfer API
        │
        ▼
Prometheus Exporter
        │
        ▼
/metrics
        │
        ▼
Prometheus Server
```

## Run

```bash
python exporter.py
```

By default, metrics are available at:

```text
http://localhost:8000/metrics
```