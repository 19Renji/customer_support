from services.llm_service import llm

def detect_intent(transcript):

    prompt = f"""
    Identify customer intent.

    Choose EXACTLY ONE:

    - Account Issue
    - Billing Issue
    - Technical Support
    - Refund Request
    - General Inquiry

    Rules:
    1. Return ONLY one option.
    2. Do not explain.

    Transcript:
    {transcript}
    """

    response = llm.invoke(prompt)

    return response.content.strip()