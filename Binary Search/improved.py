import bisect

data_list = [1, 2, 4, 8, 6, 78, 2, 21, 11, 53, 99, 102, 12, 65, 6, 92, 73, 81, 66, 43]
data_list.sort()


def search(query):
    if query not in data_list:
        return -1
    return bisect.bisect_left(data_list, query)


def main():
    print("Hi! The current list of data is: ", data_list, ".")
    print("")
    query = int(input("To begin your search, enter a query: "))

    result = search(query)

    if result == -1:
        print(f"{query} was not found in the list!")
    else:
        print(f"{query} was found in the list at index: {result}")

main()
