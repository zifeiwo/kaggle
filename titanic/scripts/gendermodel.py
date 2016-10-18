import csv as csv
import numpy as np

#open csv file
csv_file_object=csv.reader(open('../csv/train.csv','rb'))
csv_file_object.next()

data=[]
for line in csv_file_object:
    data.append(line)
data=np.array(data)

num_passengers=np.size(data[0::,1].astype(np.float)) 
num_survived=np.sum(data[0::,1].astype(np.float))
proportion_survived=num_survived/num_passengers

women_only_stat=data[0::,4]=='female'
men_only_stat=data[0::,4]!='female'

women_survived=data[women_only_stat,1].astype(np.float)
men_survived=data[men_only_stat,1].astype(np.float)

proportion_women_survived=np.sum(women_survived)/np.size(women_survived)
proportion_men_survived=np.sum(men_survived)/np.size(men_survived)

print 'all survived proportion:%s' % proportion_survived
print 'men survived proportion:%s' % proportion_men_survived
print 'women survived proportion:%s' % proportion_women_survived

test_file=open('../csv/test.csv','rb')
test_file_object=csv.reader(test_file)
test_file_object.next()

prediction_file=open('../csv/genderbasedmodel.csv','wb')
prediction_file_object=csv.writer(prediction_file)
prediction_file_object.writerow(['PassengerId','IsSurvived'])
for line in test_file_object:
    if line[3]=='female':
        prediction_file_object.writerow([line[0],'1'])
    else:
        prediction_file_object.writerow([line[0],'0'])
prediction_file.close()
test_file.close()

