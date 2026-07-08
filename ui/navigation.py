"""
Enterprise Sidebar Navigation — v2
====================================
"""

import streamlit as st
from ui.design_system import (
    PLATFORM_NAME,
    PLATFORM_VERSION,
    PLATFORM_CLASSIFICATION,
    COMPANY,
    PREPARED_FOR,
)

SECTIONS = [
    {
        "label": "Customer Onboarding",
        "icon": "📋",
        "steps": [
            "Threat Model",
            "Application Analysis",
            "Coverage Analysis",
            "Detection Context",
            "Telemetry Analysis",
            "Telemetry Validation",
        ],
    },
    {
        "label": "Detection Engineering",
        "icon": "⚙️",
        "steps": [
            "Detection Planning",
            "AI Detection Generation",
            "Detection Review",
            "Detection Explanation",
        ],
    },
    {
        "label": "Deployment",
        "icon": "🚀",
        "steps": [
            "Approval",
            "Deployment Package",
        ],
    },
]

ALL_STEPS = []
for section in SECTIONS:
    ALL_STEPS.extend(section["steps"])


def _section_progress(section, current_step):
    start = 0
    for s in SECTIONS:
        if s is section:
            break
        start += len(s["steps"])
    total = len(section["steps"])
    completed = sum(1 for i in range(total) if start + i < current_step)
    return completed, total


def render():
    sb = st.sidebar

    # ── Brand Block ──
    sb.markdown(f"### 🛡️ {COMPANY}")
    sb.caption(PLATFORM_NAME)
    sb.caption(f"{PLATFORM_CLASSIFICATION}  ·  {PLATFORM_VERSION}  ·  {PREPARED_FOR}")
    sb.divider()

    current = st.session_state.step
    global_idx = 0

    for section in SECTIONS:
        completed, total = _section_progress(section, current)

        # Section header
        sb.markdown(f"**{section['icon']} {section['label']}**")

        # Section progress
        progress_val = completed / total if total > 0 else 0
        sb.progress(progress_val)

        pct = int(progress_val * 100)
        sb.caption(f"{pct}% · {completed} of {total}")

        # Steps
        for step_name in section["steps"]:
            if global_idx < current:
                prefix = "✅"
            elif global_idx == current:
                prefix = "▸"
                step_name = f"**{step_name}**"
            else:
                prefix = "　·"

            sb.markdown(f"&nbsp;&nbsp;{prefix} {step_name}")
            global_idx += 1

        sb.markdown("")

    sb.divider()

    # ── Overall ──
    overall = (current + 1) / len(ALL_STEPS)
    sb.progress(overall)
    sb.caption(f"Step {current + 1} of {len(ALL_STEPS)} · {int(overall * 100)}% complete")

    # ── Platform Knowledge ──
    sb.divider()
    sb.markdown("**📖 Platform Knowledge**")
    sb.caption("Architecture · Agents · Roadmap")
