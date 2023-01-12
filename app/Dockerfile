FROM python:3.11-slim

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /code

COPY ./src /code

# Creates a non-root user with an explicit UID and adds permission to access the /code folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
