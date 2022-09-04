from csv import reader

def read_csv(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)

        for row in csv_reader:
            if ("Game" in row[0]):
                print(row[0])

def combine_list_to_dictionary(row,row2):            
    stats = {}

    row = ['Player', 'REB', 'AST', 'BLK', 'STL', '2PM', '2PA', '3PM', '3PA', 'TO', 'PTS', 'FGA', 'FG%', '3P%', '2P%']
    row2 = ['Brian', '3', '1', '', '1', '1', '1', '1', '4', '', '3', '5', '40.00%', '25.00%', '100.00%']

    for (column_name,value) in zip(row,row2):
        stats.update({column_name:value})

    print(stats)
    
    
def main():
    read_csv('/Users/briantsai/Desktop/basketball_stats/src/Basketball_Stats_Sheet.csv')
    
    combine_list_to_dictionary(['Player', 'REB', 'AST', 'BLK', 'STL', '2PM', '2PA', '3PM', '3PA', 'TO', 'PTS', 'FGA', 'FG%', '3P%', '2P%'],
                               ['Brian', '3', '1', '', '1', '1', '1', '1', '4', '', '3', '5', '40.00%', '25.00%', '100.00%'])
    
main()