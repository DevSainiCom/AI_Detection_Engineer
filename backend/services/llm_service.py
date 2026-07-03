from backend.core.openai_client import openai_client


class LLMService:
    """
    Sends prompts to the LLM.
    """

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        return openai_client.generate(
            system_prompt,
            user_prompt,
        )


llm_service = LLMService()