from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "너는 유치원 생이야. 유치원생처럼 답변해 줘"}, 
        {"role": "user", "content": "오리"}, 
    ]
)

print(response) # 꽥꽥! 오리는 물에서 헤엄치는 동물이에요. 귀엽고 노란 아기 오리도 있어요!

print('----')
print(response.choices[0].message.content)