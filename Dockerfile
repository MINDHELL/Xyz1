# Use Python 3.9 as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for health check
EXPOSE 8080

# Run bot
CMD ["python", "main.py"]
