from pydantic import BaseModel


def validate_body(body: list | dict, model: BaseModel) -> list[BaseModel] | BaseModel:
    if body is None:
        raise ValueError("Body is required")

    if isinstance(body, str):
        raise ValueError("Body must be a json")
    elif isinstance(body, list):
        return [model(**item) for item in body]
    return model(**body)
