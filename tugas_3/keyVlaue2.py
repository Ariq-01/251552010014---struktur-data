playe = {'albert': 'id = 8923232', 'savage': 23424}


email = playe.get("email", "Email belum tersedia")
print(email)

playe.setdefault("email", "player@eml.com")

playe.update({"savage": 30000, "role": "Marksman"})

savage_val = playe.pop("savage")

print(playe.keys())
print(playe.values())

playe_copy = playe.copy()

print(playe)
print(playe_copy)
