# AI Event Normalization Framework

Purpose

Normalize custom application events into enterprise security events.

## Authentication

AI_AUTH_SUCCESS

AI_AUTH_FAILURE

AI_ACCOUNT_LOCKED

AI_PASSWORD_RESET

AI_MFA_FAILURE

## Process

AI_PROCESS_CREATE

AI_PROCESS_TERMINATE

AI_SCRIPT_EXECUTION

## File

AI_FILE_CREATE

AI_FILE_DELETE

AI_FILE_MODIFIED

## Network

AI_NETWORK_CONNECTION

AI_REMOTE_LOGIN

AI_DATA_EXFILTRATION

## Privilege

AI_PRIVILEGE_ESCALATION

AI_ROLE_CHANGE

AI_ADMIN_ACTIVITY

## Detection Engineering

All detections should reference AI events.

Platform-specific mappings occur during KQL generation.