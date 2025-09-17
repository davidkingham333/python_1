data1 = bytes([0b10101010, 0b11001100, 0b11110000])
data2 = bytes([0b10101010, 0b11001100, 0b11110000])

def binary_to_hex(data):
    return data.hex()

# Funkce pro provedení XOR operace mezi dvìma binárními daty.
def xor_binary_data(data1, data2):
    return bytes(a ^ b for a,b in zip(data1, data2))

hex_data1 = binary_to_hex(data1)
hex_data2 = binary_to_hex(data2)

print(f"{hex_data1}")
print("f{hex_data2}")

# Provést XOR operaci
result_data = xor_binary_data(data1, data2)

hex_result = binary_to_hex(result_data)

print(f"{hex_result}")
