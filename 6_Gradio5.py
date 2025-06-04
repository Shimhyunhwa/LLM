import gradio as gr

def add(num1, num2): 
    return num1 + num2 

interface = gr.Interface(          
    fn=add, 
    inputs = ['number', 'number'], 
    outputs = 'number',
    title = '계산기', 
    description = '숫자 두개를 입력하세요',
    flagging_mode ="never" # flag를 하지않음
)

## ※ Flag 버튼
## 기본적으로 생성된 인터페이스에서 
## 사용자가 앱의 입력이나 출력을 플래그(flagging)할 수 있도록 제공되는 기능입니다. 
## 플래그 버튼을 누르면 해당 입력과 출력이 기록되어 
## 문제 상황이나 유용한 사례를 저장하거나 분석하는 데 활용됩니다. 
## Flag 버튼을 원하지 않는 경우 flagging_options를 비활성화하거나 설정을 변경하여 제거할 수 있습니다. 
interface.launch()