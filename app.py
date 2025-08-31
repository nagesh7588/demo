from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # App Settings appear exactly as you named them
    app_setting = os.environ.get('APP_SETTING_EXAMPLE', 'Not set')

    # Connection Strings are prefixed by Azure depending on type
    # For Custom → CUSTOMCONNSTR_
    # For SQLAzure → SQLCONNSTR_
    # For MySQL → MYSQLCONNSTR_
    # For PostgreSQL → PGSQLCONNSTR_
    connection_string = (
        os.environ.get('CUSTOMCONNSTR_CONNECTION_STRING_EXAMPLE')
        or os.environ.get('SQLCONNSTR_CONNECTION_STRING_EXAMPLE')
        or os.environ.get('MYSQLCONNSTR_CONNECTION_STRING_EXAMPLE')
        or os.environ.get('PGSQLCONNSTR_CONNECTION_STRING_EXAMPLE')
        or 'Not set'
    )

    return f"""
    <h1>Azure Environment Variables Demo</h1>
    <p><b>App Setting (APP_SETTING_EXAMPLE):</b> {app_setting}</p>
    <p><b>Connection String (CONNECTION_STRING_EXAMPLE):</b> {connection_string}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
