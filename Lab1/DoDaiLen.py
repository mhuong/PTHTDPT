ibrow = "🤨"
print(len(ibrow))

print(ibrow.encode("utf-8"))

print(len(ibrow.encode("utf-8")))


# Calling list() on a bytes object gives you
# the decimal value for each byte
print(list(b'\xf0\x9f\xa4\xa8'))