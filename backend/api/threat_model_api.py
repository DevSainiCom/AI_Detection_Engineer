"""
Threat Model API

Acts as the interface between the UI and the
Threat Model Service.
"""

from backend.schemas.threat_model_request import (
    ThreatModelRequest,
)
from backend.schemas.threat_model_response import (
    ThreatModelResponse,
)
from backend.services.threat_model_service import (
    threat_model_service,
)


class ThreatModelAPI:
    """
    API layer for Threat Model generation.
    """

    def generate(
        self,
        request: ThreatModelRequest,
    ) -> ThreatModelResponse:

        return threat_model_service.generate(request)


threat_model_api = ThreatModelAPI()