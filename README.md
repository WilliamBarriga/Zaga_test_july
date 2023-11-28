# Instructions

To execute the flask application, run the following commands:

```bash
docker-compose build --no-cache
docker-compose up
```

if you don't want to use docker, you can run the following commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest-playwright
playwright install

export FLASK_APP=main.py
python -m flask run --host=0.0.0.0 --port=8000
```

---
# REST API


## Scraping
```http
GET /scraper
```

get the scraped opinions from the website if there are any otherwise return an empty list


```http
POST /scraper
```

scrape the opinions from the website and return the scraped opinions

- Body:

```json
{
    "order": "asc",
}
```

| Parameter | Type     | Description                                                             |
| :-------- | :------- | :---------------------------------------------------------------------- |
| `order`   | `string` | **Required**. Options:`asc`, `desc` order the scraped opinions by score |

```http
GET /scraper/Ta
```
get the saved TaSession Cookie

```http
POST /scraper/Ta
```
save the TaSession Cookie into a file on the container



## Openai
```http
POST /openai
```

Send a scraped opinion to the openai api and return and save the identified category. (you can check the opinion category with the `GET /scraper` endpoint)

- Body:

```json
{
    "id": 1,
}
```

| Parameter | Type  | Description                                                                                                  |
| :-------- | :---- | :----------------------------------------------------------------------------------------------------------- |
| `id`      | `int` | **Optional**. The id of the opinion to send to the openai api if not provided the first opinion will be sent |

# Spended time
- scraping: 2h
- openai: 20min
- flask: 1h




---
# Python Challenge

## Introduction

This challenge is for a candidate who is passionate about Machine Learning and has strong competency with Python.

We are not aiming to take too much of your personal time for this challenge, and it is intended to be completed in 3
hours. We expect to see how you approach and solve the problem, and not the most perfect written code.

This challenge consists in a scrapping bot that will be used to extract data from a website. This text will be then 
marked as positive, neutral or negative.

 