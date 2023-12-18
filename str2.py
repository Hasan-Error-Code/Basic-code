country = "Bangladesh"
f = country.find("Ban")
print(f)

print("-" * 50)

coun = "North Corea"
count = coun.replace("North", "South")
print(count)
print(coun)
print("-" * 50)

text = "hello"
text = text.replace("h", "H")
print(text)
print("-" * 50)

st = "  Hey there this  is Hasan  "
mod = st.lstrip()
print(mod)
mod2 = st.rstrip()
print(mod2)
mod3 = st.strip()
print(mod3)
print("-" * 50)

s = "bangladesh"
up = s.upper()
print(up)
lp = up.lower()
print(lp)
ca = lp.capitalize()
print(ca)
print('-' * 50)
print("-" * 20, "split", "-" * 20)
sp = "Hey   there  this is   Hasan, I am    from Bangladesh"
spr = sp.split()
print(spr)
for i in spr:
    print(i)