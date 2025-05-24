# Local Time Agent

This agent uses the Gemini API to provide the current local time for a given city.

## Setup Instructions

1.  **Set GOOGLE_API_KEY:**
    You need to set the `GOOGLE_API_KEY` environment variable to your Google API key.
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY"
    ```
    Replace `"YOUR_API_KEY"` with your actual key.

2.  **Install Dependencies:**
    Navigate to the project directory and run:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Agent

To start the agent, run:
```bash
python main.py
```
The agent will then prompt you to enter a city name. Type 'exit' or 'quit' to stop.

## Running Tests

To run the unit tests, navigate to the project root directory and execute:
```bash
python -m unittest discover tests
```
