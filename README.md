# SRE Engineer Assistant

SRE Engineer Assistant is a plugin for Site Reliability Engineering workflows.

It is designed to help with:
- Alert triage and severity routing
- Root cause analysis with evidence correlation
- Incident mitigation and stakeholder communications
- Reliability follow-up through SLO, error-budget, and postmortem work

## Plugin Manifest

The canonical plugin manifest is defined in `.github/plugin.json`.

Installer-compatible manifests are also available at:
- `plugin.json` (repository root)
- `.github/plugin/plugin.json`

These compatibility paths allow `copilot plugin install https://github.com/<owner>/<repo>` to discover the plugin manifest automatically.

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

2. **Install using Copilot CLI (recommended)**
   ```bash
   copilot plugin install https://github.com/deniskisina/sre-engineer
   ```

3. **Load the plugin manually in VS Code (alternative)**
   - Open VS Code
   - Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Linux/Windows)
   - Search for `GitHub Copilot: Load Plugin`
   - Select the cloned `sre-engineer` directory (specifically the `.github` folder containing `plugin.json`)

4. **Verify installation**
   - Run the validation script:
     ```bash
     python3 .github/scripts/validate-plugin-paths.py
     ```
   - Output should show: `Plugin validation passed: 1 public agent(s), 4 internal agent(s), 11 skills, marketplace metadata OK`

## Usage

### Invoke the SRE Engineer

You interact with the plugin through a single agent: **sre-engineer**. Describe your incident, reliability question, or task, and the agent will automatically route to the right internal specialists.

#### Example Prompts

- "I have an alert storm on the checkout service. Help me triage and respond."
- "My API latency spiked 30 seconds ago. Let's investigate the root cause."
- "We burned 60% of our SLO budget in 3 days. What should we do?"
- "Help me mitigate this database connection pool exhaustion."
- "Generate a postmortem from this incident timeline."

#### Capabilities (Automatically Delegated)

The agent internally coordinates:
- **Alert Triage**: "CPU is at 95% on checkout-api. What should I check?"
- **RCA**: "Correlate logs, metrics, and traces for this incident."
- **Mitigation**: "Create a mitigation plan and recovery checklist."
- **Reliability**: "Assess our SLO status and recommend priorities."

### Available Skills

Skills are automatically triggered by relevant keywords in your prompts:

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

### Public Agent (User Interface)

- `sre-engineer`: Main orchestrator that guides you through SRE workflows and internally delegates to specialists.

### Internal Agents (Orchestrated by sre-engineer)

- `alert-triage`: Classifies alerts and routes escalations
- `rca-investigator`: Performs root cause analysis with evidence correlation
- `incident-commander`: Coordinates mitigation and recovery
- `reliability-advisor`: Guides SLO and reliability decisions

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