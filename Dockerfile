FROM python:3.12.9

# Set working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "main:app" , "--reload", "--host", "0.0.0.0", "--port", "8000"]
