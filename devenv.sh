#!/bin/zsh
pid=$(wezterm cli spawn --cwd . -- zsh -c "source .venv/bin/activate && python manage.py runserver")
ppid=$(wezterm cli split-pane --pane-id $pid --cwd ./distrito_libre_frontend/ -- zsh -c "npm install && npm run dev -- --open")
source .venv/bin/activate
nvim .
