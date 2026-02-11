# chatbot-agent
A simple text-based chat-bot agent that can take in user input, respond to user input and extend itself according to it's functional capabilities


##  Features
* **Multi-Model Support:** Powered by `litellm` to connect to OpenAI, Anthropic, or local LLMs.
* **Interactive UI:** Built with `streamlit` for a smooth user experience.
* **Google Integration:** Uses `google-generativeai` for advanced reasoning.

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
````

## Set up Virtual Environment (Recommended)

# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Configure your .env file
1. Create a .env file
2. Click here https://support.google.com/googleapi/answer/6158862?hl=en to learn how to set up a google api key to run agent.
3. Enter your Google Api Key into the file (possibly) in this format:
  GOOGLE_API_KEY=your_key_here
# Add any other keys required by LiteLLM


