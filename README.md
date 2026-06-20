# SRE Engineer Assistant

SRE Engineer Assistant is a plugin for Site Reliability Engineering workflows.

It is designed to help with:
- Alert triage and severity routing
- Root cause analysis with evidence correlation
- Incident mitigation and stakeholder communications
- Reliability follow-up through SLO, error-budget, and postmortem work

## Plugin Manifest

The plugin manifest is defined in `.github/plugin.json`.

### Marketplace Metadata

Marketplace listing metadata is defined in `.github/plugin/marketplace.json`. This file includes:
- Display name and icon
- Publisher and author information
- Repository and homepage URLs
- Capabilities summary (agents and skills)
- Feature descriptions
- Keywords and categories for discovery
- Pricing and support links

## Installation

### Prerequisites
- Visual Studio Code
- GitHub Copilot extension
- Access to this repository

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/deniskisina/sre-engineer.git
   ```

2. **Load the plugin in VS Code**
   - Open VS Code
   - Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Linux/Windows)
   - Search for `GitHub Copilot: Load Plugin`
   - Select the cloned `sre-engineer` directory (specifically the `.github` folder containing `plugin.json`)

3. **Verify installation**
   - Run the validation script:
     ```bash
     python3 .github/scripts/validate-plugin-paths.py
     ```
   - Output should show: `Plugin validation passed: 5 agents, 11 skills`

## Usage

### Using Agents

Invoke agents in Copilot Chat with trigger phrases:
- **sre-engineer**: General SRE workflows — "Orchestrate response to this incident"
- **alert-triage**: Alert filtering — "Triage these alerts by severity"
- **rca-investigator**: Root cause analysis — "Investigate the root cause from this timeline"
- **incident-commander**: Mitigation steps — "Create a mitigation plan"
- **reliability-advisor**: Reliability decisions — "Assess our SLO status"

### Using Skills

Skills trigger automatically based on prompt keywords. Examples:

- **monitoring**: "CPU is at 95% on checkout-api. What should I check?"
- **alerting**: "We had 120 pages overnight with no impact. How do we reduce noise?"
- **incident-management**: "Generate a recovery checklist for restoring API availability."
- **slo-error-budget**: "Our SLO burned 40% in 2 days. What now?"
- **observability-correlation**: "Correlate logs, metrics, and traces for this incident."
- **runbooks**: "Execute this recovery runbook safely."
- **postmortems**: "Draft a blameless postmortem from this incident."
- **capacity-planning**: "Forecast traffic for 90 days and identify bottlenecks."
- **change-risk**: "Assess risk for this auth-service deployment."
- **incident-comms**: "Write a customer-facing status page update."
- **dependency-mapping**: "Map blast radius for this cache-cluster degradation."

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
	plugin/
		marketplace.json
	agents/
		*.agent.md
	skills/
		*/SKILL.md
	scripts/
		validate-plugin-paths.py
	workflows/
		validate-plugin.yml
```

## Validation

Run this before publishing plugin changes:

```bash
python3 .github/scripts/validate-plugin-paths.py
```

This checks:
- All agent files referenced in `plugin.json` exist
- All skill directories and their `SKILL.md` files exist
- `marketplace.json` is valid JSON

## CI

GitHub Actions runs this same validation automatically on pull requests and pushes to `main` when plugin-related files change.

Workflow file:
- `.github/workflows/validate-plugin.yml`