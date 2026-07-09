import os
import requests

from dotenv import load_dotenv

load_dotenv()


class INNORIXClient:

    def __init__(self):

        self.base_url = os.getenv("INNORIX_BASE_URL").rstrip("/")
        self.api_key = os.getenv("INNORIX_API_KEY")

        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    # ---------------------------------------------------------
    # Unified Transfer
    # ---------------------------------------------------------

    def get_unified_transfer_list(
        self,
        automation_id,
        limit=100,
        cursor=None,
        search_keyword=None,
        status_filter=None,
        type_filter=None
    ):

        params = {
            "automationId": automation_id,
            "limit": limit
        }

        if cursor:
            params["cursor"] = cursor

        if search_keyword:
            params["searchKeyword"] = search_keyword

        if status_filter:
            params["statusFilter"] = status_filter

        if type_filter:
            params["typeFilter"] = type_filter

        response = self.session.get(
            f"{self.base_url}/api/transfer/unified-by-automation",
            params=params
        )

        response.raise_for_status()

        return response.json()

    # ---------------------------------------------------------
    # Metrics
    # ---------------------------------------------------------

    def get_transfer_metrics(
        self,
        automation_id,
        limit=100
    ):

        result = self.get_unified_transfer_list(
            automation_id=automation_id,
            limit=limit,
            type_filter="automation,monitor,history"
        )

        items = result.get("data", [])

        metrics = {
            "transfer_total": len(items),
            "transfer_queued": 0,
            "transfer_running": 0,
            "transfer_completed": 0,
            "transfer_failed": 0,
            "transfer_paused": 0,
            "transfer_cancelled": 0,
            "transfer_retry": 0,
            "transfer_skipped": 0
        }

        for item in items:

            status = item.get("status")

            if status in (-1, 0):
                metrics["transfer_queued"] += 1

            elif status in (1, 6):
                metrics["transfer_running"] += 1

            elif status == 2:
                metrics["transfer_completed"] += 1

            elif status == 3:
                metrics["transfer_paused"] += 1

            elif status == 5:
                metrics["transfer_cancelled"] += 1

            elif status == 7:
                metrics["transfer_skipped"] += 1

            elif status == 8:
                metrics["transfer_retry"] += 1

            elif status in (4, 99):
                metrics["transfer_failed"] += 1

        return metrics

    # ---------------------------------------------------------
    # Transfer Detail
    # ---------------------------------------------------------

    def get_transfer_detail(
        self,
        transfer_id,
        workspace_id=None,
        id_type="transfer"
    ):

        params = {
            "idType": id_type
        }

        if workspace_id:
            params["workSpaceId"] = workspace_id

        response = self.session.get(
            f"{self.base_url}/api/transfer-history/{transfer_id}/detail",
            params=params
        )

        response.raise_for_status()

        return response.json()

    # ---------------------------------------------------------
    # Transfer Files
    # ---------------------------------------------------------

    def get_transfer_files(
        self,
        transfer_id,
        page=1,
        size=10,
        current_path=None,
        workspace_id=None,
        id_type="transfer"
    ):

        params = {
            "page": page,
            "size": size,
            "idType": id_type
        }

        if current_path:
            params["current_path"] = current_path

        if workspace_id:
            params["workSpaceId"] = workspace_id

        response = self.session.get(
            f"{self.base_url}/api/transfer-history/{transfer_id}/get-files",
            params=params
        )

        response.raise_for_status()

        return response.json()