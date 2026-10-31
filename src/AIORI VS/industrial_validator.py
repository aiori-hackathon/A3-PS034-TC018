
import json
import re
from pathlib import Path
from decimal import Decimal
from yangson import DataModel

BASE_DIR = Path(__file__).parent

# Load our demonstration YANG model
model = DataModel.from_file(
    str(BASE_DIR / "yang-library.json"),
    [str(BASE_DIR)]
)


def validate_yang(data):
    try:
        validation_data = data.copy()

        decimal_fields = [
            "temperature_c",
            "current_a",
            "vibration_mm_s"
        ]

        for field in decimal_fields:
            validation_data[field] = str(validation_data[field])

        root = model.from_raw({
            "telemetry-demo:telemetry": validation_data
        })

        root.validate()

        return True, "YANG validation successful"

    except Exception as error:
        print("ERROR TYPE:", type(error).__name__)
        print("FULL ERROR:", repr(error))

        return False, f"{type(error).__name__}: {error}"


def safe_correction(data):
    corrected = data.copy()
    changes = []

    # Only correct an exact, predefined RPM format.
    rpm = corrected.get("rpm")

    if isinstance(rpm, str):
        match = re.fullmatch(r"([0-9]+)rpm", rpm)

        if match:
            corrected["rpm"] = int(match.group(1))
            changes.append("Converted RPM text to integer")

    return corrected, changes


# Simulated industrial motor notifications
notifications = [
    {
        "device": "Motor-01",
        "temperature_c": 72.5,
        "current_a": 4.2,
        "rpm": 1450,
        "vibration_mm_s": 3.2
    },
    {
        "device": "Motor-02",
        "temperature_c": 68.4,
        "current_a": 3.8,
        "rpm": "1450rpm",
        "vibration_mm_s": 2.8
    },
    {
        "device": "Motor-03",
        "temperature_c": "hello",
        "current_a": 4.5,
        "rpm": 1400,
        "vibration_mm_s": 3.5
    },
    {
        "device": "Motor-04",
        "temperature_c": 75.0,
        "current_a": 5.1,
        "rpm": 1500,
        "vibration_mm_s": 2.5
    }
]

accepted = []
rejected = []

for notification in notifications:

    print("\nProcessing:", notification["device"])

    # First validation
    valid, reason = validate_yang(notification)

    if valid:
        accepted.append({
            "notification": notification,
            "status": "Accepted",
            "correction": "None"
        })
        print("ACCEPTED:", reason)
        continue

    print("Initial validation failed:", reason)

    # Try only predefined safe corrections
    corrected, changes = safe_correction(notification)

    if changes:
        print("Correction:", changes)

        # Validate corrected data again
        valid_again, reason_again = validate_yang(corrected)

        if valid_again:
            accepted.append({
                "notification": corrected,
                "status": "Accepted after correction",
                "correction": ", ".join(changes)
            })
            print("REVALIDATION SUCCESS:", reason_again)
            continue

        print("Revalidation failed:", reason_again)

    # Reject data that cannot be safely recovered
    rejected.append({
        "notification": notification,
        "reason": reason,
        "status": "Rejected / Quarantined"
    })

    print("REJECTED:", notification["device"])


# Save accepted records
with open(BASE_DIR / "industrial_accepted.jsonl", "w",
          encoding="utf-8") as file:
    for item in accepted:
        file.write(json.dumps(item) + "\n")


# Save rejected records
with open(BASE_DIR / "industrial_rejected.jsonl", "w",
          encoding="utf-8") as file:
    for item in rejected:
        file.write(json.dumps(item) + "\n")


print("\n========== PIPELINE SUMMARY ==========")
print("Accepted:", len(accepted))
print("Rejected:", len(rejected))
print("Total:", len(notifications))
print("Accepted file: industrial_accepted.jsonl")
print("Rejected file: industrial_rejected.jsonl")
