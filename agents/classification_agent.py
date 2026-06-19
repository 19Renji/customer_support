from services.llm_service import llm

def classify_issue(transcript):

    prompt = f"""
    You are a customer support classification agent.

    Classify the issue into EXACTLY ONE category from this list:

    - Login Failure
    - Payment Issue
    - Refund Request
    - Technical Issue
    - General Inquiry

    Rules:
    1. Return ONLY one category.
    2. Do not invent new categories.
    3. If the customer is asking a general question, use General Inquiry.
    4. If unsure, use General Inquiry.

    Transcript:
    {transcript}
    """

    response = llm.invoke(prompt)

    return response.content.strip()