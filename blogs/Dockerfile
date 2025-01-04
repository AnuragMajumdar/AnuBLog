FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies for bash and netcat
RUN apt-get update && apt-get install -y \
    bash \
    netcat-openbsd \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . /app/

# Add wait-for-it.sh for handling database readiness
COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expose the port the app will run on
EXPOSE 8000

# Use bash for wait-for-it script, apply migrations, and run the Django server
ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--"]

# Automate migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
