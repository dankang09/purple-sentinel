from hello import greet

def test_greet() -> None:
    # 실제 실행 결과
    actual = greet("Daniel")

    # 예상 결과
    expected = "Hello, Daniel! Welcome to Purple Sentinel"

    assert actual == expected # 두 값이 같은지 검증