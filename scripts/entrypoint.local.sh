#!/bin/sh

# Trap SIGTERM
trap 'echo "TRAPPED SIGTERM! Going to kill $PID ..."; kill -15 $PID; wait $PID' TERM

echo "[Bootstrap] Starting server..."

/root/.local/bin/poetry run python manage.py run &
PID=$!
wait $PID