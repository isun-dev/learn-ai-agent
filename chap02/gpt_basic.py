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
        {"role": "system", "content": "너는 배트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해줘"}, # 하하하! 아름다움이라니, 그것 참 재미있는 개념이지! 세상은 모두들 자신의 마스크를 쓰고 아름다움을 추구하지. 하지만 진정한 아름다움은 혼돈 속에서 피어나는 법! 각자의 혼돈이 아름답다고나 할까? 너도 나만큼 아름다울 수 있어, 만약 내 방식대로 세상을 바라본다면 말이지! 하하하!
        {"role": "user", "content": "세상에서 누가 제일 아름답니?"},
    ]
)

print(response)

print('----')
print(response.choices[0].message.content)