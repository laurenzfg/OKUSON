#!/usr/bin/env python

import sys,os,string

people = []
i = sys.stdin
while 1:
    line = i.readline()
    if not(line): break
    line = line.strip()
    if not(line) or line[0] == '#': continue
    p = line.split(':')
    people.append(p)
i.close()

TeXHeader = r'''\documentclass[11pt,german]{article}

\parindent0pt
\pagestyle{empty}
\usepackage{babel}
\usepackage{times}
\usepackage[a4paper,textwidth=7.3in,textheight=10.5in]{geometry}
\usepackage[latin1]{inputenc}
\usepackage{longtable}

\begin{document}
\sloppy
'''

TeXFooter = r'''
\end{document}'''

TeXGroupStart = r'''\textbf{\large Gruppennummer: %s}

\begin{longtable}{|l|p{3.4cm}|c|c|c|c|c|c|c|c|c|c|c|c|c||c|}
\hline
Matnr. & Name, Vorname & B0 & B1 & B2 & B3 & B4 & B5 & B6 &
 B7 & B8 & B9 & B10 & B11 & B12 & $\displaystyle \sum$ \endhead
\hline
\hline'''

TeXGroupEnd = r'''
\end{longtable}
\newpage
'''

TeXPerson = r''' %s & %s &&&&&&&&&&&&&&\\ \hline'''

print TeXHeader

o = sys.stdout
lastgroup = -1
opened = 0
for i in range(len(people)):
    p = people[i]
    if p[17] != lastgroup:
        if opened: print TeXGroupEnd
        lastgroup = p[17]
        print TeXGroupStart % (lastgroup)
        opened = 1
    print TeXPerson % (p[0],p[1]+', '+p[2])
print TeXGroupEnd
print TeXFooter

