"""
Version History Service
"""

from copy import deepcopy
from datetime import datetime


class VersionHistoryService:

    def __init__(self):

        self.history = []

    def add_version(
        self,
        detection: dict,
    ):

        version = {

            "Timestamp": datetime.utcnow().isoformat(),

            "Version": detection.get(
                "Version",
                "1.0",
            ),

            "Detection": deepcopy(
                detection
            ),

        }

        self.history.append(version)

        return version

    def get_history(self):

        return self.history


version_history_service = VersionHistoryService()