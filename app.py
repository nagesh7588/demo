from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    app_setting = os.environ.get('APP_SETTING_EXAMPLE', 'Not set')
    connection_string = os.environ.get('CONNECTION_STRING_EXAMPLE', 'Not set')
    return f"""
    <h1>Azure Environment Variables Demo</h1>
    <p><b>App Setting (APP_SETTING_EXAMPLE):</b> {app_setting}</p>
    <p><b>Connection String (CONNECTION_STRING_EXAMPLE):</b> {connection_string}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
