hereimport os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

GEMINI_KEY = "AQ.Ab8RN6InDw1plCe9ECs4rp78HQqRCTamIdN5Zt0KrxtUtby8zA"
client = genai.Client(api_key=GEMINI_KEY)

@app.route('/api/generate-seo', methods=['GET'])
def generate_seo():
    topic = request.args.get('topic')
    
    if not topic:
        return jsonify({"status": "error", "message": "Topic parameter is required"}), 400

    try:
        prompt = f"You are an SEO expert. Generate an optimized Blog Title, 5 Keywords, and a short introduction paragraph for the topic: '{topic}'. Return the response strictly in clear JSON format with keys: title, keywords (as list), and introduction. Do not add markdown backticks."

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return jsonify({
            "status": "success",
            "topic": topic,
            "ai_response": response.text
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
