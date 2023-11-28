FROM python:3.11
RUN apt-get update && apt-get upgrade -y


WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

RUN pip install pytest-playwright

RUN playwright install-deps

RUN playwright install

COPY . .

ENV FLASK_APP=main.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]

