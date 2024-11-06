# app/Dockerfile
FROM python:3.11-slim

# Install updates
RUN apt-get update && apt-get upgrade -y && apt-get install -y

# Set the working directory for the app
WORKDIR /app

# Copy app-specific requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code into the container
COPY src/ src/

# Copy the app boostrapper
COPY run.py .

# Expose the application port
EXPOSE 5000

# Command to run the app (e.g., a Flask app)
CMD ["python", "run.py"]