import string as st

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# string = []
# for i in text: 
#     if i.islower() : 
#         char = st.ascii_lowercase[(st.ascii_lowercase.index(i)+ 2)]
#     elif i.isupper(): 
#         char = st.ascii_uppercase[(st.ascii_uppercase.index(i) + 2)]
#     else: 
#         char = i 
#     string.append(char) 

# print(string)

new_text = ""
for letter in text:
    if letter not in st.ascii_letters:
        new_text += letter
    else:
        index = st.ascii_letters.find(letter) + 2 
        if index > 25:
            index -= 26

        new_text += st.ascii_letters[index]

print(new_text)

        
