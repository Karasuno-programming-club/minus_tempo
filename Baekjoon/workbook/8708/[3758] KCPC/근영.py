T = int(input())

for _ in range(T):
    team_cnt, problem_cnt, answer_id, log_cnt = map(int, input().split())

    # 점수 기록할 리스트
    logs = [[0 for _ in range(problem_cnt + 1)] for _ in range(team_cnt + 1) ]
    # 풀이 횟수 기록할 리스트
    cnt = [0 for _ in range(team_cnt + 1) ]
    # 제출 시간 기록할 리스트(인덱스)
    time = [0 for _ in range(team_cnt + 1)]
    
    answer = [i for i in range(1, team_cnt + 1)]

    for i in range(log_cnt):
        team, problem, score = map(int, input().split())

        logs[team][problem] = max(logs[team][problem], score)
        cnt[team] += 1
        time[team] = max(time[team], i)
    
    answer.sort(key=lambda x:(-1 * sum(logs[x]), cnt[x], time[x]))
    print(answer.index(answer_id) + 1)