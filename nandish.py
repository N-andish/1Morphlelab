from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    name = "C Nandish"

    # System username (use getpass or fallback to environment variable)
    username = getpass.getuser()

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get the top (or ps) output
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # Return the formatted output
    result = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {server_time}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    
    return result

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)