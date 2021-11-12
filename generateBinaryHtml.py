def generateCSS(nmbrElements, width): 

    css = ".binary patterns {\n"
    css += "\tposition: absolute;\n"
    css += f"\twidth:{width}\n"
    css += "\tdisplay: grid;\n"
    css += f"\tgrid-template-columns: repeat({nmbrElements},1fr)\n"
    css += "}\n"
    css += "\n\n"
    css += ".zero-bit {\n"
    css += "\twidth: 30px\n"
    css += "\theight: 30px\n"
    css += "\tborder-radius: 50%\n"
    css += "\tbackground-color: black\n"
    css += "}\n"

    return css


string = "00011100101100011000101"

html = "<div class='binary-pattern'>\n"


for char in string:

    if(char == '0'):
        html += "\t<div class='zero-bit'></div>\n"
    elif(char == '1'):
        html += "\t<div class='one-bit'></div>\n"


html += "</div>"

file = open('bin-pattern.txt', 'w')
file.truncate()
file.write(html)

file.write("\n\nCSS:\n\n")
file.write(generateCSS(len(string),"100%"))

file.close()


