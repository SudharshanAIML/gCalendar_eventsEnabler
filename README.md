
# Google Calendar Event Creator

A Python application that allows you to create and manage Google Calendar events programmatically using the Google Calendar API.

## Features

- Create calendar events with custom details
- Add attendees to events
- Set event location and description
- Configure event timing with timezone support

## Prerequisites

- Python 3.6 or higher
- Google Cloud Platform account
- Google Calendar API enabled

## Setup

1. Clone the repository:
```bash
git clone https://github.com/SudharshanAIML/gCalendar_eventsEnabler.git
cd gCalendar_eventsEnabler
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Google Cloud Project:
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select an existing one
   - Enable the Google Calendar API
   - Create OAuth 2.0 credentials
   - Download the credentials and save as `credentials.json` in the project root

4. Configure OAuth:
   - Add `http://localhost:8080/` to the authorized redirect URIs in your Google Cloud Console
   - Place your `credentials.json` file in the project root directory

## Usage

Run the application:
```bash
python main.py
```

The first time you run the application, it will:
1. Open your default web browser
2. Ask you to sign in to your Google account
3. Request permission to access your calendar
4. Create a token.json file for future authentication

## Project Structure

- `main.py`: Main application file
- `credentials.json`: Google OAuth credentials (not included in repository)
- `token.json`: User authentication token (generated after first run)
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Security Note

- Never commit `credentials.json` or `token.json` to version control
- Keep your OAuth credentials secure
- Add these files to .gitignore

## License

MIT License 
