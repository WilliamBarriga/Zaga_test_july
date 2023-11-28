from flask import Blueprint, request

# validator
from commons.validator import validate_body

# services
from services.scrapers import get_saved_opinions, update_calification
from services.openai import send_opinion_to_gpt

# models
from models.openai import SendOpinion


router = Blueprint("openai", __name__, url_prefix="/openai")


@router.route("/", methods=["POST"])
def send_opinion():
    try:
        body: SendOpinion = validate_body(request.json, SendOpinion)

    except:
        body = None

    opinions = get_saved_opinions()
    calification = send_opinion_to_gpt(opinions[body.id] if body else opinions[0])
    update_calification(body.id if body else 0, calification)

    return {"calification": calification.name}
