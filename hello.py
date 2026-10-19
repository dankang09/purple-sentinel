def greet(name:str) -> str: # 매개 변수 타입 힌트 -> 리턴 타입 힌트
    return f"Hello, {name}! Welcome to Purple Sentinel"

if __name__ == "__main__": # 파일을 직접 실행할 때만 아래 코드 실행
    message = greet("Daniel")
    print(message)
