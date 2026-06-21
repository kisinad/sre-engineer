#!/usr/bin/env bash
set -euo pipefail

# Generic hook logger for agent invocations. It records raw payloads so schema changes do not break logging.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOG_DIR="$REPO_ROOT/.github/logs"
LOG_FILE="$LOG_DIR/agent-calls.log"

mkdir -p "$LOG_DIR"

timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
payload="${1:-}"

{
  printf '[%s] hook=onAgentCall\n' "$timestamp"
  if [[ -n "$payload" ]]; then
    printf 'payload=%s\n' "$payload"
  fi
  printf '\n'
} >> "$LOG_FILE"
