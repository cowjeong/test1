import pickle 

list =['a','b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(list, f)