from groq import Groq
from configs.settings import GROQ_API_KEY


def fact_check(context):

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    You are a professional fact checker. Review the following research context for factual accuracy. 
    Correct any errors, remove misinformation, and provide a clean, reliable version.

    Context:
    {context}

    Provide the corrected context below:
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You strictly check facts and provide only accurate, verified information."},
            {"role": "user", "content": prompt}
        ],
        model="mixtral-8x7b-32768",
        temperature=0.3,
        max_tokens=2048,
    )

    return response.choices[0].message.content.strip()
