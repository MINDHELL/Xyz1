# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy bot files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for health check
EXPOSE 8080

# Start the bot
CMD ["python", "main.py"]
