def get_permutations(sequence):
    # Trường hợp cơ sở (Base case): Nếu chuỗi chỉ có 1 ký tự hoặc rỗng
    if len(sequence) <= 1:
        return [sequence]

    # Tách ký tự đầu tiên và các ký tự còn lại
    first_char = sequence[0]
    rest_chars = sequence[1:]

    # Đệ quy lấy tất cả hoán vị của phần còn lại
    perms_of_rest = get_permutations(rest_chars)

    result = []

    # Trường hợp đệ quy (Recursive case):
    # Chèn ký tự đầu tiên vào mọi vị trí có thể của từng hoán vị phần còn lại
    for perm in perms_of_rest:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + first_char + perm[i:]
            
            # Tránh trùng lặp nếu chuỗi đầu vào có các ký tự giống nhau
            if new_perm not in result:
                result.append(new_perm)

    return result


# --- THỬ NGHIỆM CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    test_str = "abc"
    permutations = get_permutations(test_str)
    print(f"Các hoán vị của '{test_str}':")
    print(permutations)