FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "80", "--host", "0.0.0.0"]