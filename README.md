# Gammu SMS Web UI

This repository provides a minimal Flask application that displays SMS messages stored in a SQLite database. It demonstrates how to use the Python `gammu` bindings together with Flask and SQLAlchemy to build a simple SMSD WebUI.

## Getting Started

1. Install dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-gammu
   pip install Flask SQLAlchemy
   ```
2. Run the application:
   ```bash
   python3 -m smsweb.app
   ```
   The web interface will be available on `http://localhost:5000`.

Sample data is automatically loaded into `sms.db` on first start. The table view can be extended to integrate with your own SMS repository.
