from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# AI assistant functions
def improve_text(text, task_type):
    """
    Improve text using AI assistance.
    This is a simple implementation that can be extended with actual AI API calls.
    """
    if not text or not text.strip():
        return {"error": "Please provide text to improve"}
    
    # For now, we'll provide simple text improvements
    # In production, this would call an AI API (OpenAI, etc.)
    improvements = {
        "grammar": f"[Grammar Check] {text}",
        "style": f"[Style Enhancement] {text}",
        "expand": f"[Text Expansion] {text}\n\nAdditional context and details can be added here to make the text more comprehensive.",
        "summarize": f"[Summary] {text[:100]}..." if len(text) > 100 else f"[Summary] {text}",
        "translate": f"[Translation] {text}",
        "creative": f"[Creative Writing] {text}\n\nWith enhanced creative elements and engaging narrative."
    }
    
    return {
        "original": text,
        "improved": improvements.get(task_type, text),
        "task_type": task_type
    }

def use_ai_api(text, task_type):
    """
    Use OpenAI API for text assistance.
    Requires OPENAI_API_KEY environment variable.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        # Fallback to simple improvement if no API key
        return improve_text(text, task_type)
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        prompts = {
            "grammar": "Please correct any grammar and spelling errors in the following text:",
            "style": "Please improve the writing style and make it more professional:",
            "expand": "Please expand on this text with more details and context:",
            "summarize": "Please provide a concise summary of this text:",
            "translate": "Please translate this text to English (if not already in English):",
            "creative": "Please enhance this text with creative writing elements:"
        }
        
        prompt = prompts.get(task_type, "Please improve this text:")
        full_prompt = f"{prompt}\n\n{text}"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        improved_text = response.choices[0].message.content
        
        return {
            "original": text,
            "improved": improved_text,
            "task_type": task_type
        }
    except Exception as e:
        return {"error": f"AI API error: {str(e)}"}

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/assist', methods=['POST'])
def assist():
    """Process text assistance request"""
    data = request.get_json()
    text = data.get('text', '')
    task_type = data.get('task_type', 'grammar')
    use_api = data.get('use_api', False)
    
    if use_api:
        result = use_ai_api(text, task_type)
    else:
        result = improve_text(text, task_type)
    
    return jsonify(result)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "AI Writing Assistant is running"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
