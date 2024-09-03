from flask import Flask, request, jsonify, send_from_directory
import json
import os
import threading
import time
import pyautogui
import keyboard

app = Flask(__name__)
CONFIG_FILE = 'config.cfg'

DEFAULT_CONFIG = {
    'theme': 'black',
    'hotkey': 'o',
    'milliseconds': 1000,  # Default to 1000 ms (1 second)
    'seconds': 0,
    'minutes': 0,
    'hours': 0
}

clicking_enabled = False
click_thread = None
click_interval_ms = DEFAULT_CONFIG['milliseconds']  # Default interval in ms
interval_event = threading.Event()

def read_config():
    """Read the configuration from the config file."""
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return DEFAULT_CONFIG

def write_config(config):
    """Write the configuration to the config file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def auto_clicker():
    """Perform auto-clicking at the specified interval."""
    global clicking_enabled, click_interval_ms
    while clicking_enabled:
        pyautogui.click()
        time.sleep(click_interval_ms / 1000)  # Convert ms to seconds

def start_clicking():
    """Start auto-clicking if not already started."""
    global clicking_enabled, click_thread
    if not clicking_enabled:
        clicking_enabled = True
        click_thread = threading.Thread(target=auto_clicker)
        click_thread.start()
        return 'started'
    return 'already running'

def stop_clicking():
    """Stop auto-clicking if currently running."""
    global clicking_enabled
    if clicking_enabled:
        clicking_enabled = False
        if click_thread:
            click_thread.join()
        return 'stopped'
    return 'already stopped'

@app.route('/')
def index():
    """Serve the main HTML file."""
    return send_from_directory('.', 'main.html')

@app.route('/start', methods=['POST'])
def start():
    """Start auto-clicking with the specified interval."""
    global click_interval_ms
    data = request.json
    milliseconds = data.get('milliseconds', 0)
    seconds = data.get('seconds', 0)
    minutes = data.get('minutes', 0)
    hours = data.get('hours', 0)
    
    # Calculate interval in milliseconds
    click_interval_ms = int(milliseconds) + int(seconds) * 1000 + int(minutes) * 60 * 1000 + int(hours) * 3600 * 1000
    
    # Update config file
    config = read_config()
    config['milliseconds'] = int(milliseconds)
    config['seconds'] = int(seconds)
    config['minutes'] = int(minutes)
    config['hours'] = int(hours)
    write_config(config)
    
    status = start_clicking()
    return jsonify({'status': status, 'interval': {'milliseconds': click_interval_ms}})

@app.route('/stop', methods=['POST'])
def stop():
    """Stop the auto-clicking."""
    status = stop_clicking()
    return jsonify({'status': status})

@app.route('/config', methods=['GET', 'POST'])
def config():
    """Get or update configuration."""
    if request.method == 'GET':
        return jsonify(read_config())
    elif request.method == 'POST':
        data = request.json
        config = read_config()
        config.update(data)
        write_config(config)
        return jsonify({'status': 'saved'})

@app.route('/status', methods=['GET'])
def status():
    """Get the current status of auto-clicking."""
    return jsonify({'status': 'running' if clicking_enabled else 'stopped'})

@app.route('/updateInterval', methods=['POST'])
def update_interval():
    """Update the interval for auto-clicking."""
    global click_interval_ms
    data = request.json

    print(f"Received data: {data}")

    # Extract interval values from the nested structure
    interval = data.get('interval', {})
    milliseconds = interval.get('milliseconds', 0)
    total_seconds = interval.get('totalSeconds', 0)

    try:
        # Convert values to integers
        milliseconds = int(milliseconds)
        total_seconds = int(total_seconds)
        
        print(f"Parsed values - Milliseconds: {milliseconds}, TotalSeconds: {total_seconds}")

        # Calculate the total milliseconds from totalSeconds
        total_milliseconds = total_seconds * 1000

        # Update interval in milliseconds
        click_interval_ms = milliseconds + total_milliseconds

        # Update config file
        config = read_config()
        config['milliseconds'] = milliseconds
        config['totalSeconds'] = total_seconds
        write_config(config)

        # Log current settings and calculated interval
        print(f"Calculated interval (ms): {click_interval_ms}")
        print(f"Config file updated: {config}")

        return jsonify({'status': 'updated', 'interval': {'milliseconds': click_interval_ms}})
    
    except Exception as e:
        print(f"Error updating interval: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    config = read_config()
    hotkey = config.get('hotkey', 'o')

    def toggle_clicking():
        """Toggle the clicking state."""
        if clicking_enabled:
            stop_clicking()
        else:
            start_clicking()

    keyboard.add_hotkey(hotkey, toggle_clicking)
    
    app.run(debug=True)