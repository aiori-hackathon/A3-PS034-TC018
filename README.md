# AIORI-3 Hackathon | Beyond Limits

**Project Title:** Schema-Validated YANG-Push Telemetry Pipeline  
**Problem Statement:** PS-034 – Cloud Computing & IoT  
**Team Name:** Beyond Limits  
**Team Code:** A3-PS034-TC018

---

## 1. Project Overview

Modern networks generate continuous streams of telemetry data to help monitor device behaviour, identify changes, and support timely operational decisions. However, receiving telemetry quickly is only one part of the challenge. Notifications that violate the expected data schema, contain malformed data, or fail to reach the monitoring application reliably can reduce the quality and trustworthiness of downstream monitoring.

**Our project focuses on making industrial IoT telemetry processing more reliable through schema-based data validation and error handling.**

We propose a telemetry pipeline that receives industrial telemetry notifications, validates them against a designated YANG model, and separates valid notifications from invalid ones.

The system also applies predefined safe correction rules to recoverable formatting errors, revalidates corrected notifications, and records notifications that cannot be safely corrected.

The current working prototype demonstrates these capabilities using simulated industrial motor telemetry and a monitoring dashboard.

## 2. Problem Statement

Traditional network monitoring often uses periodic polling, which can miss short-lived changes occurring between polling intervals. YANG-Push supports subscription-based delivery of telemetry updates according to configured conditions, enabling a streaming approach to monitoring.

However, a telemetry pipeline must do more than receive updates. It must verify that notifications conform to the expected YANG data model and handle invalid data appropriately.

This project addresses the challenge of building a pipeline that:

- Validates incoming notifications against a designated YANG model.
- Identifies malformed and schema-invalid notifications.
- Corrects predefined recoverable formatting errors safely.
- Revalidates corrected notifications before acceptance.
- Records invalid notifications for further inspection.
- Provides visibility into telemetry validation results.

## 3. Proposed Solution

We propose a **schema-validation and telemetry-processing pipeline** that places a validation stage before downstream monitoring.

Instead of accepting every incoming notification directly, the system checks each notification against the predefined YANG model.

The processing approach follows these stages:

1. **Telemetry Generation:** Generate industrial motor telemetry notifications.
2. **Schema Validation:** Validate incoming notifications against the YANG model.
3. **Error Detection:** Identify incorrect data types and malformed values.
4. **Safe Error Correction:** Apply predefined correction rules to recoverable errors.
5. **Revalidation:** Validate corrected notifications again.
6. **Acceptance:** Store notifications that pass validation.
7. **Rejection and Quarantine:** Reject invalid notifications and record error information.
8. **Dashboard Monitoring:** Display validation results and motor telemetry details.

## 4. Proposed Architecture

The proposed architecture consists of a telemetry source, a YANG schema validator, an error-handling stage, output storage, and a dashboard consumer.

### Architecture Flow

**Valid Notification Path:**

Telemetry Source → YANG Schema Validator → Accepted Notifications → Dashboard

**Recoverable Error Path:**

Telemetry Source → YANG Schema Validator → Safe Correction → Revalidation → Accepted Notifications

**Invalid Notification Path:**

Telemetry Source → YANG Schema Validator → Rejection / Quarantine → Error Log

### Component Description

- **1. Telemetry Source:** Generates industrial motor telemetry notifications.
- **2. YANG Schema Validator:** Checks incoming notifications against the defined YANG model.
- **3. Error Detection Module:** Identifies invalid data and validation errors.
- **4. Safe Correction Module:** Applies predefined correction rules to recoverable formatting errors.
- **5. Revalidation Module:** Checks corrected notifications against the YANG model again.
- **6. Output Storage:** Maintains separate accepted and rejected notification records.
- **7. Dashboard:** Displays validation outcomes and motor telemetry information.

## 5. Key Objectives

- Implement YANG-model-based telemetry validation.
- Identify invalid notifications before acceptance.
- Correct predefined recoverable formatting errors safely.
- Revalidate corrected notifications.
- Maintain separate accepted and rejected notification records.
- Provide a dashboard for monitoring telemetry and validation results.
- Package the working prototype using Docker.
- Establish a foundation for future message-broker integration and reliability testing.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and validation logic |
| Yangson | YANG schema validation |
| YANG | Telemetry data modelling |
| JSON / JSONL | Telemetry data and output storage |
| Streamlit | Interactive monitoring dashboard |
| Docker | Application containerisation |
| Visual Studio Code | Development environment |

