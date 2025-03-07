from groq import Groq
from configs.settings import GROQ_API_KEY


def draft_answer(context):
    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    You are an expert research assistant. Based on the VERIFIED CONTEXT below, draft a professional, clear, and highly informative answer.

    Guidelines:
    - Use formal, neutral, and academic language.
    - Organize the answer with logical flow and clear paragraphs.
    - Emphasize factual accuracy, and avoid speculation.
    - Make sure the answer can stand alone without needing to read the context.
    - DO NOT include citations here; citations are handled separately.
    
    VERIFIED CONTEXT:
    {context}

    FINAL ANSWER:
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You provide clear, factual, and helpful research answers with excellent structure."},
            {"role": "user", "content": prompt}
        ],
        model="mixtral-8x7b-32768",
        temperature=0.6,  
        max_tokens=2048,
    )

    return response.choices[0].message.content.strip()
