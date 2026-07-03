"""
MITRE ATT&CK Mapping Service
"""


class MITREMappingService:

    MITRE_MAP = {

        "password spray": {
            "tactics": [
                "Credential Access"
            ],
            "techniques": [
                "T1110.003"
            ],
        },

        "kerberoasting": {
            "tactics": [
                "Credential Access"
            ],
            "techniques": [
                "T1558.003"
            ],
        },

        "golden ticket": {
            "tactics": [
                "Defense Evasion",
                "Persistence"
            ],
            "techniques": [
                "T1558.001"
            ],
        },

        "powershell": {
            "tactics": [
                "Execution"
            ],
            "techniques": [
                "T1059.001"
            ],
        }

    }

    def map(
        self,
        attack_description: str,
    ):

        attack = attack_description.lower()

        for keyword, mapping in self.MITRE_MAP.items():

            if keyword in attack:

                return mapping

        return {

            "tactics": [],

            "techniques": [],

        }


mitre_mapping_service = MITREMappingService()