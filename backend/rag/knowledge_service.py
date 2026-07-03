from pathlib import Path


class KnowledgeService:
    """
    Simple Retrieval-Augmented Generation (RAG)
    using Markdown files.
    """

    def __init__(self):

        self.knowledge_dir = Path("knowledge")

    def retrieve(self, search_text: str):
        """
        Retrieve relevant knowledge files based on
        keywords found in the provided search text.
        """

        search_text = search_text.lower()

        knowledge = []
        sources = []

        if not self.knowledge_dir.exists():
            return "", []

        for file in self.knowledge_dir.glob("*.md"):

            filename = file.stem.lower()

            score = 0

            for word in filename.replace("-", "_").split("_"):

                if word in search_text:
                    score += 1

            if score > 0:

                knowledge.append(
                    file.read_text(encoding="utf-8")
                )

                sources.append(file.name)

        return "\n\n".join(knowledge), sources


knowledge_service = KnowledgeService()