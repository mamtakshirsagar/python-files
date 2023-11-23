import re
str="mamta is beautiful and smart and very smart"
x=re.search("smart",str)
print(x.group(0))
y=re.findall("smart",str)
print(y)
z=re.match("smart",str)
print(z)
if x:
    print("pattern found")
else:
    print("pattern not found")