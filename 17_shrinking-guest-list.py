guests = ["jack dorsey", "jordan peterson", "kobe bryant"]
print(guests[0].title() + ", Im honoured to invite you to dinner.")
print(guests[1].title() + ", Im honoured to invite you to dinner.")
print(guests[2].title() + ", Im honoured to invite you to dinner.")

print("\nLuckily I have found a bigger dinner table, so there is room to invite a few more guests.\n")

guests.insert(0, "jay z")
guests.insert(2, "david goggins")
guests.append("muhammad ali")
print(guests[0].title() + ", Im honoured to invite you to dinner.")
print(guests[1].title() + ", Im honoured to invite you to dinner.")
print(guests[2].title() + ", Im honoured to invite you to dinner.")
print(guests[3].title() + ", Im honoured to invite you to dinner.")
print(guests[4].title() + ", Im honoured to invite you to dinner.")
print(guests[5].title() + ", Im honoured to invite you to dinner.")

print("\nUnfortunately the new dinner table won't arrive in time for the dinner, and there will only be space for two people.\n")

print(guests.pop(0).title() + ", I'm very sorry to have to withdraw the dinner invitation due to unforseen circumstances.")
print(guests.pop().title() + ", I'm very sorry to have to withdraw the dinner invitation due to unforseen circumstances.")
print(guests.pop(0).title() + ", I'm very sorry to have to withdraw the dinner invitation due to unforseen circumstances.")
print(guests.pop().title() + ", I'm very sorry to have to withdraw the dinner invitation due to unforseen circumstances.")

print(guests[0].title() + ", I'm pleased to say you made the cut.")
print(guests[1].title() + ", I'm pleased to say you made the cut.")

del guests[0]
del guests[0]
print(guests)