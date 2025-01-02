import sys
import time

def progress_bar(percentage, width=50):
    """
    打印进度条
    :param percentage: 当前进度百分比 (0-100)
    :param width: 进度条的宽度，默认是50字符
    """
    completed = int(width * (percentage / 100))              #已完成部分
    remaining = width - completed                            #未完成部分
    bar = f"[{'#' * completed}{'.' * remaining}]"
    sys.stdout.write(f"\rProgress: {percentage:3d}% {bar}")  #动态刷新行
    sys.stdout.flush()                                       #※实现动态更新，不换行输出

# 模拟进度条运行
for i in range(101):    #0%到100%
    progress_bar(i)     #更新进度条
    time.sleep(0.05)    #模拟延迟

print("\nDone!")        #结束后换行
