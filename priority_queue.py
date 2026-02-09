#in priority queue elements are based on priority, smaller value higher priority
import heapq

def main():
    pq=[]

    #push elements
    heapq.heappush(pq,10)
    heapq.heappush(pq,1)
    heapq.heappush(pq,4)

    #pop smallest first
    print(heapq.heappop(pq))  # 1
    print(heapq.heappop(pq))  # 4
    
    #priority queue with priority value, it will pop based on tuple value
    priority = []

    heapq.heappush(priority, (0, 'A'))
    heapq.heappush(priority, (2, 'B'))
    heapq.heappush(priority, (1, 'C'))

    print(heapq.heappop(priority))  # (0, 'A')
    print(heapq.heappop(priority))  # (1, 'C')

if __name__=="__main__":
    main()
