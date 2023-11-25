import csv

divisor = 100000

outfileno = 1

with open('../steam_reviews.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    lines = []
    count = 0
    
    for line in infile:
        count = count + 1
        lines.append(line)
        
        if count % divisor == 0:
            with open('steam_reviews_part/steam_reviews-{}.csv'.format(outfileno), 'w') as outfile:
                outfile.writelines(lines)
                lines = []
                outfileno += 1
                #print(f'File #: {outfileno-1} written')
    print('Final Lines')
    with open('steam_reviews_part/steam_reviews-{}.csv'.format(outfileno), 'w') as outfile:
                outfile.writelines(lines)
                lines = []