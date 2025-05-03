#!/usr/bin/env bash
set -e

# load .env if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

streamlit run app/main.py --server.port ${PORT:-8501}

chmod +x run.sh
