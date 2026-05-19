# Day 3 - Controlled Dependency / SCA Demo

## Purpose

This file documents the controlled vulnerable dependency sample created for SCA practice.

## Important Safety Note

The file `dependency-demo/requirements.txt` contains intentionally old package versions for training only. These packages should not be installed or used in the working Flask app.

## Files Added

- `dependency-demo/requirements.txt`
- Updated `.github/dependabot.yml`

## Controlled Demo Dependencies

| Package | Version | Purpose |
|---|---|---|
| requests | 2.19.1 | Old dependency for SCA/update practice |
| jinja2 | 2.10 | Old dependency for SCA/update practice |
| flask | 0.12.2 | Old dependency for SCA/update practice |

## Expected Product Security Workflow

1. Add controlled vulnerable dependency sample.
2. Push to GitHub.
3. Allow Dependabot / dependency graph to detect outdated or vulnerable dependencies.
4. Review alerts or update PRs.
5. Record evidence in Evidence Log.
6. Move validated findings into Vulnerability Register.
7. Track remediation through package update.
8. Verify closure through clean scan or merged update PR.

## Current Status

Dependabot configuration updated. Scanner evidence is still pending until GitHub processes the new dependency manifest.

## Learning Point

SCA findings should be validated before being treated as official vulnerabilities. The security review should consider package usage, version, CVE details, exploitability, exposure, severity, owner, SLA, and remediation evidence.