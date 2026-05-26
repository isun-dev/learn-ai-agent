from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

while True:
    user_input = input("사용자: ")
    if user_input == "exit":
        break
    
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=[
            {"role": "system", "content": "너는 사용자를 도와주는 상담사야"},
            {"role":"user", "content": user_input},

        ],
    )
    print("AI: ", response.choices[0].message.content)
''' 싱글턴
사용자: 안녕, 내이름은 홍길동이야
AI:  안녕하세요, 홍길동님! 만나서 반갑습니다. 어떻게 도와드릴까요?
사용자: 내 이름이 뭘까?
AI:  죄송하지만, 저는 사용자의 개인 정보를 알 수 없습니다. 이름이나 기타 개인 식별 정보를 저장하거나 기억하지 않습니다. 어떻게 도와드릴까요?
사용자: exit'''