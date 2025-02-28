import random
import heapq

def create_population(timeslot, courses):
    population = []
    for t in range(10): 
        chromosome = ""
        for i in range(timeslot):
            slot = ""
            for j in range(courses):
                slot += str(random.choice([0, 1]))
            chromosome += slot
        population.append(chromosome)
    #print(population)
    return population


def penalty_count(chromosome, timeslot, courses):
    idx = 0
    overlap = 0
    for i in range(timeslot):
        count = 0
        for j in range(courses):
            if chromosome[idx] == '1':  
                count += 1
            idx += 1
        if count > 1:  
            overlap += (count - 1)
    #print(f"{chromosome}, Overlap Penalty: {overlap}")

    c_penalty = 0
    for i in range(courses):
        count = 0
        for j in range(timeslot):
            idx = j * courses + i
            if chromosome[idx] == '1': 
                count += 1
        c_penalty += abs(count - 1)

    #print(f"{chromosome}, Consistency Penalty: {c_penalty}")

    penalty = overlap + c_penalty
    return penalty


def parent_selection(population):
    p1 = random.randint(0, len(population) - 1)
    p2 = random.randint(0, len(population) - 1)
    while p1 == p2:
        p2 = random.randint(0, len(population) - 1)
 
    return population[p1], population[p2]


def mutation(child):
    child = list(child) 
    c = random.randint(0, len(child) - 1)
    if child[c] == '0':
        child[c] = '1'
    else:
        child[c] = '0'

    child =''.join(child) 
    return  child


if __name__ == "__main__":
    
    inp = open("input1.txt", "r")
    courses, timeslot = map(int, inp.readline().split())
    course_list = []
    for i in range(courses):
        temp=inp.readline().strip()
        course_list.append(temp)

    #print(course_list)
    print("Task-1")
    population = create_population(timeslot, courses)
    best = None

    for iter in range(1000):
        child_list = []
        for i in range(10):  
            p1, p2 = parent_selection(population)

            crossover_point = random.randint(1, len(p1) - 1)
            c1 = p1[:crossover_point ] + p2[crossover_point :]
            c2 = p2[:crossover_point ] + p1[crossover_point :]

          
            c1 = mutation(c1)
            c2 = mutation(c2)

            child_list.extend([c1, c2])

       
        heap = []
        for child in child_list:
            penalty = penalty_count(child, timeslot, courses)
            heapq.heappush(heap, (penalty, child))


        population = []
        for x in range(10):
            population.append(heap[x][1])


        if best is None or best[0] > heap[0][0]:
            best = heap[0]

        if best[0] == 0:  
            break
    print(best[1])
    print(best[0]*(-1))


    print("Task-2")
    cp1 = random.randint(0, len(p1) - 2)  
    cp2 = random.randint(cp1 + 1, len(p1) - 1)

    c1 = p1[:cp1] + p2[cp1:cp2] + p1[cp2:]  
    c2 = p2[:cp1] + p1[cp1:cp2] + p2[cp2:]

    #print(p1, p2)
    #print(cp1, cp2)
    print(c1, c2)
    