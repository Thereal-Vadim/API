from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quote')
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        if response.status_code == 200:
            data = response.json()
            quote = {
                'content': data['content'],
                'author': data['author']
            }
            return jsonify(quote)
        else:
            return jsonify({'error': 'Failed to fetch quote'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
