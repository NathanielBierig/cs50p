phile = input("File Name: ").strip().split(".")[-1].lower()
if phile in ["gif","jpg","jpeg", "png"] :
    print("image/"+phile)
elif phile == "txt":
     print("plain/"+phile)
elif phile in ["pdf", "zip"]:
     print("application/"+phile)
else:
    print("application/octet-stream")