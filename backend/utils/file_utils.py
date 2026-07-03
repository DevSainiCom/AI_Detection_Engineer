from pathlib import Path
from datetime import datetime


OUTPUT_DIR = Path("outputs")

OUTPUT_DIR.mkdir(exist_ok=True)


def save_detection(
    detection: str,
    filename: str = "sentinel_detection",
):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = OUTPUT_DIR / f"{filename}_{timestamp}.json"

    file_path.write_text(
        detection,
        encoding="utf-8"
    )

    return file_path