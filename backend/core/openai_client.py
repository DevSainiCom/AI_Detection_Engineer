from openai import OpenAI

from backend.core.config import settings


class OpenAIClient:
    """
    Wrapper around the OpenAI Responses API.
    """

    def __init__(self):

        if not settings.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found."
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        response = self.client.responses.create(
            model=settings.MODEL_NAME,
            instructions=system_prompt,
            input=user_prompt,
        )

        return response.output_text


openai_client = OpenAIClient()