# Synthetic SSH authentication logs

# IP별 로그인 실패 횟수 집계 구현하기
def count_failed_logins(
    events: list[dict[str, str]]
) -> dict[str, int]:

    counts: dict[str, int] = {}

    for event in events:
        # status가 failed가 아니면 건너띄기 (Guard Clause)
        if event["status"] != "failed":
            continue

        # 현재 IP의 실패 횟수를 1 증가시킴
        ip = event["ip"]
        # Dictionary Counter Pattern
        counts[ip] = counts.get(ip, 0) + 1
    
    return counts


if __name__ == "__main__":
    # 예제 데이터는 직접 실행할 때만 생성한다.
    # 각 이벤트를 Key-Value 형태의 dict로 표현
    logs = [
        {"ip": "192.0.2.10", "status": "failed"},
        {"ip": "192.0.2.20", "status": "success"},
        {"ip": "192.0.2.10", "status": "failed"},
        {"ip": "192.0.2.30", "status": "failed"},
        {"ip": "192.0.2.10", "status": "failed"},
    ]

    # 문자열 IP들을 저장할 집합 생성 (타입 힌트)
    unique_ips: set[str] = set()

    # logs 에서 하나씩 꺼내서 집합에 추가(중복 제거)
    for event in logs:
        unique_ips.add(event["ip"])
        #print(unique_ips)

    print("Total events:", len(logs))
    print("Unique source IPs", sorted(unique_ips))
    print("Failed login counts:", count_failed_logins(logs))