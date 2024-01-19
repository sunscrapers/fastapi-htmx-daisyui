###############
# BUILD IMAGE #
###############
FROM mcr.microsoft.com/playwright:v1.41.0-jammy

# Install Ubuntu requirements
RUN apt update && apt install -y python3-pip

# Install requirements
RUN pip install --upgrade pip
COPY ./e2e_tests/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Install playwright dependencies
RUN playwright install

# Copy project files
COPY ./e2e_tests /e2e_tests
WORKDIR e2e_tests
