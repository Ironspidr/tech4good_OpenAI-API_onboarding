from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = "Provide a valid JSON object. Write a haiku about recursion in programming."
followup = "Provide a valid JSON object. The haiku should also about the Big-O notation."

resp1 = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "Provid output in valid JSON. You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

data = resp1.choices[0].message.content

print(data)

followup = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "Provide output in valid JSON. You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": data
        },
        {
            "role": "user",
            "content": followup
        }
    ]
)

followup_data = followup.choices[0].message.content

print(followup_data)

