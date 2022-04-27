N = int(input())
robots = []
for i in range(N):
	robot = {"name": input()}
	robots.append(input())

name = input()
for idx, i in enumerate(robots):
	if i == name:
		print(robots[idx])
