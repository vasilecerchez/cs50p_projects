
file_name=input("insert file name: ").strip().lower()

diz_ex={"gif":"image/gif","jpg":"image/jpeg","jpeg":"image/jpeg",
    "png":"image/png","pdf":"application/pdf",
    "txt":"text/plain","zip":"application/zip"}

est=file_name.split(".")[-1]
if est in diz_ex.keys():
    print(diz_ex[est])
else:
    print("application/octet-stream")
    
    

# Solution 2 .............................
# string.endswith("...")
"""
file_name=input("insert file name: ").strip().lower()

if file_name.endswith('.gif'):
    print("image/gif")
elif file_name.endswith('.jpg'):
    print("image/jpeg")

"""