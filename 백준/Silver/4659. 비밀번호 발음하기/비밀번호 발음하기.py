def is_acceptable(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    has_vowel = False
    vowel_count = 0
    consonant_count = 0

    for i, ch in enumerate(word):
        # 모음 포함 체크
        if ch in vowels:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        # 모음 또는 자음 3개 연속 금지
        if vowel_count == 3 or consonant_count == 3:
            return False

        # 같은 글자 연속 두 번 금지 (단, 'ee', 'oo' 제외)
        if i > 0:
            if ch == word[i - 1] and ch not in ('e', 'o'):
                return False

    # 최소 한 개 이상의 모음 포함 필수
    return has_vowel


while True:
    pw = input()
    if pw == "end":
        break

    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
