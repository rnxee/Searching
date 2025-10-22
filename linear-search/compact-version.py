def solve_baggage():
    T = int(input("Number of test cases: "))
    results = []
    for t in range(T):
        T -= 1
        N = int(input("\nNumber of conveyors: "))
        conveyors = [list(map(int, input("Space-separated baggage tags: ").split())) for _ in range(N)]
        X = int(input("Baggage tag to find: "))

        result = "Not Found"
        case = f"Case {t + 1}"

        # search through each conveyor
        for i in range(N):
            if X in conveyors[i]:
                result = i + 1 # 1-based index
                results.append(f"{case}: Conveyor {result}")
                break
        else: results.append(f"{case}: {result}")

        if T == 0:
            print()
            for j in results:
                print(j, end="\n")

solve_baggage()