FROM python
LABEL authors="Kwame"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python cs_standards_imports.py

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/app/entrypoint.sh"]