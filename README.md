# Calendar Assistant Chatbot

A web-based chatbot application that helps manage your Google Calendar through natural language commands. Built with Flask, LangChain, and Composio tools.

![image](https://github.com/user-attachments/assets/4216b5da-370b-40ff-a167-e3c413d79fcb)

## Features

- Schedule meetings and events
- View upcoming events
- Update existing events
- Delete events
- Find free time slots
- Natural language processing for commands
- Modern, responsive UI

## Prerequisites

- Python 3.8 or higher
- Google Calendar API credentials
- Composio API key
- Groq API key

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:
```
COMPOSIO_API_KEY=your_composio_api_key
GROQ_API_KEY=your_groq_api_key
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Usage

The chatbot understands natural language commands. Here are some examples:

- "Schedule a meeting tomorrow at 5 PM"
- "Show my meetings this week"
- "Update the meeting on Friday to 6 PM"
- "Delete my meeting on Monday"
- "Find free slots for a 1-hour meeting"

## Project Structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
└── templates/
    └── index.html     # Chatbot interface
```

## License

MIT License 
