import asyncio
import csv
async def fetch_data(path):
    print('start fetching')
    with open(path) as input_file, open('results.csv', 'w') as csv_out:
        reader_obj = csv.reader(input_file)
        next(reader_obj)
        writer = csv.writer(csv_out, delimiter=',')
        await write_csv(writer,reader_obj)
    print('done fetching')
    return {'csv generated':'results.csv'}

async def write_csv(writer,reader_obj):
    writer.writerow(['Passenger with id less than 900 who survived'])
    for row in reader_obj:
        id = int(row[0])
        if id < 900 and int(row[1]):
            print(f'passenger found and id is {id}')
            writer.writerow([id])
   

async def main():
    path = 'data/titanic.csv'
    task1 = asyncio.create_task(fetch_data(path))
    value = await task1
    print(f'Results of task1 {value}')
    
asyncio.run(main())