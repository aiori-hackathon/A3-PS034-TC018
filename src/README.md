# Schema-Validated YANG-Push Telemetry Pipeline

## AIORI-3 Hackathon – Beyond Limits

**Problem Statement:** PS-034 – Cloud Computing & IoT  
**Team Code:** A3-PS034-TC018  
**Project Type:** Software-Based Industrial IoT Telemetry Prototype

## 1. Project Overview

The Schema-Validated YANG-Push Telemetry Pipeline is designed to improve the reliability of industrial IoT telemetry through schema-based data validation.

The system checks incoming industrial motor notifications against a predefined YANG data model before accepting them for monitoring.

It identifies invalid data, applies predefined safe correction rules to recoverable errors, revalidates corrected notifications, and rejects data that cannot be safely corrected.

The current working demonstration uses simulated industrial motor telemetry.

## 2. Key Features

- **YANG Schema Validation:** Checks incoming telemetry against the defined data structure and data types.
- **Safe Error Correction:** Applies predefined correction rules to recoverable formatting errors.
- **Revalidation:** Validates corrected notifications again before acceptance.
- **Invalid Data Rejection:** Rejects notifications that do not satisfy the schema.
- **Quarantine and Error Logging:** Records rejected notifications for further inspection.
- **Telemetry Monitoring Dashboard:** Displays validation results and individual motor parameters.
- **Custom Telemetry Tester:** Allows users to submit JSON notifications for validation.
- **Docker Containerisation:** Runs the dashboard in a containerised environment.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Validation logic |
| Yangson | YANG-based data validation |
| YANG | Telemetry data modelling |
| Streamlit | Monitoring dashboard |
| Docker | Application containerisation |
| JSON | Telemetry data format |

## 4. System Workflow

1. Receive an industrial motor telemetry notification.
2. Check its structure and data types against the YANG schema.
3. Identify validation errors.
4. Apply a predefined safe correction if the error is recoverable.
5. Revalidate the corrected notification.
6. Accept valid notifications.
7. Reject and record invalid notifications.
8. Display validation results through the dashboard.

## 5. Project File Structure

```text
AIORI VS/
│
├── Dashboard.py
├── industrial_validator.py
├── telemetry-demo.yang
├── yang-library.json
├── requirements.txt
├── Dockerfile
├── industrial_accepted.jsonl
├── industrial_rejected.jsonl
└── README.md
```

## 6. Installation Requirements

- Python 3
- Docker Desktop
- Visual Studio Code (recommended)

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## 7. Running the Validation Program

Open a terminal in the project directory and execute:

```bash
python industrial_validator.py
```

The program processes the configured telemetry samples and generates accepted and rejected output records.

## 8. Running the Dashboard

To start the dashboard directly using Streamlit:

```bash
streamlit run Dashboard.py
```

Open the following address in your browser:

```text
http://localhost:8501
```

## 9. Running with Docker

Build the Docker image:

```bash
docker build -t aiori-telemetry .
```

Run the container:

```bash
docker run -d -p 8501:8501 --name aiori-dashboard aiori-telemetry
```

Open the dashboard:

```text
http://localhost:8501
```

To check the running container:

```bash
docker ps
```

## 10. Demonstration and Test Cases

The prototype demonstrates the following test cases:

**Test Case 1 – Valid Notification**

A correctly formatted industrial motor notification is validated and accepted.

**Test Case 2 – Recoverable Formatting Error**

An RPM value received as `1450rpm` is converted into the integer `1450` using a predefined safe correction rule. The corrected notification is revalidated and accepted.

**Test Case 3 – Invalid Data Type**

A temperature value received as `hello` does not satisfy the expected decimal data type and is rejected.

## 11. Demonstration Results

In the current demonstration, four simulated notifications are processed:

- Total notifications: 4
- Accepted notifications: 3
- Rejected notifications: 1
- Accepted rate: 75%
- Rejected rate: 25%

These are results from the current demonstration dataset, not live industrial measurements.

## 12. Output Files

- `industrial_accepted.jsonl` – Stores accepted telemetry notifications.
- `industrial_rejected.jsonl` – Stores rejected telemetry notifications and associated error information.

## 13. Current Prototype Scope

The current implementation demonstrates software-based telemetry validation using simulated industrial motor notifications.

The dashboard, Python validator, YANG model, error-handling logic and Docker-based execution form the working prototype.

Live hardware telemetry and external message-broker integration are not demonstrated in this version.

## 14. Expected Benefits

- Improves telemetry data quality.
- Identifies invalid notifications before acceptance.
- Supports safe correction of predefined recoverable errors.
- Maintains separate records of accepted and rejected data.
- Provides a visual interface for monitoring validation results.
- Supports containerised application execution.

---

**Team Beyond Limits | AIORI-3 Hackathon | PS-034**
