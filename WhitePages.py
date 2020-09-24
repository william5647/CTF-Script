tab_ascii_chars = []
final_binary = ""

#Reading the file
with open('whitepages.txt','r') as fileobj:
    for line in fileobj:
       for ch in line:
           #Getting ascii values of the char
           tab_ascii_chars.append(ord(ch))

i=0
while i < len(tab_ascii_chars):
    if tab_ascii_chars[i] == 226 and tab_ascii_chars[i+1] == 128 and tab_ascii_chars[i+2] == 131: # if tab
        final_binary += "0"
        i += 3
    elif tab_ascii_chars[i] == 32: #if space
        final_binary += "1"
        i += 1
    else:
        print i
        print tab_ascii_chars[i]
        print tab_ascii_chars[i+1]
        print tab_ascii_chars[i+2]
        raise Error("oops :/")
        
#Outputs the final result
print final_binary
