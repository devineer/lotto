w,h = 2,46
num_count =  [[0 for x in range(w)] for y in range(h)] 

for idx in range(0,46):
    num_count[idx][0] = idx

with open("lotto.csv") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for episode in content:
    numbers = episode.split(',')
    numbers.pop(0)
    for num in numbers:
        num_count[int(num)][1] += 1

print sorted(num_count,key=lambda l:l[1], reverse=True)
