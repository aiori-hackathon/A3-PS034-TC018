
import json
from pathlib import Path
import subprocess
import sys

import streamlit as st
from yangson import DataModel

st.set_page_config(
    page_title="AIORI-3 Industrial Telemetry Dashboard",
    page_icon="📡",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

ACCEPTED_FILE = BASE_DIR / "industrial_accepted.jsonl"
REJECTED_FILE = BASE_DIR / "industrial_rejected.jsonl"


def read_json_lines(path):
    records = []

    if path.exists():
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    return records

# Run the industrial telemetry validator
result = subprocess.run(
    [sys.executable, str(BASE_DIR / "industrial_validator.py")],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    st.error("Validator execution failed.")
    st.code(result.stderr)

# Load actual validator output
accepted = read_json_lines(ACCEPTED_FILE)
rejected = read_json_lines(REJECTED_FILE)

total = len(accepted) + len(rejected)

st.title("📡 AIORI-3 Industrial Telemetry Dashboard")

st.caption(
    "Beyond Limits | PS-034 | Schema-Validated YANG-Push Telemetry Pipeline"
)

st.info(
    "Industrial motor telemetry simulation with YANG schema validation, "
    "predefined safe correction, revalidation and rejection."
)

if st.button("🔄 Refresh Dashboard"):
    st.rerun()

st.divider()

# Main statistics
st.subheader("📊 Pipeline Overview")

col1, col2, col3 = st.columns(3)

col1.metric("✅ Accepted", len(accepted))
col2.metric("❌ Rejected", len(rejected))
col3.metric("📨 Total Processed", total)

if total > 0:
    accepted_rate = len(accepted) / total * 100
    rejected_rate = len(rejected) / total * 100

    col1, col2 = st.columns(2)
    col1.metric("Accepted Rate", f"{accepted_rate:.1f}%")
    col2.metric("Rejected Rate", f"{rejected_rate:.1f}%")

st.divider()

# Accepted notifications
st.subheader("✅ Accepted Motor Notifications")

if accepted:
    accepted_rows = []

    for item in accepted:
        data = item.get("notification", {})

        accepted_rows.append({
            "Device": data.get("device", "Unknown"),
            "Temperature (°C)": data.get("temperature_c"),
            "Current (A)": data.get("current_a"),
            "RPM": data.get("rpm"),
            "Vibration (mm/s)": data.get("vibration_mm_s"),
            "Status": item.get("status", "Accepted"),
            "Correction": item.get("correction", "None")
        })

    st.dataframe(
        accepted_rows,
        use_container_width=True,
        hide_index=True
    )
else:
    st.warning("No accepted motor notifications found.")

st.divider()

# Rejected notifications
st.subheader("❌ Rejected / Quarantined Notifications")

if rejected:
    rejected_rows = []

    for item in rejected:
        data = item.get("notification", {})

        rejected_rows.append({
            "Device": data.get("device", "Unknown"),
            "Temperature (°C)": data.get("temperature_c"),
            "Current (A)": data.get("current_a"),
            "RPM": data.get("rpm"),
            "Vibration (mm/s)": data.get("vibration_mm_s"),
            "Rejection Reason": item.get("reason", "Not recorded"),
            "Status": item.get("status", "Rejected")
        })

    st.dataframe(
        rejected_rows,
        use_container_width=True,
        hide_index=True
    )
else:
    st.success("No rejected notifications found.")

st.divider()

# Validation chart
st.subheader("📈 Validation Results")

if total > 0:
    chart_data = {
        "Status": ["Accepted", "Rejected"],
        "Notifications": [len(accepted), len(rejected)]
    }

    st.bar_chart(
        chart_data,
        x="Status",
        y="Notifications",
        horizontal=True
    )

st.divider()

# Industrial telemetry details
st.subheader("⚙️ Motor Telemetry Details")

if accepted:
    for item in accepted:
        data = item.get("notification", {})

        with st.expander(
            f"🔧 {data.get('device', 'Unknown')} — "
            f"{item.get('status', 'Accepted')}"
        ):
            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Temperature",
                f"{data.get('temperature_c', 'N/A')} °C"
            )

            c2.metric(
                "Current",
                f"{data.get('current_a', 'N/A')} A"
            )

            c3.metric(
                "Speed",
                f"{data.get('rpm', 'N/A')} RPM"
            )

            c4.metric(
                "Vibration",
                f"{data.get('vibration_mm_s', 'N/A')} mm/s"
            )

            st.write(
                "**Correction:**",
                item.get("correction", "None")
            )

st.divider()

st.subheader("📁 Pipeline Output Files")

st.write(
    f"Accepted output: `{ACCEPTED_FILE.name}` "
    f"({'Available' if ACCEPTED_FILE.exists() else 'Not found'})"
)

st.write(
    f"Rejected output: `{REJECTED_FILE.name}` "
    f"({'Available' if REJECTED_FILE.exists() else 'Not found'})"
)

st.caption(
    "Demonstration uses simulated industrial motor notifications. "
    "Results are loaded from the actual output files of industrial_validator.py. "
)

st.divider()

st.header("🧪 Custom Industrial Telemetry Tester")

st.write(
    "Enter a motor notification in JSON format. "
    "The actual YANG model will validate the notification."
)

custom_json = st.text_area(
    "Enter Custom Motor Telemetry",
    value='''{
    "device": "Motor-05",
    "temperature_c": 70.5,
    "current_a": 4.5,
    "rpm": 1450,
    "vibration_mm_s": 3.0
}''',
    height=180
)


def validate_custom_notification(data):
    validation_data = data.copy()

    decimal_fields = [
        "temperature_c",
        "current_a",
        "vibration_mm_s"
    ]

    for field in decimal_fields:
        validation_data[field] = str(validation_data[field])

    custom_model = DataModel.from_file(
        str(BASE_DIR / "yang-library.json"),
        [str(BASE_DIR)]
    )

    root = custom_model.from_raw({
        "telemetry-demo:telemetry": validation_data
    })

    root.validate()


if st.button("🚀 Test Custom Notification"):
    try:
        custom_data = json.loads(custom_json)

        if not isinstance(custom_data, dict):
            st.error("Rejected: Enter a JSON object.")
        else:
            try:
                validate_custom_notification(custom_data)

                st.success(
                    "✅ ACCEPTED: Notification passed YANG validation."
                )

            except Exception as validation_error:

                corrected = custom_data.copy()
                changes = []

                rpm = corrected.get("rpm")

                if isinstance(rpm, str):
                    import re

                    match = re.fullmatch(r"([0-9]+)rpm", rpm)

                    if match:
                        corrected["rpm"] = int(match.group(1))
                        changes.append(
                            "Converted RPM text to integer"
                        )

                if changes:
                    try:
                        validate_custom_notification(corrected)

                        st.success(
                            "✅ ACCEPTED AFTER SAFE CORRECTION"
                        )
                        st.write("Correction:", changes)
                        st.json(corrected)

                    except Exception as second_error:
                        st.error(
                            "❌ REJECTED: Revalidation failed."
                        )
                        st.code(str(second_error))

                else:
                    st.error("❌ REJECTED: YANG validation failed.")
                    st.code(str(validation_error))

    except json.JSONDecodeError:
        st.error("Invalid JSON format.")
