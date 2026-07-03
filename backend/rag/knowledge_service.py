"""
Knowledge Service

Simple RAG for AI Detection Engineering.
"""

from pathlib import Path


class KnowledgeService:

    def __init__(self):

        self.knowledge_dir = Path("knowledge")

    def retrieve(self, search_text: str):

        search_text = search_text.lower()

        knowledge = []

        sources = []

        if not self.knowledge_dir.exists():

            return "", []

        for file in self.knowledge_dir.rglob("*.md"):

            filename = file.stem.lower()

            score = 0

            for word in filename.replace("-", "_").split("_"):

                if word in search_text:

                    score += 1

            if score > 0:

                knowledge.append(
                    file.read_text(
                        encoding="utf-8"
                    )
                )

                sources.append(file.relative_to(self.knowledge_dir).as_posix())

        return "\n\n".join(knowledge), sources

    def load_kql_knowledge(self):

        folder = self.knowledge_dir / "kql"

        knowledge = []

        sources = []

        if not folder.exists():

            return "", []

        for file in sorted(folder.glob("*.md")):

            knowledge.append(
                file.read_text(
                    encoding="utf-8"
                )
            )

            sources.append(file.name)

        return "\n\n".join(knowledge), sources


knowledge_service = KnowledgeService()