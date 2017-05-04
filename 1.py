import re
s="1,NAME1,email123@gmail.com,7893225566,\nNAME2,2,7893445567email456@yahoo.co.in,7893225577,3,NAME3,email567@rediffmail.com"
print(s)
print(re.findall("[0-9]{10}",s))
print(re.findall("[a-z][0-9]",s,re.I))
print(re.findall("[a-zA-Z][0-9]",s))
print(re.findall("[0-9]{2}",s))
print(re.findall("[0-9]{2,5}",s))
print(re.findall("[0-9]{1,5}",s))
print(re.findall("[0-9]*",s))
print(re.findall("[0-9]+",s))
print(re.findall("[0-9]?",s))
print(re.findall(".",s))
print(re.findall(".",s,re.DOTALL))
print(re.findall("\.",s))

import re
s="1,NAME1,email123@gmail.com,7893225566,\nNAME2,2,7893445567email456@yahoo.co.in,7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
print(re.findall("[a-z][0-9]+@[a-z]+\.[com]{2,3}\.*[in]*",s))


import re
s="1,NAME1,email123@gmail.com,7893225566,\nNAME2,2,7893445567email456@yahoo.co.in,7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
#print(re.match("[a-z][0-9]+@[a-z]+\.[com]{2,3}\.*[in]*",s))
print(re.match("[0-9]",s))

import re
s="1,NAME1,email123@gmail.com,7893225566,\nNAME2,2,7893445567email456@yahoo.co.in,7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
print(re.search("[a-z][0-9]+@[a-z]+\.[com]{2,3}\.*[in]*",s))



import re
s="1,NAME1,email123@gmail.com,\n7893225566,NAME2,2,\n7893445567email456@yahoo.co.in,\n7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
print(re.findall("^[0-9]{10}",s,re.M))


import re
s="1,NAME1,email123@gmail.com,\n7893225566,NAME2,2,\n7893445567email456@yahoo.co.in,\n7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
print(re.findall(".com",s))


import re
s="1,NAME1,email123@gmail.com,\n7893225566,NAME2,2,\n7893445567email456@yahoo.co.in,\n7893225577,3,NAME3,email567@rediffmail.com"
#print(s)
print(re.findall(".com$",s))
