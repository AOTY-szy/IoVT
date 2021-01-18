import numpy as np

def simulate(label_nums, frame_step):
    uncompleted = list(range(label_nums))
    frame = 0
    while True:
        choices = np.random.randint(0, frame_step, (len(uncompleted), ))
        dels = []
        for i in np.unique(choices):
            uni = np.where(choices == i)[0]
            if uni.size > 1:
                conflict = [uncompleted[j] for j in uni]
                print("在{0}号帧的{1}号间隙".format(frame, i), end=" ")
                print("标签", *conflict, end="")
                print(" 发生冲突")
            else:
                print("在{0}号帧的{1}号间隙".format(frame, i), end=" ")
                print("标签", str(uncompleted[uni[0]]), end="")
                print(" 完成发送")
                dels.append(uni[0])
        [uncompleted.pop(d) for d in sorted(dels, reverse=True)]
        if not len(uncompleted):
            break

        frame += 1
    print("Over")


if __name__ == '__main__':
    simulate(20, 10)