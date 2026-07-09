import os
import time

from client import INNORIXClient

client = INNORIXClient()


def export_metrics():

    metrics = client.get_transfer_metrics(
        automation_id=os.getenv("AUTOMATION_ID")
    )

    payload = {
        "resource": {
            "service.name": "innorix",
            "service.namespace": "transfer"
        },
        "metrics": [
            {
                "name": "innorix.transfer.total",
                "value": metrics["transfer_total"]
            },
            {
                "name": "innorix.transfer.running",
                "value": metrics["transfer_running"]
            },
            {
                "name": "innorix.transfer.completed",
                "value": metrics["transfer_completed"]
            },
            {
                "name": "innorix.transfer.failed",
                "value": metrics["transfer_failed"]
            },
            {
                "name": "innorix.transfer.queued",
                "value": metrics["transfer_queued"]
            },
            {
                "name": "innorix.transfer.retry",
                "value": metrics["transfer_retry"]
            }
        ]
    }

    print("Exporting metrics to OpenTelemetry...")
    print(payload)

    # TODO:
    # Send payload to OTLP Collector
    # Endpoint:
    # OTEL_EXPORTER_OTLP_ENDPOINT


if __name__ == "__main__":

    print("INNORIX OpenTelemetry Exporter started.")

    while True:

        export_metrics()

        time.sleep(5)