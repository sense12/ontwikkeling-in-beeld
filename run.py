from flask import Flask
import os

@app.route('/')
def index():
	return "Hello from Flask!"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)

