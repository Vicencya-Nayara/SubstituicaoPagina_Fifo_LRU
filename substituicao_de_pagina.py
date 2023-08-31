import random

def fifo(page_references, num_frames):
    frames = [-1] * num_frames  # Inicializa os frames com -1 (vazios)
    page_faults = 0

    fifo_queue = []  # Fila para o algoritmo FIFO

    for page in page_references:
        if page not in frames:
            if len(fifo_queue) < num_frames:
                fifo_queue.append(page)
            else:
                evicted_page = fifo_queue.pop(0)
                if evicted_page in frames:
                    frames[frames.index(evicted_page)] = page
                fifo_queue.append(page)
            page_faults += 1

    return page_faults

def lru(page_references, num_frames):
    frames = [-1] * num_frames  # Inicializa os frames com -1 (vazios)
    page_faults = 0

    lru_queue = []  # Lista para o algoritmo LRU

    for page in page_references:
        if page not in frames:
            if len(lru_queue) < num_frames:
                lru_queue.append(page)
            else:
                evicted_page = lru_queue.pop(0)
                if evicted_page in frames:
                    frames[frames.index(evicted_page)] = page
                lru_queue.append(page)
            page_faults += 1
        else:
            lru_queue.remove(page)
            lru_queue.append(page)

    return page_faults

def main():
    num_page_references = 50  # Número de referências de página aleatórias
    page_references = [random.randint(0, 9) for _ in range(num_page_references)]

    print("Referências de página aleatórias:", page_references)

    for num_frames in range(1, 11):  # Testa de 1 a 10 quadros de página
        print(f"\nNúmero de quadros de página: {num_frames}")
        print("Número de page faults usando FIFO:", fifo(page_references, num_frames))
        print("Número de page faults usando LRU:", lru(page_references, num_frames))

if __name__ == "__main__":
    main()
