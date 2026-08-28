def ktra(sequence):
    if len(sequence) <= 1:
        return [sequence]
    
    ky_tu_dau = sequence[0]
    ky_tu_con_lai = sequence[1:]

    de_quy_phan_con_lai = ktra(ky_tu_con_lai)

    result = []

    for ky_tu in de_quy_phan_con_lai:
        for i in range(len(ky_tu) + 1):
            new_ky_tu = ky_tu[:i] + ky_tu_dau + ky_tu[i:]

        if new_ky_tu not in result:
            result.append(new_ky_tu)

    return result

if __name__ == "__main__": 
    test_str = "abc"
    ky_tu = ktra(test_str)
    print(f"Các hoán vị của '{test_str}':")
    print(ky_tu)