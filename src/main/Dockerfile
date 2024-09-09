FROM python:3.12
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${BACKEND_PORT}
CMD ["python", "main.py"]