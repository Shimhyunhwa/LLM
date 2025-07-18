import gradio as gr

def handle_input(text):  # 입력받은 text라는 글자를 그대로 돌려주는(출력하는) 역할
    return text


# Gradio 인터페이스 만들기

# with문: 어떤 작업의 시작과 끝을 정리해서 처리할 때  쓰는 문법
with gr.Blocks() as demo: # Blocks(): 우리가 UI(화면)를 만들겠다고 선언하는 레고판 
    # 입력박스만들기
    text_input = gr.Textbox(label = "문자입력", lines =1)
    # Textbox():글을 입력할 수 있는 상자 # label="문자입력": 박스 위에 보이는 글자 # lines=1: 한 줄만 입력할거야!
    
    # 출력박스(위에서 입력한 값을 보여줄 출력전용 박스) 만들기
    output_text = gr.Textbox(label = "출력") # label="출력": 박스 위에 "출력"이라고 써 놓을 수있음

    # 이벤트 연결하기 
    text_input.submit(handle_input, inputs = text_input, outputs = output_text) 
    # text_input.submit: 사용자가 Enter 눌렀을 때만 반응하게 하고 싶음
    # fn=handle_input: 위에서 만든 함수를 사용할 것임 
    # inputs=text_input: 사용자 입력을 함수에 넣음
    # outputs=output_text: 함수의 결과를 여기 출력

demo.launch() # Gradio 앱을 실행하는 버튼

## 전체요약
# 1) 글을 입력하면
# 2) handel_input 함수가 입력을 받아서 
# 3) 그대로 다시 출력하고 
# 4) 출력 박스에 결과가 보임 