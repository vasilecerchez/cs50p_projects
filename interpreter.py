

info=input(" insert data: ").strip()
# 3 + 6
info_list=info.split()
if len(info_list)>3:
    # problem with input
    pass
x=float(info_list[0])
y=info_list[1]
z=float(info_list[2])

if y=="+":
    print(x+z)
elif y=="-":
    print(x-z)
elif y=="*":
    print(x*z)
elif y=="/":
    print(round(x/z,1))
else:
    #print("insert a valid operation")
    pass



