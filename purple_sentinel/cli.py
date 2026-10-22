import argparse

from .security_logs import count_failed_logins

# CLI 프로그램의 주요 실행 흐름 정의
def main() -> None:
    # CLI 가 사용할 옵션과 도움말을 관리하는 객체 생성
    parser = argparse.ArgumentParser(
        description="Purple Sentinel - Security Log Analyzer"
    )

    # 사용자가 입력할 --demo 옵션 등록
    parser.add_argument(
        "--demo",
        action="store_true",  # 옵션이 있으면 True, 없으면 False
        help="Run a demo with systhetic SSH logs"
    )

    args = parser.parse_args()  # 실제 PowerShell 명령어에서 전달된 인자 분석

    if args.demo:  # 사용자가 --demo 를 지정했는지 확인
        logs= [
            {"ip": "192.0.2.10", "status": "failed"},
            {"ip": "192.0.2.20", "status": "success"},
            {"ip": "192.0.2.10", "status": "failed"},
        ]

        results = count_failed_logins(logs)  # Day2에 직접 구현한 함수 재사용 (리팩토링 완료 2026.10.22)
        print("Failed login counts:", results)
    else:
        parser.print_help()  # 옵션 지정안하면 도움말 출력