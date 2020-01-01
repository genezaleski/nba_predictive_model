from csv import reader
from math import sqrt
from math import exp
from math import pi
import time
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        if row[column]:
            row[column] = float(row[column].strip())
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
	    lookup[value] = i
            print('[%s] => %d' % (value, i))
	for row in dataset:
            row[column] = lookup[row[column]]
	return lookup
 
# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated
 
# Calculate the mean of a list of numbers
def mean(numbers):
        numbers = filter(bool,numbers)
        if not len(numbers)==0:
	    return sum(numbers)/float(len(numbers))
        else:
            return 0
 
# Calculate the standard deviation of a list of numbers
def stdev(numbers):
        numbers = filter(bool,numbers)
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)
 
# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries
 
# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries
 
# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent
 
# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities
 
# Predict the class for a given row
def predict(summaries, row):
	probabilities = calculate_class_probabilities(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label
 
# Make a prediction with Naive Bayes on Iris Dataset
filename = 'playerStatsCopy.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# fit model
model = summarize_by_class(dataset)
# define a new record
# pts,reb,ast
row = [15,1,1]
# predict the label
start = time.time()
label = predict(model, row)
end = time.time()
print('Data=%s, Predicted: %s' % (row, label))
if label==3:
    print("The statistics entered should belong to an all-star player.")
elif label==4:
    print("The statistics entered should belong to an above average scorer.")
elif label==2:
    print("The statistics entered should belong to an above average playmaker.")
elif label==0:
    print("The statistics entered should belong to an above average rebounder.")
elif label==1:
    print("The statistics entered should belong to an average nba player.")
print("Completed execution in ",end-start," seconds.")

def error_percentage(actual,predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100

predicted1 = []
row=[2,2,2]
predicted1.append(predict(model,row))
row=[2,6,6]
predicted1.append(predict(model,row))
row=[10,2,2]
predicted1.append(predict(model,row))
row=[13,8,9]
predicted1.append(predict(model,row))
row=[28,14,3]
predicted1.append(predict(model,row))
row=[15,1,2]
predicted1.append(predict(model,row))
row=[8,2,8]
predicted1.append(predict(model,row))
row=[17,1,1]
predicted1.append(predict(model,row))
row=[30,10,10]
predicted1.append(predict(model,row))
row=[14,2,4]
predicted1.append(predict(model,row))
actual1 = [1,2,1,2,3,4,2,4,3,4]
print("Error Rate: ",100-error_percentage(actual1,predicted1))
