def solution(friends, gifts):
    next_gifts = [0] * len(friends)
    give_dict = {}
    get_dict = {}
    for friend in friends:
        give_dict[friend] = []
        get_dict[friend] = []

    for gift in gifts:
        give, get = map(str, gift.split())

        give_dict[give].append(get)
        get_dict[get].append(give)
    
    for idx, friend in enumerate(friends):
        for i in range(idx+1, len(friends)):
            give_cnt = give_dict[friend].count(friends[i])
            get_cnt = get_dict[friend].count(friends[i])
            
            if give_cnt > get_cnt:
                next_gifts[idx] += 1
            elif give_cnt < get_cnt:
                next_gifts[i] += 1
            else:
                gift_point1 = len(give_dict[friend]) - len(get_dict[friend])
                gift_point2 = len(give_dict[friends[i]]) - len(get_dict[friends[i]])
                if gift_point1 > gift_point2:
                    next_gifts[idx] += 1
                elif gift_point1 < gift_point2:
                    next_gifts[i] += 1 
            
    answer = max(next_gifts)
    return answer