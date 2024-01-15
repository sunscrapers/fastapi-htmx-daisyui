FROM python:3.11.7-slim

ENV PYTHONPATH=/src

# Install Node.js
RUN apt update && apt install -y nodejs npm

# Install requirements
ARG REQUIREMENTS_FILE=base.txt
ADD requirements/${REQUIREMENTS_FILE} requirements.txt
RUN pip install pip --upgrade && pip install -r requirements.txt

# Copy project
ADD /app /src/app
ADD /tailwindcss/ /src

# Set workdir
WORKDIR /src

# Install Tailwind CSS
RUN npm install
RUN npm run build:tailwindcss
RUN npm run build:htmx
RUN npm run build:daisyui

# Command to run when image started
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
