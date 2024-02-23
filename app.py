from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

def read_file_content(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
    return content
    
@app.route('/')
def hello():    
    # Get current date and time
    now = datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    # File path
    file_path = '/app/files/your_file.txt'
    

    # Open file in append mode
    with open(file_path, 'a+') as file:
        # Read existing content
        content = file.read()
        
        # Move cursor to the beginning of the file
        file.seek(0, 0)
        
        # Write current date and time at the top
        file.write(f'Current date and time: {current_datetime}<br>')
        
        # Write back the existing content
        file.write(content)
        
    # Read file content
    file_content = read_file_content(file_path)
    
    return file_content

if __name__ == '__main__':

    app.run(port=8081,host='0.0.0.0')
