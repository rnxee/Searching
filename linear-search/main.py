# linear-search Function
def find_baggage(conveyors, target):
    for i in range(len(conveyors)): # Loops through conveyors
        for tags in conveyors[i]: # Loops through Baggage Tags
            if tags == target: # returns index if target is found
                return i + 1
    return -1


def get_baggage(conveyors):
    baggage = [] # Stores the baggage tags
    for i in range(conveyors):
        tags = input(f"Conveyor {i+1}: Baggage Tags: ")
        tags = [int (i) for i in tags.split()] # Splits the input
        baggage.append(tags)
    return baggage


def main():
    cases = int(input("Enter No. of test case/s: "))
    results = [] # Stores the result

    for i in range(cases): # For every case we'll execute this block of codes
        conveyors = int(input(f"\nCase {i+1}: No. of conveyors: "))
        baggage = get_baggage(conveyors) # Gets Baggage tag Numbers
        x = int(input("Enter missing baggage tag no.: "))

        result = find_baggage(baggage, x) # Gets the Conveyor where the missing baggage is

        if result != -1:
            results.append(f"Conveyor {result}.")
        else:
            results.append("Not Found.")

    print("\nResults:")
    for i, r in enumerate(results):
        print(f"Case {i+1}: {r}")

main()