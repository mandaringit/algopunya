T = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

new_scores = list(map(lambda num: num/max_score*100, scores))
print(sum(new_scores)/T)
