import png
import re
img = "7.png"
(w, h, rgba, dummy) = png.Reader(img).read()

it = list(rgba)
mid = int(h / 2)
l = len(it[mid])
res = [chr(it[mid][i]) for i in range(0, l, 4*7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]
print("".join(res))
print("".join(map(chr, map(int, re.findall("\d+", "".join(res))))))
