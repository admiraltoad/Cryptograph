"""
    Cryptograph
"""
import os, sys
import webbrowser

def encrypt_html_table_row(text):
    if len(text) > 12:
        raise Exception("Entry too long '{0}'".format(text))

    table_row1 = "  <tr>\n"
    table_row2 = "  <tr>\n"
    for letter in text:        
        table_row1 += "    <td style=\"width:75px;height:75px;\">"
        table_row2 += "    <td style=\"width:75px;height:25px;"
        if letter.isalpha(): 
            table_row1 += "<img src=\".\keys\{0}.jpg\">".format(letter)
            table_row2 += "border-bottom:1px solid;"
        table_row1 += "</td>\n"          
        table_row2 += "\"></td>\n"
    table_row1 += "  </tr>\n"
    table_row2 += "  </tr>\n"

    return table_row1 + table_row2

def main():
    text = input("Text to Encrypt: ")
    html = "<html>\n"
    html += "<body>\n"

    html_table = "<table>\n"

    current_line = ""
    for word in text.lower().split():
        if len(word) > 12:
            raise Exception("Entry too long '{0}'".format(word))

        newline = False
        if word.endswith("."):
            word = word[:1]
            newline = True        

        if (len(current_line) + len(word)) > 12:
            html_table += encrypt_html_table_row(current_line.strip())
            if newline:
                html_table += "  <tr><td colspan=\"12\" style=\"width:900px;height:25px;\">&nbsp;</td></tr>\n"
            current_line = "" ## reset        
        current_line += word + " "

    if len(current_line) > 0:
        html_table += encrypt_html_table_row(current_line.strip())

    html_table += "</table>\n"    
    
    html += html_table
    html += "</body>\n"
    html += "</html>" 
        
    outfilename = os.path.join(os.path.dirname(__file__), "encrypted.html")
    if os.path.isfile(outfilename):
        os.remove(outfilename)

    outfile = open(outfilename, "w")
    outfile.write(html)
    outfile.close()

    webbrowser.open("file://" + os.path.realpath(outfilename))
    
    return 0

if __name__ == "__main__":   				 
    rcode = main()
    sys.exit(rcode)