import random

dic = {'a': 'ストレート', 'b': '変化球'}

print('ピッチャーが投げた!')
print('a=ストレート b=変化球 aかbを入力して打ってください!')
user = input('>>>   ')
user = user.lower()

try:
	use_choice = dic[user]
	choice_list = ['a', 'b']
	pc =dic[random.choice(choice_list)]

	win = 'ヒット!'
	lose = 'アウト...'

	if use_choice == 'ストレート':
		if pc == 'ストレート':
			judge = win
		else:
			judge = lose
	elif use_choice == '変化球':
		if pc == '変化球':
			judge = win
		else:
			judge = lose

	print('あなたが選んだのは %s' % use_choice)
	print('コンピューターが選んだのは %s' % pc)
	print('結果は%s' % judge)
except:
	print('aかbを入力して打ってください!')