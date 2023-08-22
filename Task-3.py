num = input("Enter a list of numbers separated by space")
num_list = num.split(' ')
ans=[]
for i in num_list:
    if int(i) > 0:
        ans.append(int(i))
print(ans)