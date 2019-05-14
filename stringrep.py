s=str(input())
count=0
for i in range (0,len(s)):
	if s[i]=="1" or s[i]=="0":
		count=count+0
	else:
		count=count+1
if count==0:
	print("yes")
else:
	print("no")
