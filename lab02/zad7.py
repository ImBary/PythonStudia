def most_frequent(items):
    most_freq = max(set(items),key=items.count)
    print(f'most freq {most_freq}')

most_frequent([1,2,3,4,5,4,4,1,4,4,4,2,1,1,1,1,])
