from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_hash = defaultdict(int) 
    for c in s:
        s_hash[c] += 1
    for c in t:
        if c in s_hash and s_hash[c] != 0:
            s_hash[c] -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("racecar", "carrace"))
    print(is_anagram("jar", "jam"))
