from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
MODEL_NAME="gemini-2.5-flash-lite"
AGENT_TEMPERATURE = 0.7
RETRY_CONFIG=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)