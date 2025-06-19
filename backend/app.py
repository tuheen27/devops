from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_form():
    data = request.form
    print("Received:", data)
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
