name = "inject.html"
file = open(name, "r")
inject = file.read(); file.close()

name = "index.html"
file = open(name, "r")
string = file.read(); file.close()
before = string
string = string.replace("background-color:#222", "background-color:#000000")
string = string.replace("<!-- Add content below the cart here -->", "<!-- Camden Start -->" + "\n\n" + inject + "\n\n" + "<!-- Camden End -->")
if string == before:
    found = False
    replacer = ""
    lines = string.splitlines()
    for line in lines:
        if "<!-- Camden Start -->" in line: found = True
        if found:
            replacer += line + "\n"
            if "<!-- Camden End -->" in line:
                found = False
                break
    string = string.replace(replacer, "<!-- Camden Start -->" + "\n\n" + inject + "\n\n" + "<!-- Camden End -->\n")

file = open(name, "w")
file.write(string)
