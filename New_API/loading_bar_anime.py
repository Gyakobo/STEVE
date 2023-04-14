import math
import colorama
import sys

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100-int(percent))
    sys.stdout.write(color + f"\r|{bar}| {percent:.2f}%")
    sys.stdout.flush()

for i in range(0, 100000):
    progress_bar(i+1, 100000)

print(colorama.Fore.RESET)


