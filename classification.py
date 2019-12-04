import numpy as np
from collections import Counter, OrderedDict
import matplotlib.pyplot as plt
import seaborn as sns

data = np.load('lingspam.npz',allow_pickle=True)
##print(data.files)
print(data['words'][0][:15])
print(data['file_names'][0])
print(data['targets'][0])
print(data['target_names'])
num_emails = len(data['words'])
print(num_emails)
total_words=0
cnt=Counter()

for entry in data['words']:
    total_words=+len(entry)
    for word in entry:
        cnt[word]=+1
ordered_cnt = OrderedDict(cnt.most_common())
print('Length of Dict:',len(cnt))
print('total_words:',total_words)



# create plot
plt.figure(figsize=(12,5))
sns.barplot(x=list(ordered_cnt.keys())[0:10], y=list(ordered_cnt.values())[0:10])
_ = plt.xlabel("words")
_ = plt.ylabel("occurrence")
_ = plt.title("Number of occurrences of words in emails")

# save figure
plt.savefig('plot.png', dpi=200)