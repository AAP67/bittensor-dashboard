from anthropic import Anthropic
from utils.knowledge import BITTENSOR_KNOWLEDGE

def get_response(question, live_data, api_key):
    client = Anthropic(api_key=api_key)
    
    system = f"""You are a Bittensor ecosystem analyst for a crypto fund.
Answer in 2-3 sentences max. Use specific numbers from the live data when available.
No fluff, no disclaimers. Be direct like a Bloomberg terminal.
Emission values are percentages (%). TAO Flow values are in TAO (τ). Prices are in USD.

{BITTENSOR_KNOWLEDGE}"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        system=system,
        messages=[
            {"role": "user", "content": f"Live Bittensor data:\n{live_data}\n\nQuestion: {question}"}
        ]
    )
    return message.content[0].text