def solve_baggage():
    T = int(input("Number of test cases: "))
    for i in range(T):
        N = int(input("\nNumber of conveyors: "))

        conveyors = [list(input("Space-separated baggage tags: ").split()) for _ in range(N)]

        X = int(input("Baggage tag to find: "))

        result = "Not Found"
        results = []

        # search through each conveyor
        for i in range(N):
            if conveyors[i] == X:
                result = i + 1 # 1-based index
                results.append(f"Case {i+1}: Conveyor {result}")
                break
            else:
                results.append(result)


        for i in results:
            print(i, end="\n")


solve_baggage()