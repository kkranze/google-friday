def push():
	x = 10
	har = ha(False)
	dee = ha(True)
	print(har,dee)
def ha(asdf):
	if(asdf):
		return hip(foo(),bar())
	else:
		return hip(bar(),foo())
def hip(hop,hi):
	return hop + hop + hi
def foo():
	return "this one"
def bar():
	print("well maybe")
	return "that one"

this = "hello this is a good day".split(" ")
bar()
foo()
print(hip(bar(),foo()))
