train_set = []
valid_set = []
test_set = []

for i in range (1810):
    train_set.append("train/images/Bbox_{}".format(str(i+1).zfill(4)))
print(*train_set,sep=',')
for i in range(1811,2271,1):
    valid_set.append("valid/images/Bbox_{}".format(str(i).zfill(4)))
print(*valid_set,sep=',')
for i in range(2271,2481,1):
    test_set.append("test/images/Bbox_{}".format(str(i).zfill(4)))
print(*test_set,sep=',')
