# Custom Log Mapping

Purpose

Map proprietary application logs to AI Event Framework.

Example

Windows

4624

↓

AI_AUTH_SUCCESS

Windows

4625

↓

AI_AUTH_FAILURE

Windows

4740

↓

AI_ACCOUNT_LOCKED

Application A

EventCode=1

↓

AI_AUTH_SUCCESS

Application A

EventCode=23

↓

AI_AUTH_FAILURE

Application A

EventCode=51

↓

AI_ACCOUNT_LOCKED

Application B

Status=SUCCESS

↓

AI_AUTH_SUCCESS

Application B

Status=FAILED

↓

AI_AUTH_FAILURE

Application B

Status=LOCKED

↓

AI_ACCOUNT_LOCKED

## Rule

Detection logic must use AI Event Framework.

Translation to vendor-specific fields occurs during KQL generation.