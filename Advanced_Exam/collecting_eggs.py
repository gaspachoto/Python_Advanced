from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])
boxes_filled = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()
    total_size = egg + paper
    if egg <= 0:
        papers.append(paper)
        continue
    if egg == 13:
        last = papers.popleft()
        papers.appendleft(paper)
        papers.append(last)
        continue
    if total_size <= 50:
        boxes_filled += 1
    else:
        continue

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
