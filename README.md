# Modular To-Do Cloud API

A FastAPI-based backend for a project-aware to-do application with cloud-ready persistence, notifications, emoji-customizable projects, calendar projections, and weekly progress maps.

## Features
- **Cloud-friendly storage** via a pluggable `CloudStorage` interface (default JSON-backed implementation simulates a cloud provider and can be swapped for real services).
- **Project grouping** with per-project emoji customization and descriptions.
- **Task management** with tagging, completion toggles, and due dates.
- **Notifications** service ready for integration with providers; currently records scheduled reminders.
- **Calendar view** endpoint projecting to-dos into calendar-friendly events.
- **Weekly progress map** summarizing completion by project and ISO week.
- **Modular routers** so features can be added or removed by composing FastAPI routers.

## Getting started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API locally:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
3. Open the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs) to try endpoints.

### Example workflow
1. Create a project:
   ```bash
   curl -X POST "http://localhost:8000/projects/?name=Personal&emoji=✨"
   ```
2. Add a task tied to the project (replace `<PROJECT_ID>`):
   ```bash
   curl -X POST "http://localhost:8000/tasks/?project_id=<PROJECT_ID>&title=Write%20spec&due_date=2024-12-31T09:00:00"
   ```
3. Schedule a notification:
   ```bash
   curl -X POST "http://localhost:8000/notifications/?item_id=<ITEM_ID>&scheduled_for=2024-12-30T09:00:00&message=Finish%20spec"
   ```
4. Explore projections:
   - Calendar view: `GET /views/calendar`
   - Weekly progress map: `GET /views/progress`

## Extending
- Swap storage by injecting a different `CloudStorage` implementation into `StateManager` in `todo_app/dependencies.py`.
- Add new feature modules by defining routers under `todo_app/routers/` and including them in `main.py`.
- Integrate real notification providers inside `NotificationService` without touching route signatures.

## Data persistence
State is saved to `data/state.json` by default. The folder is created automatically when the service starts.
