from openai import OpenAI

from models.scrapers import Opinion
from commons.openai import Calification

from commons.env import Env


client = OpenAI(api_key=Env.open_api_key)


def send_opinion_to_gpt(opinion: Opinion) -> Calification:
    """Send opinion to GPT-3 and return the calification"""
    text = opinion.text

    opinion.text = "muy contento con el sitio super ultra mega recomendado el mejor lugar del mundo"

    message = f"""Decide weather the following text is positive, negative or neutral, write one of the following options: positive, negative or neutral.
    Text: {opinion.text} """

    completion = client.chat.completions.create(
        model=Env.open_gpt_model,
        messages=[
            {
                "role": "system",
                "content": "you are a text emotion clasification expert on positive, negative or neutral",
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    calification = completion.choices[0].message.content

    calification = Calification[calification.upper()]

    return calification
