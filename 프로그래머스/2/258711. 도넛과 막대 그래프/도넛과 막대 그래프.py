def solution(edges):
    answer = [0, 0, 0, 0] #생성한 정점 번호, 도넛 모양 개수, 막대 모양 개수, 8자 모양 개수
    
    #진출 차수, 진입 차수 구하기
    nodes = {}
    for a, b in edges:
        if a not in nodes:
            nodes[a] = [0, 0]
        if b not in nodes:
            nodes[b] = [0, 0]
        
        nodes[a][0] += 1
        nodes[b][1] += 1

    for node_num, out_in in nodes.items():
        
        #생성한 정점(진출 차수 >= 2, 진입 차수 0)
        if out_in[0] >= 2 and out_in[1] == 0:
            answer[0] = node_num
        #막대 개수(진출 차수 0, 진입 차수 >= 1)
        elif out_in[0] == 0 and out_in[1] >= 1:
            answer[2] += 1
        #8자 개수(진출 차수 2, 진입 차수 >= 2)
        elif out_in[0] == 2 and out_in[1] >= 2:
            answer[3] += 1
    #도넛 개수(생성한 정점의 진출 차수 - 막대 개수 - 8자 개수)
    answer[1] = nodes[answer[0]][0] - answer[2] - answer[3]
        
    return answer