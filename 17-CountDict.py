s = input("Enter a string: ")

ch_cnt = {}

for char in s:
    if char in ch_cnt:
        ch_cnt[char] += 1
    else:
        ch_cnt[char] = 1

for char, count in ch_cnt.items():
    print(f"'{char}': {count}")
