from pydantic import BaseModel


class DetectionRequest(BaseModel):
    """
    User request for generating a Sentinel detection.
    """

    attack_description: str