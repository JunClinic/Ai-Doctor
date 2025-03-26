The main Flask application, showcasing modularity and professionalism.

```python
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from src.ai_engine import AIDiagnosticEngine
from src.config import Config
from src.utils import setup_logging
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize AI engine
ai_engine = AIDiagnosticEngine()

@app.route("/")
def index():
    """Render the main landing page."""
    logger.info("Rendering index page")
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    """Handle chat interactions with AI diagnostics."""
    if request.method == "GET":
        logger.info("Rendering chat page")
        return render_template("chat.html")
    
    if request.method == "POST":
        user_input = request.json.get("message")
        lang = request.json.get("lang", "en")
        logger.info(f"Received user input: {user_input} in language: {lang}")
        
        response = ai_engine.process_input(user_input, lang)
        logger.info(f"AI response: {response}")
        return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger.info(f"Starting Jun's Clinic on port {port}")
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
