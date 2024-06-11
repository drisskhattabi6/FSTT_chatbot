import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import gc

# Append the path for the RAG module
sys.path.append('../RAG')
from RAG import AIAgent, RAGSystem, extract_answer_from_text 

# Initialize global variables
ai_agent = None
rag_system = None

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/model", methods=["POST"])
def initialize_model():
    global ai_agent, rag_system
    try:
        # Get the model name from the request JSON
        data = request.json
        model = data.get("model", "")
        del ai_agent
        del rag_system
        gc.collect()
        if model == "rag":
            try:
                # Initialize the AI Agent
                ai_agent = AIAgent(model_name="google/gemma-2b-it")
                # Initialize the RAGSystem with the existing collection
                rag_system = RAGSystem(ai_agent=ai_agent, num_retrieved_docs=15)
                return jsonify({"response": True})
            except Exception as e:
                return jsonify({"response": False, "error": str(e)})
        else:
            ai_agent = AIAgent()
            rag_system = None
            return jsonify({"response": True})
    except Exception as e:
        # Return an error response
        return jsonify({"error": str(e)}), 500

@app.route("/query", methods=["POST"])
def handle_query():
    global ai_agent, rag_system
    try:
        # Get the prompt from the request JSON
        data = request.json
        prompt = data.get("prompt", "")
        context = data.get("prevRes", "")
        if rag_system is None:
            res = ai_agent.generate(prompt)
        else:
            res = rag_system.query(prompt)
        res = extract_answer_from_text(res)

        # Return the response
        return jsonify({"response": res})
    except Exception as e:
        # Return an error response
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8500)

