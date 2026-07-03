#!/usr/bin/env bash
# Status line command for Claude Code.
# Reads session JSON from stdin and outputs context usage on the left,
# model and effort on the right.

input=$(cat)

# Pull both the percentage and the raw token counts out of the statusline JSON.
used_pct=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
max_tokens=$(echo "$input" | jq -r '.context_window.context_window_size // empty')
used_tokens=$(echo "$input" | jq -r '
    if .context_window.current_usage == null then empty
    else
        (.context_window.current_usage.input_tokens // 0)
        + (.context_window.current_usage.cache_creation_input_tokens // 0)
        + (.context_window.current_usage.cache_read_input_tokens // 0)
    end
')

# No usage data at all means we are pre-first-message. Print nothing.
if [ -z "$used_pct" ]; then
    exit 0
fi

used_int=$(printf '%.0f' "$used_pct")

# Color thresholds: green <=60%, yellow >60% and <=80%, red >80%.
if [ "$used_int" -gt 80 ]; then
    color='\033[31m'
elif [ "$used_int" -gt 60 ]; then
    color='\033[33m'
else
    color='\033[32m'
fi

# Build the left side: context usage.
if [ -n "$used_tokens" ] && [ -n "$max_tokens" ]; then
    used_k=$(( (used_tokens + 500) / 1000 ))
    max_k=$(( (max_tokens + 500) / 1000 ))
    left=$(printf '%b[context: %dk/%dk tokens (%d%%)]\033[00m' \
        "$color" "$used_k" "$max_k" "$used_int")
else
    left=$(printf '%b[context: %d%%]\033[00m' "$color" "$used_int")
fi

# Right side: model display name (from stdin JSON) and effort level.
dim='\033[2m'
reset='\033[00m'
model=$(echo "$input" | jq -r '.model.display_name // empty')
effort="${CLAUDE_EFFORT_LEVEL:-}"
if [ -z "$effort" ]; then
    effort=$(jq -r '.effortLevel // "?"' ~/.claude/settings.json 2>/dev/null || echo "?")
fi
right=''
if [ -n "$model" ]; then
    right="$model"
fi
if [ -n "$effort" ]; then
    [ -n "$right" ] && right="$right / $effort" || right="$effort"
fi
if [ -n "$right" ]; then
    right_fmt=$(printf '%b%s%b' "$dim" "$right" "$reset")
    cols=$(tput cols 2>/dev/null || echo 80)
    # Claude Code's status bar has its own horizontal padding (borders,
    # scrollbar gutter). Subtract margin so right-aligned content doesn't
    # overflow past the visible pane and get truncated.
    #margin=6
    margin=3
    cols=$(( cols - margin ))
    # Strip ANSI escapes to measure visible width (perl is on every macOS).
    visible() { printf '%s' "$1" | perl -pe 's/\e\[[0-9;]*m//g'; }
    left_visible=$(visible "$left")
    right_visible=$(visible "$right_fmt")
    pad=$(( cols - ${#left_visible} - ${#right_visible} - 1 ))
    [ "$pad" -lt 1 ] && pad=1
    printf '%s%*s%s' "$left" "$pad" '' "$right_fmt"
else
    printf '%s' "$left"
fi
