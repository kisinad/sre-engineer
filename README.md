# SRE Engineer Assistant

SRE Engineer Assistant is a plugin for Site Reliability Engineering workflows.

It is designed to help with:
- Alert triage and severity routing
- Root cause analysis with evidence correlation
- Incident mitigation and stakeholder communications
- Reliability follow-up through SLO, error-budget, and postmortem work

## Plugin Manifest

The plugin manifest is defined in `.github/plugin.json`.

## Agents

- `sre-engineer`: End-to-end orchestration
- `alert-triage`: Signal filtering, deduplication, and escalation advice
- `rca-investigator`: Timeline and root cause investigation
- `incident-commander`: Mitigation and communication coordination
- `reliability-advisor`: SLO and reliability improvement guidance

## Skills

- `monitoring`
- `alerting`
- `incident-management`
- `slo-error-budget`
- `observability-correlation`
- `runbooks`
- `postmortems`
- `capacity-planning`
- `change-risk`
- `incident-comms`
- `dependency-mapping`

## Repository Structure

```text
.github/
	plugin.json
	agents/
		*.agent.md
	skills/
		*/SKILL.md
```

## Validation

Run this before publishing plugin changes:

```bash
python3 .github/scripts/validate-plugin-paths.py
```

## CI

GitHub Actions runs this same validation automatically on pull requests and pushes to `main` when plugin-related files change.

Workflow file:
- `.github/workflows/validate-plugin.yml`