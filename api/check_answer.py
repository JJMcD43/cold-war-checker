# check_answer.py
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/api/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data['answer']
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Is the following answer correct for a Cold War question? '{user_answer}'",
        max_tokens=50
    )

    ai_feedback = response.choices[0].text.strip()
    is_correct = "correct" in ai_feedback.lower()

    return jsonify({
        "feedback": ai_feedback,
        "isCorrect": is_correct
    })
