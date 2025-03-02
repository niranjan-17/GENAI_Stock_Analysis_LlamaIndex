# Use official Python image as base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files to the container
COPY requirements.txt .
COPY app.py .
COPY src/ ./src/
COPY articles/ ./articles/
COPY storage/ ./storage/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
