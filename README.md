# AI Text Completion App

A simple command-line application that uses OpenAI’s GPT-3.5-turbo model to complete text prompts. Enter any prompt, and the app will generate a continuation or response.

## Features
- Interactive prompt loop  
- Handles empty or too-long inputs  
- Graceful error messages for API issues  
- Fixed generation settings (temperature, max_tokens, top_p)

## Prerequisites
- Python 3.8 or newer  
- An OpenAI API key (sign up at https://platform.openai.com)

## Setup

1. **Clone or download** this repo into a folder:  
   ```bash
   git clone https://github.com/your-username/ai-text-completion-project.git
   cd ai-text-completion-project
   ```

2. **Create & activate a virtual environment**:  
   ```bash
   python -m venv venv
   ```

   **Then activate it:**

   - On **Windows (PowerShell)**:  
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On **macOS/Linux**:  
     ```bash
     source venv/bin/activate
     ```

3. **Install required packages**:  
   ```bash
   pip install openai python-dotenv
   ```

4. **Configure your API key**:  
   - Create a file named `.env` in the root project directory  
   - Add your key inside the file:  
     ```ini
     OPENAI_API_KEY=sk-YourSecretAPIKeyHere
     ```

## Usage

Run the app using:

```bash
python text_completion_app.py
```

You’ll see:
```text
=== Text Completion App ===
Type 'quit' or leave empty to exit.

Prompt:
```

- Type any sentence or question and press Enter  
- The app will generate and print a response  
- Type `quit` or press Enter on an empty line to exit  

## Example

```text
Prompt: explain recursion like I'm five
→ Recursion is like holding a mirror in front of another mirror...
```

## Customizing Defaults

If you want to experiment with different generation settings, edit the constants near the top of `text_completion_app.py`:

```python
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS  = 150
DEFAULT_TOP_P       = 1.0
```

Adjust those values, save, and re-run the app to see how the outputs change.

## Dependencies

- `openai`
- `python-dotenv`

## Project Structure

```text
ai-text-completion-project/
├── .env                # your API key (not tracked)
├── text_completion_app.py
└── README.md
```

Feel free to tweak, extend, or integrate this into a larger project. Happy prompting!
