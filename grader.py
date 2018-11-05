import csv
import sys

header=[]
header1=[]
data=[]
data1=[]
counter = 0
problems=["s1", "s7", "s9", "s12", "s13", "s14", "s15", "s16", "s17", "e3", "s19", "s20", "s21", "e9", "e10", "s27", "s28", "s29", "e14", "s31", "s32", "s33", "s34", "s35"]
problems1=["s2", "s8", "s15", "s16", "s17", "s18", "e3"]
final, acc={}, {}

def parse(file):
    data=[]
    with open(file, 'rb') as f:
        reader = csv.reader(f)
        header = next(reader)[2:]
        for row in reader:
            # row is a list of strings
            # use string.join to put them together
            data.append(row[1:])
    return data, header


data, header = parse(sys.argv[1])
data1, header1, = parse(sys.argv[2])

def grade(data, header, problems):
    final={}
    toGrade=[]
    for i, v in enumerate(header):
        if i < 1:
            continue
        else:
            if v.split('-')[0] in problems:
                toGrade.append(i)

    global acc
    for v in data:
        fullName = v[1] + v[0]
        attempted = sum((1 for prob in toGrade if v[prob] in ('Y', 'N')))
        if attempted == len(toGrade):
            if fullName not in acc:
                acc[fullName] = 0
            if(acc[fullName] == -1):
                continue
            acc[fullName] += sum((1 for prob in toGrade if v[prob] in('Y', )))
        else:
            acc[fullName] = -1

def final_grade():
    #[1, 2, 3]
    final={}
    for k, v in acc.items():
        if(v > 0):
            percentage=float(v)/((len(problems)+len(problems1)))
            if percentage > 0.6:
                final[k] = 4
            elif percentage > 0.4:
                final[k] = 3
            else:
                final[k] = 2
        else:
            final[k] = 1

    return final
    
grade(data, header, problems)
grade(data1, header1, problems1)
final = final_grade()
     
for k, v in final.items():
    print k + ": " + str(v)
