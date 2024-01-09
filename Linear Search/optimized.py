data_list = [1, 2, 4, 6, 78, 2, 21, 11, 53, 99, 102, 12, 65, 6, 92, 73, 81, 66, 43]


def search(query):
    result = next((index for index, value in enumerate(data_list) if value == query), -1)
    return result


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
