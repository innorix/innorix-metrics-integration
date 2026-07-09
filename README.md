# INNORIX Metrics Integration

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Prometheus](https://img.shields.io/badge/Prometheus-Supported-E6522C)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Supported-425CC7)
![License](https://img.shields.io/badge/License-Commercial-red)
![Status](https://img.shields.io/badge/Status-Official-success)

Official integration examples for exporting INNORIX transfer metrics to Prometheus and OpenTelemetry.

## Supported Platforms

- Prometheus
- OpenTelemetry

## Features

- Retrieve transfer metrics using the INNORIX REST API
- Export transfer metrics for observability platforms
- Monitor transfer status in real time
- Integrate with Prometheus and OpenTelemetry
- Build dashboards and alerts using transfer metrics

## Repository Structure

```text
.
├── client.py
└── integrations/
    ├── prometheus/
    └── opentelemetry/
```

## Workflow

```text
INNORIX Platform
        │
Transfer API
        │
        ▼
Metrics Exporter
        │
        ├── Prometheus
        └── OpenTelemetry
```

## Metrics

- Total Transfers
- Queued Transfers
- Running Transfers
- Completed Transfers
- Failed Transfers
- Paused Transfers
- Cancelled Transfers
- Retry Transfers
- Skipped Transfers

## Requirements

- Python 3.10+
- INNORIX Platform
- INNORIX API Key
- Prometheus or OpenTelemetry

## Installation

```bash
pip install -r requirements.txt
```

Copy the example configuration.

```bash
cp .env.example .env
```

Update the configuration.

```text
INNORIX_BASE_URL=
INNORIX_API_KEY=
AUTOMATION_ID=
```

Run an exporter.

### Prometheus

```bash
cd integrations/prometheus

python exporter.py
```

### OpenTelemetry

```bash
cd integrations/opentelemetry

python exporter.py
```

## License

Commercial License

Copyright © INNORIX Co., Ltd. All rights reserved.