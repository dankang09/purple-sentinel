from .cli import main

# -m 으로 실행 시 해당 패키지의 __main__.py를 프로그램의 Entry Point로 사용함
if __name__ == "__main__":
    main() # 실제 CLI 함수 호출