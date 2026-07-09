# OpenTelemetry

This example demonstrates how to export INNORIX transfer metrics using OpenTelemetry.

## Overview

The exporter retrieves transfer information from the INNORIX Platform and sends transfer metrics to an OpenTelemetry Collector using the OTLP protocol.

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
OpenTelemetry Exporter
        │
        ▼
OTLP Collector
        │
        ▼
Observability Platform
```

## Run

```bash
python exporter.py
```

Configure the collector endpoint in `.env`.

```text
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318/v1/metrics
```