#! C:\Program Files\Python37\python
def sort(a):
    words=a.split()
    words.sort()
    for word in words:
        print(word)
import cgi
print("content:text/html\n")
print("<html>")
print("<head><title>my sec</title>")
print("</head>")
print("</body>")


form=cgi.FieldStorage()
a=form.getvalue("first")

print('<form method="post" action="a2.py">')
print('<p>enter first:<input type="text" name="first"/></p>')

print('<input type="submit" value="submit"/>')
print('<br>')
print("</body>")
print("</html>")
sort(a)
      
      

