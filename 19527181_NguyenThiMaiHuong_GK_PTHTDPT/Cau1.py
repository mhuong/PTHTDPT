#Chạy đoạn code sau và giải thíc từng dòng code
str_original = "UTF-8 PYTHON PROGRAMMING ENCODING AND DECODING"
bytes_encoded = str_original.encode(encoding="utf-8")
print(type(bytes_encoded))
str_decoded=bytes_encoded.decode()
print(type(str_decoded))

print(type(bytes_encoded))
print(type(str_decoded))
print(bytes_encoded==str_decoded)

