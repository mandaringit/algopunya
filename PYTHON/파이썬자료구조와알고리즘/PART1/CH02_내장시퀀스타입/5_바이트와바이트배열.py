blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

print(the_bytes[1])

the_byte_array[1] = 127
print(the_byte_array)

# 비트와 비트 연산자
print(1 << 2)

x = 6
print(x & (x - 1))
