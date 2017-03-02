import time
start=time.time()

result = set()

pan_factors = set()
for a in range(1, 9999):
  stra = str(a)
  if len(stra) != len(set(stra)): continue
  if "0" in stra: continue
  pan_factors.add(a)

for a in pan_factors:
  for b in pan_factors:
    productstr = str(a)+str(b)+str(a*b)
    if "0" in productstr: continue
    if len(set(productstr)) != 9 or len(productstr) != 9: continue

    print(a, b, a*b)
    result.add(a*b)

print(sum(result))

end=time.time()
print(str(round(end-start,3))+" seconds")