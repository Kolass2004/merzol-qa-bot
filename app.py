from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    context = data['context']
    question = data['question']
    
    # Call the function
    answer = answer_question(context, question)
    
    # Return the response
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
