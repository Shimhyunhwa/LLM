import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv() # dotenv파일을 읽어올수있음 

client = OpenAI( # GPTAI와 연결하는 함수  # client 는 연결객체
    api_key = os.getenv("API_KEY") # Env에있는 API_KEY변수를 읽어오게됨 
) 

# temperature: 출력의 무작위성(창의성), Scope: 0.0 <= x < 1.0 
# 값이 낮을 수록 결정론적(늘 비슷한 값이 나옴), 높을수록 무작위성 
# 0.0 : 항상 같은 입력 -> 같은 출력 (답, 수학, 정답형 질문에 이용)
# 0.x : 적당한 무작위성 (마케팅 문구, 스토리 작성에 이용)

response = client.chat.completions.create(
    model = "gpt-4.1-2025-04-14", # 모델 이름 
    messages = [
        {"role": "user", "content":"왜 강남은 강남이라고 할까요?"}
    ],temperature= 0.0 
)

# print(response)

print(response.choices[0].message.content)
