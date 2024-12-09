from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    print(f"Received message: {message}")  # Log the received message

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([message])
        generated_response = response.text.strip()

        print(f"Response from Google Generative AI: {generated_response}")  # Log the response
        return jsonify({"response": generated_response})

    except Exception as e:
        print(f"Error: {str(e)}")  # Log any errors
        return jsonify({"error": "Failed to generate a response"}), 500

if __name__ == '__main__':
    app.run(debug=True)
