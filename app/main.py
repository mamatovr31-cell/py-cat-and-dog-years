def calculator_human(age, divisor):
    if age < 0:
        raise ValueError("age must be non-negative")
    if not isinstance(age, int):
        raise TypeError("age must be int")

    if age < 15:
        return 0
    age_animal = int(age)
    age_human = 0
    if age_animal >= 15:
        age_animal -= 15
        age_human += 1
    if age_animal >= 9:
        age_animal -= 9
        age_human += 1
        age_human += age_animal // divisor
    return age_human


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat = calculator_human(cat_age, 4)
    dog = calculator_human(dog_age, 5)
    return [cat, dog]
