import numpy as np
import re

# label_encodes = ['0010', '0110', '1001', '1100']
label_encodes = ['0110', '0111', '1110', '1111']

stack = ['1', '0']
t = 0
while stack:
    quo = stack.pop()
    res = [re.match(quo, label_encode) for label_encode in label_encodes]
    match_labels = np.where(res)[0]
    num = match_labels.size
    if num > 1:
        stack.append(quo + '1')
        stack.append(quo + '0')
    t += 1

print("遍历次数:", t)