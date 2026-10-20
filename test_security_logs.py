# Pytest - Edge Case Test
from security_logs import count_failed_logins


# Test1: 동일 IP의 실패 이벤트만 존재할 경우
def test_count_failed_logins() -> None:
    logs = [
        {"ip":"192.0.2.10", "status": "failed"},
        {"ip":"192.0.2.10", "status": "failed"},
        {"ip":"192.0.2.10", "status": "failed"},
    ]

    actual = count_failed_logins(logs)
    expected = {"192.0.2.10": 3}
    
    assert actual == expected


# Test2: 성공 이벤트만 존재할 경우 (Negative Test Case)
def test_success_only() -> None:
    logs = [
        {"ip": "192.0.2.20", "status": "success"},
    ]

    actual = count_failed_logins(logs)
    expected = {}

    assert actual == expected

# Test3: Edge Case - Empty Event Input
def test_empty_logs() -> None:
    logs = []
    
    actual = count_failed_logins(logs)
    expected = {}

    assert actual == expected


# Test4: 여러 Source IP의 실패 횟수 집계
def test_multiple_ips() -> None:
    logs = [
        {"ip": "192.0.2.10", "status": "failed"},
        {"ip": "192.0.2.20", "status": "failed"},
        {"ip": "192.0.2.10", "status": "failed"},
        {"ip": "192.0.2.30", "status": "success"},
    ]

    actual = count_failed_logins(logs)
    expected = {"192.0.2.10": 2, "192.0.2.20": 1}

    assert actual == expected