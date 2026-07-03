from backend.schemas.detection_request import DetectionRequest
from backend.services.detection_service import detection_service
from backend.utils.file_utils import save_detection


def main():
    print("=" * 70)
    print("              AI Detection Engineer")
    print("=" * 70)

    attack_description = input(
        "\nDescribe the attack you want to detect:\n\n> "
    )

    request = DetectionRequest(
        attack_description=attack_description
    )

    print("\nGenerating Microsoft Sentinel Detection...\n")

    try:
        response = detection_service.generate_detection(request)

        file_path = save_detection(
            detection=response,
            filename="sentinel_detection"
        )

        print("=" * 70)
        print("Detection Generated Successfully")
        print("=" * 70)

        print(response)

        print("\n" + "=" * 70)
        print(f"Detection saved to:\n{file_path}")
        print("=" * 70)

    except Exception as ex:
        print("\nERROR")
        print("-" * 70)
        print(ex)


if __name__ == "__main__":
    main()