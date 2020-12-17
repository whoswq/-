f = open("实验数据.txt")
lines = f.readlines()
f.close()

filename = "latex_input.txt"

with open(filename, 'w') as w:
    for i in range(28):
        line1 = lines[i].split()
        line2 = lines[i + 28].split()
        str = ""
        str = str + line1[0] + '0 & '
        str += line1[1].ljust(7, '0') + ' & '
        t = '%.4f' % float(line1[2])
        str += t + ' & '
        str = str + line2[0] + '0 & '
        str += line2[1].ljust(7, '0') + ' & '
        t = '%.4f' % float(line2[2])
        str += t + r' \\'
        w.write(str + "\n")
