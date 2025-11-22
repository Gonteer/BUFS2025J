import ollama

# --- 설정 ---
# 1. Ollama 서버의 IP와 포트를 지정합니다.
OLLAMA_SERVER_URL = "http://localhost:11434"

# 2. 사용할 모델 이름
MODEL_NAME = "gemma3:1b" 

# 3. 모델에게 보낼 질문
USER_QUESTION = "점성술이 무엇인가요?"

# --- 실행 ---
try:
    # Client 객체를 생성할 때 서버 주소를 명시적으로 전달합니다.
    client = ollama.Client(host=OLLAMA_SERVER_URL)
    
    # 생성된 client 객체를 사용하여 요청을 보냅니다.
    response = client.generate(
        model=MODEL_NAME, 
        prompt=USER_QUESTION
    )
    
    # 응답 텍스트를 출력합니다.
    print(f"--- [서버 주소] ---")
    print(OLLAMA_SERVER_URL)
    print("\n--- [모델 응답] ---")
    print(response['response'])
    
except Exception as e:
    print(f"\n[오류 발생]: 서버 연결 또는 모델 실행 문제.")
    print(f"오류 내용: {e}")
    print(f"**참고:** {OLLAMA_SERVER_URL} 주소에 Ollama 서버가 실행 중인지, 네트워크 방화벽이 포트 11434를 허용하는지 확인하세요.")
