from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/debug/http')
def debug_http():
    try:
        response = requests.get('https://www.google.com', timeout=10)
        return jsonify(
            status_code=response.status_code,
            url=response.url,
            headers=dict(response.headers),
            text=response.text[:200]  # first 200 chars of response body
        )
    except Exception as e:
        return jsonify(error=str(e))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)