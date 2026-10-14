# AIORI-3 Hackathon | Beyond Limits

**Project Title:** Schema-Validated YANG-Push Telemetry Pipeline  
**Problem Statement:** PS-034 – Cloud Computing & IoT  
**Team Name:** Beyond Limits  
**Team Code:** A3-PS034-TC018

---

## 1. Project Overview

Modern networks generate continuous streams of telemetry data to help monitor device behaviour, identify changes, and support timely operational decisions. However, receiving telemetry quickly is only one part of the challenge. Notifications that violate the expected data schema, contain malformed data, or fail to reach the monitoring application reliably can reduce the quality and trustworthiness of downstream monitoring.

**Our project focuses on making YANG-Push telemetry processing more reliable, validated, and measurable.**

We propose a containerised telemetry pipeline that receives notifications from the supplied YANG-Push publisher or a faithful emulator, validates them against the designated YANG model, and forwards accepted notifications through a message broker to a dashboard consumer. Malformed and schema-invalid notifications are rejected and recorded for analysis.

Beyond validation, the project evaluates how the pipeline behaves during operation and recovery. We measure message loss, duplicate messages, end-to-end delivery delay, and the impact of consumer restarts. These measurements will help us understand both the effectiveness of schema validation and the reliability of the overall data-delivery path.

Our goal is to demonstrate a practical, standards-based approach to processing streaming telemetry in which **data validity is checked before forwarding, and delivery behaviour is evaluated using measurable evidence.**

## 2. Problem Statement

Traditional network monitoring often uses periodic polling, which can miss short-lived changes occurring between polling intervals. YANG-Push supports subscription-based delivery of telemetry updates according to configured conditions, enabling a streaming approach to monitoring.

However, a telemetry pipeline must do more than receive updates. It must verify that notifications conform to the expected YANG data model and handle delivery in a way that can be tested and evaluated.

This project addresses the challenge of building an integrated pipeline that:

- Validates incoming notifications against the designated YANG model.
- Rejects malformed and schema-invalid notifications.
- Forwards valid notifications through a message broker without altering their structure.
- Provides visibility into accepted telemetry and pipeline behaviour.
- Evaluates message loss, duplicate delivery, end-to-end delay, and consumer-restart behaviour.

## 3. Proposed Solution

We propose a **schema-validation and telemetry-delivery pipeline** that places a validation stage between the telemetry publisher and the downstream monitoring application.

Instead of forwarding every incoming notification directly to the consumer, the pipeline checks each notification against the supplied YANG model first. Only notifications that pass validation proceed to the message broker. Invalid notifications are rejected and recorded for testing and analysis.

The pipeline will be developed and evaluated through the following stages:

1. **Telemetry generation:** Use the supplied publisher or a faithful emulator to generate YANG-Push notifications.
2. **Schema validation:** Validate incoming notifications against the designated YANG model.
3. **Invalid-data handling:** Reject malformed and schema-invalid notifications and record relevant validation results.
4. **Message-broker integration:** Forward valid notifications while preserving their structure.
5. **Dashboard monitoring:** Receive and display accepted telemetry and relevant pipeline status.
6. **Reliability evaluation:** Measure message loss, duplicate messages, and end-to-end delivery delay.
7. **Recovery testing:** Restart the consumer under controlled conditions and observe the effect on message delivery.

## 4. Proposed Architecture

The proposed architecture consists of a telemetry publisher, a YANG schema validator, a message broker, a dashboard consumer, and an evaluation module. Incoming notifications are validated before forwarding to ensure that only schema-valid notifications proceed to the monitoring application.

### Architecture Flow

**Valid Notification Path:**

Telemetry Publisher / Emulator → YANG Schema Validator → Message Broker → Dashboard Consumer

**Invalid Notification Path:**

YANG Schema Validator → Reject Notification → Record Validation Result

### Component Description

- **1. Telemetry Publisher / Emulator:** Generates YANG-Push notifications using the supplied publisher or a faithful emulator.
- **2. YANG Schema Validator:** Validates incoming notifications against the supplied YANG model to check their structure and schema compliance.
- **3. Invalid-Notification Handler:** Rejects malformed or schema-invalid notifications and records validation results for analysis.
- **4. Message Broker:** Transfers accepted notifications to the dashboard consumer while preserving their structure.
- **5. Dashboard Consumer:** Receives and displays accepted telemetry for monitoring.
- **6. Evaluation Module:** Measures message loss, duplicate messages, end-to-end delivery delay, and pipeline behaviour during consumer restarts.

