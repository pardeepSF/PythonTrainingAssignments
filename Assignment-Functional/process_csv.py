import csv

def read_csv(filename): 
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',') 
        return list(lines)[1:]


def clean_data(filename):
    
    data = read_csv(filename)
    data = list(filter(lambda x: int(x[0])>900 , data))
    data = list(filter(lambda x: int(x[1])==1, data))
    
    return list(map(lambda x:x[0], data))
def write_data(data):

    with  open('results.csv', 'w') as csv_out:
        writer = csv.writer(csv_out, delimiter=',')
        writer.writerow(['Passenger with id greater than 900 who survived and count=1'])
        for row in data:
            writer.writerow([row])
        csv_out.close()
   

if __name__ == '__main__':
    path = "data/titanic.csv"
    write_data(clean_data(path))