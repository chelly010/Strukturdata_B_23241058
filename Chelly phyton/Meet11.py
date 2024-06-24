# For Loop (Perulangan)
print("For Loop:")
nama = ["adam", "aran", "chelly"]
for nama in nama:
    print(nama)

# While Loop (Perulangan memiliki kondisi agar bisa berjalan terus)
print("While Loop:")
n = 5  # jumlah bintang yang ingin diulang

for i in range(n):
    print("1" * (i + 1))

# Nested Loop (Perulangan yang tedapat perulangan lagi)
print("Nested Loop:")
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})")

# Loop with Break (Perulangan yang dapat di hentian secara paksa sesuai statement yang di inginkan)
print("Loop with Break:")
for x in range(1, 5):
    if x == 5:
        break
    print(x)

# Loop with Continue
print("Loop with Continue:")
for x in range(1, 5):
    if x == 5:
        continue
    print(x)

# Loop with Else
print("Loop with Else:")
for x in range(3, 6):
    print(x)
else:
    print("Loop finished")