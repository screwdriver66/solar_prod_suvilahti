#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
export PORT=$PORT
exec gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - run:application
# exec gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - run:application
