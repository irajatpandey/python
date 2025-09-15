def is_rotation(s1: str, s2: str) -> bool:
    """
    Checks if s2 is a rotation of s1.
    """
    pass

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    s3 = "hello"
    print(f"Is '{s2}' a rotation of '{s1}'? {is_rotation(s1, s2)}")
    print(f"Is '{s3}' a rotation of '{s1}'? {is_rotation(s1, s3)}")