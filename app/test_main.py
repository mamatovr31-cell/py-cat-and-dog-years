from app.main import get_human_age
import pytest

@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (
            0,
            7,
            [0, 0]
        ),
        (
            0,
            14,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            23,
            23,
            [1, 1]
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            27,
            27,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        ),
    ]
)
def test_correct_count(
        cat_age,
        dog_age,
        expected_result
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result

def test_negative_age() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)
    with pytest.raises(ValueError):
        get_human_age(1, -5)

def test_another_age() -> None:
    with pytest.raises(TypeError):
        get_human_age(1, 5.7)
    with pytest.raises(TypeError):
        get_human_age(1.7, 5)