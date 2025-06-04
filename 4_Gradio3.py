# 체크박스를 체크하면 그에 따라 메시지를 출력하는 간단한 동의 창 만들기 

import gradio as gr # Gradio라는 도구 상자를 꺼내고, 그걸 gr이라는 짧은 이름으로 부를거야! 

def handle_checkbox(selected): # 사용자가 체크박스에 체크(✔)했는지 안 했는지 여부를 알려줄거야! 
    if selected: # 혹시 selected 값이 있으면
        return "동의했습니다!"
    return "동의하지 않았습니다!"  # 체크박스는 True(체크됨) 또는 False(체크 안됨) 값을 selected라는 변수에 전달함

with gr.Blocks() as demo: # UI 조립 시작! Blocks은 화면에 어떤 것들을 배치할지 그리는 도화지
    checkbox = gr.Checkbox(label = "개인정보 사용에 동의하겠습니까?") # 실제로 사용자에게 보여질 체크박스 박스
    output_checkbox = gr.Textbox(label = '출력') # 사용자의 선택에 따라 결과 메시지를 보여주는 박스 
                                                 # 처음에는 아무 내용이 없고, 체크박스를 눌렀을 때 채워짐.
    checkbox.change(handle_checkbox, inputs=checkbox, outputs=output_checkbox)
    # 사용자가 체크박스를 바꿀 때(change):handle_checkbox 함수가 실행.
        ## checkbox:내가 만든 체크박스 UI 요소
        ## .change : "변경(change) 이벤트"를 감지하겠다는 의미(사용자가 체크박스를 체크하거나 해제할 때를 말함)

    # inputs=checkbox: 체크박스의 상태가 함수의 selected에 자동으로 전달됨.
      ## 사용자가 체크를 하면 selected = True가 되고, 체크를 해제하면 selected = False가 됨.

    # outputs=output_checkbox: 함수의 결과가 이 텍스트박스에 표시됨.
    # 체크박스가 스위치고, 연결된 전구가 텍스트박스!.
    # 스위치를 켜면 → 전구가 반응해서 불이 들어오거나 꺼지게됨.
    demo.launch()

    ## 전체요약
    # 1) 사용자가 체크박스를 클릭함 (check 또는 uncheck)
    # 2) Gradio가 "어! 체크박스 상태가 바뀌었네!" 하고 감지함 → .change 작동
    # 3) handle_checkbox() 함수를 실행하면서 현재 체크된 상태 (True 또는 False)를 전달
    # 4) 함수가 결과 문자열을 리턴
    # 5) 그 문자열이 output_checkbox에 자동으로 표시됨
   
