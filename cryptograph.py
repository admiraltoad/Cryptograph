"""
    Cryptograph
"""
import os, sys
import webbrowser

def encrypt_html_table_row(text):
    if len(text) > 12:
        raise Exception("Entry too long '{0}'".format(text))

    table_row = "  </tr>\n"
    for letter in text:        
        table_row += "    <td style=\"width:75px;height:75px;\">"
        if letter.isalpha(): 
            table_row += "<img src=\".\keys\{0}.jpg\">".format(letter)
        table_row += "</td>\n".format(letter)                    
    table_row += "  <tr>\n"

    return table_row

def main():
    text = input("Text to Encrypt: ")
    html = "<html>\n"
    html += "<body>\n"

    html_table = "<table>\n"

    current_line = ""
    for word in text.lower().split():
        if len(word) > 12:
            raise Exception("Entry too long '{0}'".format(word))

        if (len(current_line) + len(word)) > 12:
            html_table += encrypt_html_table_row(current_line.strip())
            current_line = "" ## reset        
        current_line += word + " "

    if len(current_line) > 0:
        html_table += encrypt_html_table_row(current_line)

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