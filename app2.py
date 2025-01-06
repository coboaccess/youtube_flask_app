from flask import Flask, jsonify, render_template

app2 = Flask(__name__)

# Data to display
video_data = [
    ['aR64zIGEXz4', 'Expert Python Programmer Shares Top UV Python Secrets!', '214', '0', 0, '0', '2024-12-27T16:16:21Z'],
    ['C81FYXVJoV8', 'How to Close All MT4 Positions at Once: Quick and Easy Steps', '116', '1', 0, '0', '2024-12-23T17:16:24Z'],
    ['XzzNqbKwbQ8', 'Weekly Passive Income Trading Stock Options on MT4 and MT5', '99', '1', 0, '0', '2024-12-22T15:01:33Z'],
    ['iYrYePJ-AXo', 'Why Settle? Go Big with Custom MT4MT5 Bots Over Copy Trading!', '19', '0', 0, '0', '2024-12-18T15:50:10Z'],
    ['JEYYEwZUZJw', 'MT5 Explained: How to Become an Algorithmic Trader', '215', '1', 0, '0', '2024-12-17T12:05:25Z'],
]

# Route to fetch the data
@app2.route('/api/videos', methods=['GET'])
def get_videos():
    return jsonify(video_data)

# Route to render the HTML page
@app2.route('/')
def index():
    return render_template('index2.html')

if __name__ == '__main__':
    app2.run(debug=True, port=5001)  # Different port for app2
