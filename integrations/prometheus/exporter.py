from flask import Flask, Response
import os

from client import INNORIXClient

app = Flask(__name__)

client = INNORIXClient()


@app.route("/metrics")
def metrics():

    data = client.get_transfer_metrics(
        automation_id=os.getenv("AUTOMATION_ID")
    )

    output = []

    output.append("# HELP innorix_transfer_total Total transfers")
    output.append("# TYPE innorix_transfer_total gauge")
    output.append(f"innorix_transfer_total {data['transfer_total']}")

    output.append("# HELP innorix_transfer_queued Queued transfers")
    output.append("# TYPE innorix_transfer_queued gauge")
    output.append(f"innorix_transfer_queued {data['transfer_queued']}")

    output.append("# HELP innorix_transfer_running Running transfers")
    output.append("# TYPE innorix_transfer_running gauge")
    output.append(f"innorix_transfer_running {data['transfer_running']}")

    output.append("# HELP innorix_transfer_completed Completed transfers")
    output.append("# TYPE innorix_transfer_completed gauge")
    output.append(f"innorix_transfer_completed {data['transfer_completed']}")

    output.append("# HELP innorix_transfer_failed Failed transfers")
    output.append("# TYPE innorix_transfer_failed gauge")
    output.append(f"innorix_transfer_failed {data['transfer_failed']}")

    output.append("# HELP innorix_transfer_paused Paused transfers")
    output.append("# TYPE innorix_transfer_paused gauge")
    output.append(f"innorix_transfer_paused {data['transfer_paused']}")

    output.append("# HELP innorix_transfer_cancelled Cancelled transfers")
    output.append("# TYPE innorix_transfer_cancelled gauge")
    output.append(f"innorix_transfer_cancelled {data['transfer_cancelled']}")

    output.append("# HELP innorix_transfer_retry Retry transfers")
    output.append("# TYPE innorix_transfer_retry gauge")
    output.append(f"innorix_transfer_retry {data['transfer_retry']}")

    output.append("# HELP innorix_transfer_skipped Skipped transfers")
    output.append("# TYPE innorix_transfer_skipped gauge")
    output.append(f"innorix_transfer_skipped {data['transfer_skipped']}")

    return Response(
        "\n".join(output),
        mimetype="text/plain"
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8000
    )