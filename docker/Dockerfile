# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for code and files
RUN mkdir code
RUN mkdir files

COPY app.py code/

# Set the working directory to the code directory
WORKDIR /app/code

# Expose the port Flask will run on
EXPOSE 8000

# Command to run the Flask application
CMD ["python", "app.py"]