from flask import Flask, send_file
import os

app = Flask(__name__)

# Get port from environment variable for cloud deployment
port = int(os.environ.get('PORT', 8080))

@app.route('/')
def index():
    try:
        with open('src/index.html', 'r') as f:
            content = f.read()
        return content, 200, {'Content-Type': 'text/html'}
    except Exception as e:
        return f"""
        <html>
            <body>
                <h1>Error loading page</h1>
                <pre>{str(e)}</pre>
            </body>
        </html>
        """, 500

@app.route('/words.csv')
def words():
    try:
        return send_file('words.csv', mimetype='text/csv')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
