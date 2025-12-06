#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../"
for s in api_gateway market_data_service market_analyzer_service price_service signal_service notification_service; do
  docker build -t local/$s:ci -f services/$s/Dockerfile .
done
