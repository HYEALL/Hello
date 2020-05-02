a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
a = a.replace(":",",")
b = a.split("  ")
c = " ".join(b)
c = c.replace("naMe","name")
c = c.replace("my","My")
print(c)

#name 소문자 my My