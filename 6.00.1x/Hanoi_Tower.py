def hanoi(n, fr, spare, to):
	if n == 1:
		print 'from', fr, 'to', to
	else:
		hanoi(n-1, fr, to, spare)
		print 'from', fr, 'to', to
		hanoi(n-1, spare, fr, to)

hanoi(3, 'a', 'b', 'c')