### Expected Functionality

The architecture separates validation from message delivery. Valid notifications proceed through the message broker, while invalid notifications are rejected and recorded. The completed pipeline will be tested to evaluate its data-validation behaviour and delivery reliability under normal operation and consumer-restart conditions.

## 5. Key Objectives

- Integrate the supplied YANG-Push publisher or a faithful emulator.
- Implement validation using the supplied YANG model.
- Prevent schema-invalid notifications from being forwarded as valid telemetry.
- Preserve notification structure during message-broker forwarding.
- Provide a dashboard for observing accepted telemetry.
- Measure message loss, duplicate messages, and end-to-end delivery delay.
- Evaluate pipeline behaviour when the consumer restarts.
- Package the prototype using containerisation for reproducible deployment and demonstration.

## 6. Technology Stack

The implementation will use the resources and technologies that best match the supplied hackathon environment.

- **Telemetry source:** Supplied YANG-Push publisher or faithful emulator.
- **Data modelling:** Supplied YANG model.
- **Validation:** A compatible YANG schema-validation library.
- **Message transport:** A suitable message broker.
- **Monitoring:** A dashboard consumer.
- **Deployment:** Containerisation tools.
- **Evaluation:** Test scripts and measurements for validation and delivery reliability.

Specific libraries, broker software, and dashboard frameworks will be documented after they are selected and integrated.

## 7. Testing and Evaluation

The project will be evaluated through controlled test cases rather than assumptions about reliability.

### Test 1: Valid Notifications
Verify that notifications conforming to the supplied YANG model pass validation.

### Test 2: Invalid Notifications
Verify that malformed or schema-invalid notifications are rejected.

### Test 3: Structure Preservation
Verify that accepted notification structures remain intact during forwarding.

### Test 4: Message Loss
Compare the number of notifications sent with the number received.

### Test 5: Duplicate Delivery
Identify notifications received more than once using appropriate test identifiers.

### Test 6: Delivery Delay
Measure the elapsed time between sending and receiving notifications.

### Test 7: Consumer Restart
Observe message-delivery behaviour when the consumer stops and restarts.

The resulting measurements will be used to document the strengths and limitations of the implemented pipeline.

## 8. Project Value and Expected Impact

The value of this project is not simply in collecting telemetry, but in **combining schema validation, controlled message forwarding, and measurable reliability testing in one pipeline.**

The proposed system aims to:

- Improve visibility into invalid telemetry before it reaches downstream monitoring.
- Make notification validation outcomes easier to inspect.
- Help identify message-delivery issues through measurable tests.
- Provide a repeatable environment for evaluating pipeline behaviour.
- Support more informed decisions about the reliability of streaming telemetry systems.

The prototype will demonstrate these benefits through implementation results and test evidence, rather than assuming that validation alone guarantees reliable delivery.

## 9. Expected Deliverables

- A containerised YANG-Push telemetry pipeline.
- Integration with the supplied publisher or a faithful emulator.
- YANG-model-based notification validation.
- Invalid-notification rejection and logging.
- Message-broker integration and a dashboard consumer.
- Test cases and measurements for pipeline reliability.
- Technical documentation and a working demonstration.

## 10. Team Information

- **Team Name:** Beyond Limits
- **Team Code:** A3-PS034-TC018
- **Problem Statement:** PS-034 – Schema-Validated YANG-Push Telemetry Pipeline
- **Category:** Cloud Computing & IoT

## 11. Development Status

**Current Status:** Initial setup and project planning.

The next stages are to inspect the supplied resources, implement the validation and message-delivery pipeline, integrate the dashboard, and perform the required reliability tests. Actual implementation details and measured results will be added as development progresses.

## 12. References

The final documentation will include the relevant YANG and YANG-Push standards, documentation for the selected validation library and message broker, and any additional technical references used during implementation.
## 13. Team Introduction Video

**Team Name:** Beyond Limits  
**Team Code:** A3-PS034-TC018

**YouTube Video:** [Watch our team introduction]((https://youtu.be/IiElbn7cXWA?si=jpVBof4f5WBgJ10H))
