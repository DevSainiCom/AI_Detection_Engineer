"""
DREAD Scoring Service
======================
Auto-calculates DREAD threat scores from use case and threat model inputs.
Feeds into alert severity, UC prioritisation, and detection framework.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DREADScore:
    damage:          int   # 1-10  How bad is the damage if exploited?
    reproducibility: int   # 1-10  How easy to reproduce?
    exploitability:  int   # 1-10  How easy to exploit?
    affected_users:  int   # 1-10  How many users affected?
    discoverability: int   # 1-10  How easy to discover?

    @property
    def total(self) -> float:
        return (
            self.damage +
            self.reproducibility +
            self.exploitability +
            self.affected_users +
            self.discoverability
        ) / 5

    @property
    def rating(self) -> str:
        t = self.total
        if t >= 8:   return "Critical"
        if t >= 6:   return "High"
        if t >= 4:   return "Medium"
        return "Low"

    @property
    def severity_color(self) -> str:
        return {
            "Critical": "red",
            "High":     "orange",
            "Medium":   "amber",
            "Low":      "green",
        }[self.rating]

    @property
    def alert_severity(self) -> str:
        return {
            "Critical": "High",
            "High":     "High",
            "Medium":   "Medium",
            "Low":      "Low",
        }[self.rating]

    def to_dict(self) -> dict:
        return {
            "Damage":          self.damage,
            "Reproducibility": self.reproducibility,
            "Exploitability":  self.exploitability,
            "AffectedUsers":   self.affected_users,
            "Discoverability": self.discoverability,
            "Total":           round(self.total, 1),
            "Rating":          self.rating,
            "AlertSeverity":   self.alert_severity,
        }


# ── MITRE → default DREAD profiles ──────────────────────────────────
# Based on industry threat intelligence for common attack patterns.
# Overridden by context from threat model / application criticality.

_MITRE_PROFILES = {
    # Credential attacks
    "T1110":    DREADScore(8, 9, 8, 8, 9),   # Password Guessing
    "T1110.003":DREADScore(9, 9, 8, 9, 9),   # Password Spray
    "T1110.001":DREADScore(7, 8, 7, 7, 8),   # Password Brute-Force
    "T1556":    DREADScore(9, 6, 7, 9, 7),   # MFA Bypass
    # Privilege / Access
    "T1078":    DREADScore(9, 7, 7, 9, 7),   # Valid Accounts
    "T1078.002":DREADScore(10,6, 7, 10,7),   # Domain Accounts
    "T1078.004":DREADScore(9, 6, 7, 9, 7),   # Cloud Accounts
    "T1068":    DREADScore(10,5, 6, 10,6),   # Privilege Escalation
    # Lateral Movement
    "T1021":    DREADScore(9, 7, 7, 9, 7),   # Remote Services
    "T1550":    DREADScore(10,6, 7, 10,7),   # Pass-the-Hash/Ticket
    # Credential Dumping
    "T1003":    DREADScore(10,5, 6, 10,6),   # OS Credential Dumping
    "T1003.001":DREADScore(10,5, 6, 10,6),   # LSASS Memory
    "T1003.003":DREADScore(10,4, 5, 10,5),   # NTDS
    "T1558.003":DREADScore(9, 5, 6, 9, 6),   # Kerberoasting
    # Execution
    "T1059":    DREADScore(8, 8, 8, 8, 8),   # Command Scripting
    "T1218":    DREADScore(7, 7, 7, 7, 7),   # LOLBins
    # Exfiltration
    "T1048":    DREADScore(9, 6, 6, 9, 5),   # Exfil over C2
    "T1530":    DREADScore(8, 7, 7, 8, 6),   # Data from Cloud Storage
    # C2
    "T1071":    DREADScore(9, 7, 7, 9, 6),   # App Layer Protocol
    "T1071.004":DREADScore(8, 7, 7, 8, 5),   # DNS Tunnelling
    # Impact
    "T1486":    DREADScore(10,5, 6, 10,7),   # Ransomware
    "T1562.002":DREADScore(9, 6, 7, 9, 7),   # Disable Event Logging
    # Web
    "T1505.003":DREADScore(10,6, 7, 10,8),   # Web Shell
    "T1190":    DREADScore(9, 7, 7, 9, 8),   # Public-Facing App Exploit
}

_CRITICALITY_MULTIPLIER = {
    "Critical": 1.0,
    "High":     0.95,
    "Medium":   0.85,
    "Low":      0.75,
}

_CATEGORY_BASE = {
    "Compliance Monitoring": DREADScore(7, 7, 6, 7, 7),
    "Threat Detection":      DREADScore(8, 7, 7, 8, 7),
    "Health Monitoring":     DREADScore(5, 8, 8, 6, 8),
}


class DREADScoringService:

    def score_from_mitre(
        self,
        mitre_technique: str,
        business_criticality: str = "High",
        uc_category: Optional[str] = None,
    ) -> DREADScore:
        """
        Return DREAD score for a MITRE technique.
        Adjusted by business criticality of the application.
        """
        base = _MITRE_PROFILES.get(
            mitre_technique,
            _CATEGORY_BASE.get(uc_category, DREADScore(6,6,6,6,6))
        )

        mult = _CRITICALITY_MULTIPLIER.get(business_criticality, 0.9)

        def adj(v): return min(10, max(1, round(v * mult)))

        return DREADScore(
            damage          = adj(base.damage          * (1.1 if business_criticality == "Critical" else 1.0)),
            reproducibility = base.reproducibility,
            exploitability  = base.exploitability,
            affected_users  = adj(base.affected_users  * (1.1 if business_criticality == "Critical" else 1.0)),
            discoverability = base.discoverability,
        )

    def score_from_inputs(
        self,
        damage:          int,
        reproducibility: int,
        exploitability:  int,
        affected_users:  int,
        discoverability: int,
    ) -> DREADScore:
        """Manual score from individual dimension inputs (1-10)."""
        return DREADScore(
            damage          = damage,
            reproducibility = reproducibility,
            exploitability  = exploitability,
            affected_users  = affected_users,
            discoverability = discoverability,
        )

    def score_use_case(
        self,
        uc_name: str,
        mitre_technique: str,
        business_criticality: str,
        uc_category: str,
        data_classification: str = "Confidential",
    ) -> DREADScore:
        """
        Full UC scoring — combines MITRE profile, business criticality,
        data classification, and UC category.
        """
        score = self.score_from_mitre(
            mitre_technique, business_criticality, uc_category
        )

        # Boost affected_users if data classification is high
        if data_classification in ("Restricted", "Confidential"):
            score = DREADScore(
                damage          = min(10, score.damage + 1),
                reproducibility = score.reproducibility,
                exploitability  = score.exploitability,
                affected_users  = min(10, score.affected_users + 1),
                discoverability = score.discoverability,
            )

        return score


dread_scoring_service = DREADScoringService()