## 7. Testing and Evaluation

The working prototype demonstrates the following test cases.

### Test 1: Valid Notifications

Verify that notifications conforming to the YANG model pass validation and are accepted.

### Test 2: Recoverable Formatting Error

A notification containing an RPM value such as `1450rpm` is processed using a predefined safe correction rule.

The value is converted into the integer `1450` and validated again before acceptance.

### Test 3: Invalid Data Type

A notification containing a temperature value such as `hello` does not satisfy the expected decimal data type and is rejected.

### Test 4: Dashboard Monitoring

Verify that accepted notifications, rejected notifications, validation results, and motor telemetry details are displayed on the dashboard.

### Test 5: Custom Telemetry Validation

Submit custom JSON telemetry through the dashboard and observe whether the YANG validation process accepts or rejects it.

## 8. Project Value and Expected Impact

The value of this project is not simply in collecting telemetry, but in combining schema validation, safe error handling, and monitoring in one prototype.

The system aims to:

- Improve telemetry data quality.
- Identify invalid data before acceptance.
- Reduce avoidable rejection through predefined safe corrections.
- Maintain records of accepted and rejected notifications.
- Improve visibility into validation outcomes.
- Provide a foundation for reliable industrial telemetry processing.

## 9. Project Deliverables

The current working prototype includes:

- Python-based industrial telemetry validator.
- YANG telemetry data model.
- YANG library configuration.
- Safe correction of predefined recoverable formatting errors.
- Revalidation of corrected notifications.
- Accepted and rejected telemetry output files.
- Streamlit monitoring dashboard.
- Custom industrial telemetry tester.
- Dockerfile and Python dependency configuration.
- Technical documentation and execution instructions.

**Repository Source Code:** [View Technical Implementation](src/AIORI%20VS/)

## 10. Team Information

- **Team Name:** Beyond Limits
- **Team Code:** A3-PS034-TC018
- **Problem Statement:** PS-034 – Cloud Computing & IoT
- **Category:** Cloud Computing & IoT

## 11. Development Status

**Current Status: Working Software Prototype**

The project has progressed from initial planning to a working software-based demonstration.

The following functionalities have been implemented:

- YANG schema loading and validation using Yangson.
- Industrial motor telemetry processing.
- Detection of invalid telemetry values.
- Predefined safe correction of recoverable formatting errors.
- Revalidation after correction.
- Accepted and rejected notification storage.
- Streamlit-based monitoring dashboard.
- Custom JSON telemetry validation through the dashboard.
- Docker-based application execution.

### Current Demonstration Results

The current demonstration processes four simulated industrial motor notifications:

| Metric | Result |
|---|---:|
| Total Notifications | 4 |
| Accepted Notifications | 3 |
| Rejected Notifications | 1 |
| Accepted Rate | 75% |
| Rejected Rate | 25% |

These results represent the current demonstration dataset and are not live industrial measurements.

### Future Development

The following enhancements remain future work:

- Integration with a YANG-Push publisher or faithful emulator.
- External message-broker integration.
- End-to-end telemetry delivery testing.
- Message-loss and duplicate-message evaluation.
- Delivery-delay measurement.
- Consumer restart and recovery testing.
- Live industrial hardware integration.

## 12. References

The project is based on YANG data modelling and YANG-Push concepts, together with the documentation of the Yangson validation library, Python, Streamlit, and Docker.

Relevant technical standards and software documentation will support further development and integration.

## 13. Team Introduction Video

**Team Name:** Beyond Limits  
**Team Code:** A3-PS034-TC018

**YouTube Video:** [Watch our team introduction](https://youtu.be/IiElbn7cXWA?si=jpVBof4f5WBgJ10H)

---
## 14. Working Demo

Live Application:
(https://youtu.be/-miq7E9YlIo?si=N98IhQFMdXUT6TtT)

**AIORI-3 Hackathon | Beyond Limits | PS-034**
