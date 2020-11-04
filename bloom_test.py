from bloomfilter import BloomFilter
from random import shuffle

def loadDatadet(infile):
	f=open(infile,'r')
	sourceInLine=[]
	for line in f.readlines():
		sourceInLine.append(line.strip('\n'))
	return sourceInLine


n = 20 #no of items to add
p = 0.05 #false positive probability

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))
'''
# original data set
# words to be added
word_present = ['abound','abounds','abundance','abundant','accessable',
				'bloom','blossom','bolster','bonny','bonus','bonuses',
				'coherent','cohesive','colorful','comely','comfort',
				'gems','generosity','generous','generously','genial']

# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
			'racism','hurt','nuke','gloomy','facebook',
			'geeksforgeeks','twitter']

for item in word_present:
	bloomf.add(item)

shuffle(word_present)
shuffle(word_absent)

test_words = word_present + word_absent
shuffle(test_words)
'''
# dataset from files
word_present=loadDatadet("dataset1.txt")
for item in word_present:
	bloomf.add(item)

test_words=loadDatadet("dataset2.txt")
shuffle(test_words)

bf_res_false_pos = []
bf_res_prob_pres = []
bf_res_false_neg = []
bf_res_not_pres = []

for word in test_words:
	if bloomf.check(word):
		# BF suggest it is probably present
		bf_res_prob_pres.append(word)
	else:
		# BF suggest it is not present
		bf_res_not_pres.append(word)


# check the result
for word in bf_res_prob_pres:
	if word not in word_present:
		bf_res_false_pos.append(word)

for word in bf_res_not_pres:
	if word in word_present:
		bf_res_false_neg.append(word)

#print("Test word: {}".format(len(test_words)))
print("BF result - definitely not present({}) : {}, \n\tin which false negative({}) : {}".format(len(bf_res_not_pres), bf_res_not_pres, len(bf_res_false_neg), bf_res_false_neg))
print("BF result - probably present({}) : {}, \n\tin which false positive({}) : {}".format(len(bf_res_prob_pres), bf_res_prob_pres, len(bf_res_false_pos), bf_res_false_pos))
print("BF result - test false positive probability : {}".format(float(len(bf_res_false_pos) + len(bf_res_false_neg)) / len(test_words) ))
