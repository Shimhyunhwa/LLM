# 드롭다운 메뉴로 과일을 고르고, 선택한 과일을 텍스트로 보여주는 프로그램
import gradio as gr

def handle_fruit(fruit): # 사용자가 선택한 과일 이름이 fruit이라는 변수에 들어옴 
    return f'선택한 과일: {fruit}' # 그걸 예쁘게 문자열로 바꿔서 돌려주는 함수

with gr.Blocks() as demo: # 화면(UI)을 구성하는 도화지를 꺼냄 # 그안에 필요한 부품들(드롭다운, 텍스트박스 등)을 올려놓는 것! 

    # 드롭다운 메뉴 만들기 
    fruit_dropdown = gr.Dropdown(label = "과일", choices=['사과', '오렌지','바나나','메론'])
    ## 사용자에게 과일 목록 중 하나를 고르도록 하는 메뉴
    ##label= "과일" → 드롭다운 위에 "과일"이라는 안내 문구가 보임.
    ## choices=[...] → 고를 수 있는 과일 종류 리스트

    # 출력용 텍스트 박스 
    output_fruit = gr.Textbox(label = '구입한 과일') #사용자가 고른 과일을 문장 형태로 보여주는 박스
    
    # 이벤트 연결 
    fruit_dropdown.change(handle_fruit, inputs= fruit_dropdown, outputs = output_fruit)
    ## fruit_dropdown: 우리가 만들었던 드롭다운 컴포넌트
    ## .change(...):무언가가 바뀌었을 때 동작해!(과일 선택이 바뀌었을 때~)
    
demo.launch()