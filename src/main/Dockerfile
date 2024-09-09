FROM python:3.12
RUN mkdir -p app
WORKDIR /home/root/app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${BACKEND_PORT}
CMD ["python", "main.py"]