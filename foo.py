import jieba.posseg
import sys

names = {}
sentence = "\n".join([i for i in sys.stdin])
print(len(sentence))

for k, v in jieba.posseg.lcut(sentence):
	if v == 'nr':
		if k in names:
			names[k] = names[k]+1
		else:
			names[k] = 1
print(names)
