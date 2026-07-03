from pathlib import Path


class RuleLibraryService:

    def __init__(self):

        self.rule_dir = Path("knowledge/rules")

    def retrieve(
        self,
        attack_description: str,
    ) -> str:

        attack = attack_description.lower()

        rules = []

        if not self.rule_dir.exists():

            return ""

        for file in self.rule_dir.glob("*.md"):

            name = file.stem.lower().replace("_", " ")

            if any(
                word in attack
                for word in name.split()
            ):

                rules.append(
                    file.read_text(
                        encoding="utf-8"
                    )
                )

        return "\n\n".join(rules)


rule_library_service = RuleLibraryService()