# Accept amount
amount = int(input("Enter Amount: "))

# 500 notes
notes = amount // 500
print("500 x", notes)
amount = amount % 500

# 200 notes
notes = amount // 200
print("200 x", notes)
amount = amount % 200

# 100 notes
notes = amount // 100
print("100 x", notes)
amount = amount % 100

# 50 notes
notes = amount // 50
print("50 x", notes)
amount = amount % 50

# 20 notes
notes = amount // 20
print("20 x", notes)
amount = amount % 20

# 10 notes
notes = amount // 10
print("10 x", notes)

