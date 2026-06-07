#!/bin/bash

# Ensure we exit on any failure
set -e

source .venv/bin/activate
source .env

# Format: ResultDir:GroundTruthFile
APPS=(
  "Mifos:Mifos.md"
  "MoodleStudent:MoodleStudent.md"
  "MoodleTeacher:MoodleTeacher.md"
  "PHPTravels:Phptravels.md"
  "Parabank:Parabank.md"
  "SwagLab:Swaglab.md"
)

MODELS=(
  "gpt-4o-mini"
  "gpt-5-mini"
)

for MODEL in "${MODELS[@]}"; do
  for APP_INFO in "${APPS[@]}"; do
    APP_DIR="${APP_INFO%%:*}"
    APP_MD="${APP_INFO##*:}"
    
    echo "=========================================================="
    echo "Running post-verify for $APP_DIR with model $MODEL"
    echo "=========================================================="
    
    test-case-generation --post-verify \
      --input "dataset/ground_truth/$APP_MD" \
      --test-cases "results/$APP_DIR/$MODEL/agent/test-cases.json" \
      --api-key "$OPENAI_API_KEY" \
      --model "openai/$MODEL" \
      --output "results/$APP_DIR/$MODEL/agent"
      
    echo "Finished $APP_DIR for $MODEL"
    echo ""
  done
done

echo "All post-verification runs complete!"
