FROM python:3.10.0

WORKDIR /app

COPY /back/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

WORKDIR /app/back

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]