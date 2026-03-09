from app.main import get_human_age


def test_correct_count_less_fifteen_age() -> None:
    assert get_human_age(0, 7) == [0, 0]
    assert get_human_age(0, 14) == [0, 0]

def test_correct_count_first_fifteen_age() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_correct_count_next_nine_age() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_correct_count_next_four_age() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(130, 88) == [28, 14]