text = input()
done = set()
unli = ["a","e","i","u","o"]
l=0
res= text
option =False
t=1
ans =0 
while l<len(text):
	if t>=3 or option:
		option =True
		if text[l] not in unli and text[l] not in done and l!= len(text)-1:
			done.add(text[l])
			res = res[:l+1+ans]+"_"+res[l+1+ans:]
			option = False
			t=0
			ans+=1
	l+=1
	t+=1
print(res)