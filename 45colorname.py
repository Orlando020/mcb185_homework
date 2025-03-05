import sys
#python3 45colorname.py ../Code/MCB185/data/colors_extended.tsv 200 0 50
#crimson #DC143C 220,20,60
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

best_color = False
best_diff = 195075 #sum of 255^2 + 255^2 + 255^2

with open(colorfile) as fp:
    for color in fp:
        listo = color.split()
        rgb = listo[2]
        rgb_list = rgb.split(',')
        rdiff = int(rgb_list[0]) - R
        gdiff = int(rgb_list[1]) - G
        bdiff = int(rgb_list[2]) - B
        totaldiff = (rdiff**2)+(gdiff**2)+(bdiff**2)
        if totaldiff < best_diff:
            best_diff = totaldiff
            best_color = color

print(best_color)