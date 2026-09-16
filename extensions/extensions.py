"""
In a file called extensions.py, implement a program that prompts 
the user for the name of a file and then outputs that file’s media 
type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default."""

extension = input("File name: ")
extension = extension.lower().strip()
if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg"):
    print("image/jpeg")
elif extension.endswith(".jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/plain")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

