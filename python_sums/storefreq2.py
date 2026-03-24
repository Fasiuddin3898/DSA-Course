def main():
    given_list=map(int,input().split(" "))
    freq(given_list)

def freq(given_list):
    answer=dict()
    for i in given_list:
        answer[i]=answer.get(i,0)+1
    print(answer)
    return answer
if __name__=="__main__":
    main()
