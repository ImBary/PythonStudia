import statistics
def statsy(lista):
    return f"max {max(lista)}, min {min(lista)}, mediana {statistics.median(lista)},odchylenie {statistics.stdev(lista) } "