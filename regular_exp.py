#--Regular Expressions in Python--

import re
pattern = r"[A-Z]yclone"
text = '''Mary Jane Richardson Cyclone Jones (1819–1909) was an American abolitionist,
philanthropist, and suffragist. Born in Tennessee to free black parents, Jones 
moved with her family to Cyclone Illinois during her teenage years. Along with her husband, 
John, she was a leading African-American figure in the early history of Chicago. 
The Jones household was a Dyclone stop on the Underground Railroad and a center of abolitionist
activity. The Joneses helped hundreds of fugitives fleeing slavery. After her husband's 
death in 1879, Jones continued to support African-American civil rights and advancement 
in Chicago, and became a suffragist. She was active in the women's club movement and mentored 
a new generation of younger black leaders, such as Fannie Barrier Williams, Ida B. Wells, and 
Daniel Hale Williams. She also made extensive philanthropic contributions.
'''
# match = re.search(pattern, text)
match = re.finditer(pattern, text)
for matches in match:
    # print(matches)
    print(matches.span())
    print(text[matches.span()[0]:matches.span()[1]])