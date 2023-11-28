from datetime import datetime

from flask import Blueprint, request

# validator
from commons.validator import validate_body

# services
from services.scrapers import (
    get_saved_opinions,
    scrape_opinions,
    save_opinions,
    getta_session,
)


# models
from models.scrapers import Opinion, SendScraping, Order


router = Blueprint("scraper", __name__, url_prefix="/scraper")


def _add_id(opinions: list[Opinion]) -> list[dict]:
    if not opinions:
        return []
    return [{"id": i, **opinion.model_dump()} for i, opinion in enumerate(opinions)]


@router.route("/", methods=["GET"])
def get_opinions() -> list[Opinion]:
    opinions = get_saved_opinions()
    return _add_id(opinions)


@router.route("/", methods=["POST"])
def post_scrape_opinions() -> list[Opinion]:
    body: SendScraping = validate_body(request.json, SendScraping)
    opinions_list = scrape_opinions(Order[body.order])
    saved_opinions = save_opinions(opinions_list)

    return _add_id(saved_opinions)


@router.route("/Ta", methods=["GET"])
def get_ta_session() -> str:
    return getta_session()


@router.route("/Ta", methods=["POST"])
def post_ta_session() -> str:
    session = getta_session()
    with open("ta_session.txt", "a+") as f:
        text = f"{datetime.now()}: {session['TASession']}\n"
        f.write(text)
    return session
