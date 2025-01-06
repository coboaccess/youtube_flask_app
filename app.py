# from flask import Flask, request, jsonify
# from flask import render_template
# import sqlite3
# from open_file_and_evaluate import channel_about_12_28_2024
# from historical import return_historical_data

# app = Flask(__name__)

# # Database connection
# def get_db_connection():
#     conn = sqlite3.connect('database.db')  # Connect to the database
#     conn.row_factory = sqlite3.Row        # Access rows as dictionaries
#     return conn

# # Initialize the database
# def init_db():
#     conn = get_db_connection()
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             keyword_arg TEXT NOT NULL,
#             compete_list TEXT NOT NULL,
#             line_complete TEXT NOT NULL,
#             date_posted DATETIME DEFAULT CURRENT_TIMESTAMP,
#             run_time TEXT NOT NULL,
#             used_in_content TEXT DEFAULT 'NO',
#             category TEXT DEFAULT 'Uncategorized'
#         )
#     ''')
#     conn.commit()
#     conn.close()


# # Route to run the Python script and load/update data
# @app.route('/run-script', methods=['POST'])
# def run_script():
#     """
#     This route processes data from the channel_about_12_28_2024 function 
#     and loads or updates it in the database. It is executed only when a POST request is made to /run-script.
#     """
#     # Generate data by calling the script
#     script_data = channel_about_12_28_2024()

#     conn = get_db_connection()
#     success_count = 0
#     for row in script_data:
#         # Check if an entry with the same keyword_arg exists
#         existing_entry = conn.execute('SELECT * FROM data WHERE keyword_arg = ?', (row['keyword_arg'],)).fetchone()

#         if existing_entry:
#             # Update existing entry (delete old entry first)
#             conn.execute('DELETE FROM data WHERE keyword_arg = ?', (row['keyword_arg'],))
#             run_time = "updated"
#         else:
#             # Insert new entry
#             run_time = "first run"

#         # Insert new or updated entry
#         conn.execute('''
#             INSERT INTO data (keyword_arg, compete_list, line_complete, run_time, category)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (row['keyword_arg'], row['compete_list'], row['line_complete'], run_time, row.get('category', 'Uncategorized')))
#         success_count += 1

#     conn.commit()
#     conn.close()

#     return jsonify({'message': f'Successfully added/updated {success_count} rows in the database.'}), 201

# # Route to run the Python script and load/update data
# @app.route('/run-script-historical', methods=['POST'])
# def run_script_historical():
#     """
#     This route processes data from the channel_about_12_28_2024 function 
#     and loads or updates it in the database. It is executed only when a POST request is made to /run-script.
#     """
#     # Generate data by calling the script
#     script_data = return_historical_data()

#     conn = get_db_connection()
#     success_count = 0
#     for row in script_data:
#         # Check if an entry with the same keyword_arg exists
#         existing_entry = conn.execute('SELECT * FROM data WHERE keyword_arg = ?', (row['keyword_arg'],)).fetchone()

#         if existing_entry:
#             # Update existing entry (delete old entry first)
#             conn.execute('DELETE FROM data WHERE keyword_arg = ?', (row['keyword_arg'],))
#             run_time = "updated"
#         else:
#             # Insert new entry
#             run_time = "first run"

#         # Insert new or updated entry
#         conn.execute('''
#             INSERT INTO data (keyword_arg, compete_list, line_complete, run_time, category)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (row['keyword_arg'], row['compete_list'], row['line_complete'], run_time, row.get('category', 'Uncategorized')))
#         success_count += 1

#     conn.commit()
#     conn.close()

#     return jsonify({'message': f'Successfully added/updated {success_count} rows in the database.'}), 201




# # Route to view all data
# @app.route('/view-data', methods=['GET'])
# def view_data():
#     conn = get_db_connection()
#     rows = conn.execute('SELECT * FROM data').fetchall()
#     conn.close()
#     return jsonify([dict(row) for row in rows])

# # Route to query data by keyword_arg
# @app.route('/query-keyword', methods=['GET'])
# def query_keyword():
#     keyword_arg = request.args.get('keyword_arg')
    
#     if not keyword_arg:
#         return jsonify({'error': 'keyword_arg is required'}), 400

#     conn = get_db_connection()
#     rows = conn.execute('SELECT * FROM data WHERE keyword_arg = ?', (keyword_arg,)).fetchall()
#     conn.close()

#     return jsonify([dict(row) for row in rows])

# # Route to query today's entries
# @app.route('/query-today', methods=['GET'])
# def query_today():
#     # Query for entries created today
#     conn = get_db_connection()
#     rows = conn.execute('SELECT * FROM data WHERE DATE(date_posted) = DATE("now")').fetchall()
#     conn.close()

#     # Return the results as JSON
#     return jsonify([dict(row) for row in rows])

# @app.route('/mark-as-used', methods=['POST'])
# def mark_as_used():
#     """
#     Marks an entry as used in content by updating the `used_in_content` field to 'YES'.
#     Expects a JSON payload with `keyword_arg` to identify the entry.
#     """
#     keyword_arg = request.json.get('keyword_arg')

#     if not keyword_arg:
#         return jsonify({'error': 'keyword_arg is required.'}), 400

#     conn = get_db_connection()
#     result = conn.execute('UPDATE data SET used_in_content = "YES" WHERE keyword_arg = ?', (keyword_arg,))
#     conn.commit()
#     conn.close()

#     if result.rowcount == 0:
#         return jsonify({'error': 'No entry found for the provided keyword_arg.'}), 404

#     return jsonify({'message': f'Keyword {keyword_arg} marked as used in content.'})

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     init_db()  # Initialize database when starting the app
#     app.run(debug=True)
