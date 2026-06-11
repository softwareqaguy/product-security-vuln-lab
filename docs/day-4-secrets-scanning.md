# Day 4 - Secrets Scanning Practice

## Purpose

This day focuses on secrets scanning and reviewing hardcoded credential findings as part of a vulnerability management workflow.

## Tool Used

Gitleaks GitHub Action

## Scenario

The training app originally contained an intentionally fake API key in:

`app/app.py`

The initial goal was to validate whether Gitleaks would detect the fake key as a possible hardcoded secret.

## Initial Scan Result

The Gitleaks workflow ran successfully but returned:

`No leaks detected`

This means the original fake key pattern in `app/app.py` was not detected by the default Gitleaks rules.

## Controlled Detection Follow-Up

To validate scanner detection, a controlled fake secret file was added:

`secrets-demo/fake-secrets.env`

A custom Gitleaks configuration file was also added:

`gitleaks.toml`

The custom rule was created for a training-only fake secret pattern:

`training-fake-secret`

The GitHub Actions workflow was updated to explicitly use the custom Gitleaks configuration.

## Controlled Detection Result

After the workflow was explicitly configured to use `gitleaks.toml`, Gitleaks detected the controlled fake secret pattern and the workflow failed as expected.

This failed workflow is considered successful evidence for the lab because it confirms the scanner detected the controlled fake secret.

## Triage Decision

This is a training-only finding. No real credentials are used.

Adjusted severity:

`Training Only / Informational`

In a real environment, an exposed active secret would require:

- Immediate credential rotation or revocation
- Removal from code
- Review of commit history exposure
- Investigation for unauthorized use
- Clean re-scan evidence before closure

## Evidence

- `EVID-008` - Initial Gitleaks scan ran successfully but found no leaks
- `EVID-009` - Controlled fake secret detected using custom Gitleaks training rule

## Vulnerability Register Update

This maps to:

`VULN-002 - Fake hardcoded API key / controlled secret detection`

The finding should be marked as triaged because the scanner result was reviewed and the severity was adjusted based on training-only context.

## Verification Plan

Future verification can be completed by removing the controlled fake secret or excluding the approved training pattern, then re-running Gitleaks to confirm the workflow returns no leaks detected.