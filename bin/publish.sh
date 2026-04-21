#!/bin/bash

# One-Click Publish Script for Academic Website
# This script stages all changes, commits them, and pushes to the remote repository.

echo "🚀 Starting publication process..."

# 1. Stage all changes
git add .

# 2. Commit changes
# Use the first argument as the commit message if provided, otherwise use a default
COMMIT_MSG=${1:-"site update and organization cleanup"}
git commit -m "$COMMIT_MSG"

# 3. Push to remote
echo "📤 Pushing to GitHub..."
git push

echo "✅ Done! Your site is being built and deployed by GitHub Actions."
echo "Check the progress at: https://github.com/Jidi1997/Jidi1997.github.io/actions"
