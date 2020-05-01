import csv
import string
import numpy as np
import re
from common  import *


reviews = []
with open('reviews_detailed.csv',"r",encoding='iso-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            txt = remove_stop_words(word_tokenize(to_lower_case(row[5])))
            reviews.append(' '.join(txt).translate(str.maketrans('', '', string.punctuation)) + '.')
            line_count += 1
    print(f'Processed {line_count} lines. Number of reviews read {len(reviews)}')


with open('preprocessed_reviews_no_stemming_full_data.csv', 'w',encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["comments"])
    for review in reviews:
        writer.writerow([review])
