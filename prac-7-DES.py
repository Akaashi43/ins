# DES Algorithm

def permute(k, arr):
    return ''.join(k[i - 1] for i in arr)

def hex2bin(s):
    return bin(int(s, 16))[2:].zfill(64)

def bin2hex(s):
    return hex(int(s, 2))[2:].upper().zfill(16)

def left_shift(k, shifts):
    return k[shifts:] + k[:shifts]

def key_schedule(key):
    key = hex2bin(key)
    key_permuted = permute(key, [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 28, 20, 12, 4
    ])
    
    left = key_permuted[:28]
    right = key_permuted[28:]
    
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    round_keys = []
    
    for shift in shifts:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined = left + right
        
        round_key = permute(combined, [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ])
        
        round_keys.append(round_key)
    
    return round_keys

def sbox_lookup(sbox, row, col):
    return sbox[row][col]

def feistel_function(right, round_key):
    expansion_permutation = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    
    sboxes = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # ... (complete all S-boxes)
    ]

    right_expanded = permute(right, expansion_permutation)
    xor_result = ''.join(str(int(b) ^ int(k)) for b, k in zip(right_expanded, round_key))
    
    sbox_output = ""
    for i in range(8):
        row = int(xor_result[i * 6] + xor_result[i * 6 + 5], 2)
        col = int(xor_result[i * 6 + 1:i * 6 + 5], 2)
        sbox_value = sbox_lookup(sboxes[i], row, col)
        sbox_output += bin(sbox_value)[2:].zfill(4)

    return permute(sbox_output, [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25
    ])

def des_encrypt(plaintext, key):
    round_keys = key_schedule(key)
    
    plaintext = hex2bin(plaintext)
    initial_permutation = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    
    plaintext = permute(plaintext, initial_permutation)
    left, right = plaintext[:32], plaintext[32:]

    for round_key in round_keys:
        temp = right
        right = ''.join(str(int(left[i]) ^ int(feistel_function(temp, round_key)[i])) for i in range(32))
        left = temp

    combined = left + right
    final_permutation = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    return bin2hex(permute(combined, final_permutation))

def des_decrypt(ciphertext, key):
    round_keys = key_schedule(key)[::-1]
    return des_encrypt(ciphertext, key)

# Example usage
key = "133457799BBCDFF1"  # 64-bit key (16 hex digits)
plaintext = "0123456789ABCDEF"  # 64-bit plaintext (16 hex digits)

ciphertext = des_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = des_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)

