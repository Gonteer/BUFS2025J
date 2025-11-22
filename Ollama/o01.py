import ollama

# --- 설정 ---
# 1. 사용할 모델 이름 (Ollama에 설치된 모델)
MODEL_NAME = "gemma3:1b" 

# 2. 모델에게 보낼 질문
USER_QUESTION = "점성술은(는) 무엇인가요? 파이썬 코드를 제시하며 간결하게 답변해 주세요."

# --- 실행 ---
try:
    # Ollama 서버에 요청을 보냅니다.
    response = ollama.generate(
        model=MODEL_NAME, 
        prompt=USER_QUESTION
    )
    
    # 응답 텍스트를 출력합니다.
    print("--- [사용자 질문] ---")
    print(USER_QUESTION)
    print("\n--- [모델 응답] ---")
    # 'response' 키에 모델의 최종 응답 텍스트가 담겨 있습니다.
    print(response['response'])
    
except Exception as e:
    print(f"\n[오류 발생]: Ollama 서버 연결 또는 모델 실행 문제.")
    print(f"오류 내용: {e}")
    print(f"**참고:** Ollama 서버가 실행 중인지 (터미널에 'ollama run {MODEL_NAME}' 입력 후 확인), '{MODEL_NAME}' 모델이 설치되었는지 확인하세요.")
