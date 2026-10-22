# Pytest - Edge Case Test
from purple_sentinel.security_logs import count_failed_logins
import pytest


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

# Test 5: status field 누락 시 명확한 오류 발생
def test_missing_status_raises_value_error() -> None:
    logs = [
        {"ip": "192.0.2.10"}
    ]

    # 이 구간에서 ValueError 가 발생하는지 검증한다.
    with pytest.raises(
        ValueError,
        match="Missing required field: status"
    ):
        count_failed_logins(logs)

# Test 6: IP field 누락 시 명확한 오류 발생
def test_missing_ip_raises_value_error() -> None:
    logs = [
        {"status": "failed"}
    ]

    with pytest.raises(
        ValueError,
        match = "Missing required field: ip"
    ):
        count_failed_logins(logs)