import re
import os

def build_match_function(pattern):    
    def matches_rule(itext):
        find_pattern = re.compile(pattern, re.MULTILINE)
        return find_pattern.finditer(itext)
    return (matches_rule)

def rules(filename):
    with open(filename, encoding="utf-8") as pattern_file:
        for line in pattern_file:
            pattern = line
            yield build_match_function(pattern)


def main(licence_directory="Licence", rule="rule.txt",grab_licence_directory="GrabLicence"):   
    for r, d, f in os.walk(licence_directory):
        for licence_file in f:
            licence = open(os.path.join(r,licence_file), encoding="cp1250")
            licence_text = licence.read()
            licence.close()
            outfile = open(os.path.join(grab_licence_directory,licence_file), "w+", encoding="utf-8")
            for matches_rule in rules(rule):
                for match in matches_rule(licence_text):
                    tp, cnt, fr , to = match.groups()
                    cnt = int(cnt)
                    fr = int(fr)
                    to = int(to)
                    for i in range(fr,to + 1,1):
                        outfile.write("%s,%s\n" % (tp, i))
            outfile.close()

                
main()