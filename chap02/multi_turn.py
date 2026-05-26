from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) # 오픈 AI 클라이언트 인스턴스 생성

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=messages,
    )
    return response.choices[0].message.content

messages = [
    {"role":"system", "content": "너는 사용자를 도와주는 상담사야"},
]

while True:
    user_input = input("사용자 : ")
    if user_input == "exit":
        break

    messages.append({"role": "user", "content": user_input})
    ai_response = get_ai_response(messages)
    messages.append({"role": "assistant", "content": ai_response}) # 이 방식을 통해 GPT와 사용자가 나눈 대화가 messages에 저장된 상태로 대화를 이어나갈 수 있다
    print("AI : ", ai_response)

'''
사용자 : 안녕? 내이름은 홍길동이야
AI :  안녕하세요, 홍길동님! 만나서 반갑습니다. 오늘 어떻게 도와드릴까요?
사용자 : 내가 누구 게?
AI :  홍길동님은 아마 한국의 고전 소설 속 캐릭터를 연상시키는 이름을 가지고 계신 것 같네요. 하지만 실제로는 어떤 분이신지 더 알고 싶어요. 자신에 대해 더 말씀해주실 수 있나요?
사용자 : 미국에서 인기있는 연예인은 누구야?
AI :  미국에서 인기 있는 연예인은 시기와 트렌드에 따라 달라질 수 있지만, 몇몇 이름은 꾸준히 인기를 끌고 있습니다. 예를 들어:

1. **테일러 스위프트 (Taylor Swift)** - 싱어송라이터로서 많은 히트곡을 가지고 있으며, 다양한 음악 상을 수상했습니다.
2. **드웨인 존슨 (Dwayne "The Rock" Johnson)** - 배우와 프로레슬러로, 그의 카리스마와 다양한 영화 출연 덕분에 많은 사랑을 받고 있습니다.
3. **비욘세 (Beyoncé)** - 가수이자 배우로, 그녀의 음악과 무대 매너로 큰 인기를 끌고 있습니다.
4. **톰 크루즈 (Tom Cruise)** - 다수의 블록버스터 영화에 출연한 배우로, 그의 액션 연기로 유명합니다.
5. **킴 카다시안 (Kim Kardashian)** - 리얼리티 TV 스타이자 사업가로, 그녀의 영향력은 패션과 미디어에까지 미치고 있습니다.

이 외에도 많은 연예인들이 큰 인기를 누리고 있습니다. 특정한 분야나 장르에 따라 다른 이름들이 떠오를 수 있습니다.
사용자 : 한국에서는 어때?
AI :  한국에서 인기 있는 연예인들도 여러 분야에 걸쳐 다양합니다. 최근 몇 년간 주목받는 이름들을 몇 가지 소개하겠습니다:

1. **방탄소년단 (BTS)** - 전 세계적으로 큰 인기를 끌고 있는 보이그룹으로, 그들의 음악과 퍼포먼스는 많은 팬들에게 사랑받고 있습니다.

2. **블랙핑크 (BLACKPINK)** - 글로벌한 인기를 자랑하는 걸그룹으로, 그들의 스타일과 음악은 많은 이들의 주목을 받고 있습니다.

3. **송중기** - 다양한 드라마와 영화에서 활약한 배우로, 그의 연기력과 매력으로 많은 팬들의 사랑을 받고 있습니다.

4. **박보검** - 그의 따뜻한 이미지와 뛰어난 연기력으로 많은 드라마와 영화에서 인기를 끌고 있는 배우입니다.

5. **아이유 (IU)** - 가수이자 배우로, 그녀의 음악적 재능과 연기 실력은 많은 사랑을 받고 있습니다.

이 외에도 다양한 분야에서 많은 연예인들이 활발히 활동하고 있으며, 특정 드라마나 예능 프로그램의 인기에 따라 유행이 달라질 수 있습니다.
'''