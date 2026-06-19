from pydantic import BaseModel


class TranscriptRequest(
    BaseModel
):

    customer_email: str

    transcript: str