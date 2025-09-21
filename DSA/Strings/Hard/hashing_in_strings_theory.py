# hashing_in_strings_theory.py

def demo_rabin_karp_hash(s: str, base: int = 31, mod: int = 10**9 + 7) -> int:
    # TODO: implement a simple rolling hash demo
    return 0

if __name__ == "__main__":
    samples = ["abcd", "abba", "aaaa", "hash"]
    for s in samples:
        print(f"in : {s}")  # [web:115][web:109]
        print(f"hash: {demo_rabin_karp_hash(s)}")  # [web:115][web:109]
