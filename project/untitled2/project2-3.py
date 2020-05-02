a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
a = a.replace(":",",")
b = a.split("  ")
c = " ".join(b)
c = c.replace("naMe","name")
c = c.replace("my","My")
c = c.replace("!!!!!!","")
print(c)

#뒷자리 1자리만 남기고 지우기