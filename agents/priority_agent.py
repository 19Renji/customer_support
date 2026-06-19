from services.llm_service import llm

def determine_priority(transcript):

    prompt = f"""
    Determine priority.

    Choose ONLY one:

    - High
    - Medium
    - Low

    Transcript:
    {transcript}

    Return ONLY one value.
    """

    response = llm.invoke(prompt)

    return response.content.strip()