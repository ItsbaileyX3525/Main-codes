from colorama import Fore

r=input("hello\n")
if r=="hello":
	ahhh="are you having a good day"
	print(ahhh)
	e=input()
	if e=="yes":
		print("thats good")
	else:
		print("go away you bozo")
elif r=="hi":
	hehe="how are you?"
	print(hehe)
	r1=input()
	if r1=="good" or "great" or "amazing":
		print("good to hear that")
	else:
		print("hope it will get better")
elif r=="hey":
	heyhey="what you doing"
	print(heyhey)
	r2=input()
	if r2=="playing a game" or "just watching something":
		print("that sounds fun")
	if r2=="nothing" or "nothing much":
		print("hope you get up to something good")

print(Fore.GREEN+"3 hours later"+Fore.WHITE)

e=input("hey what are you doing currently\n")