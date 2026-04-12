FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8001

CMD ["gunicorn", "littlelemon.wsgi:application", "--bind", "0.0.0.0:8001"]