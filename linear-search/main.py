# Linear Search Function
def find_baggage(conveyors, target):
    for i in range(len(conveyors)): # Loops through conveyors
        for tags in conveyors[i]: # Loops through Baggage Tags
            if tags == target: # returns index if target is found
                return i + 1  # 1-based index
    return -1 # return -1 if not found


def get_baggage(conveyors):
    conveyor = [] # Stores the baggage tags
    for i in range(conveyors):
        tags = input(f"Conveyor {i+1}: Baggage Tags: ")
        tags = [int (i) for i in tags.split()] # Splits the tags with space as separator and converting them into integers
        conveyor.append(tags) # append each tags
    return conveyor # return the conveyor containing the baggage tags


def main():
    cases = int(input("Enter No. of test case/s: "))
    results = [] # Stores the test’s result

    for i in range(cases): # execute this block for every test
        conveyors = int(input(f"\nCase {i+1}: No. of conveyors: "))
        conveyor = get_baggage(conveyors) # Gets Baggage tag Numbers
        x = int(input("Enter missing baggage tag no.: "))

        result = find_baggage(conveyor, x) # Gets the Conveyor where the missing baggage is

        if result != -1:
            results.append(f"Baggage found at Conveyor {result}.")
        else:
            results.append("Not Found.")

    print("\nResults:")
    for i, r in enumerate(results):
        print(f"Case {i+1}: {r}")

main()