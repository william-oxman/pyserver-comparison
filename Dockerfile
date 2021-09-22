FROM python:3.9

RUN pip install -r requirements.txt

EXPOSE 80

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]