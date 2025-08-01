#from library  import Library
#lib= Library()
import matplotlib.pyplot as plt
from votingsystem import VotingSystem
from person import Person
'''
def even_odd_sort (numberslist:list):
    ''''''
    identifies even and order number and 
    then sorts a list of even numbers in ascending order
    and sorts a list of odd numbers in descending order.
    ''''''
    even_numbers = sorted([num for num in numberslist if num %2 == 0])
    odd_numbers = sorted([num for num in numberslist if num %2 !=0],reverse=True)
    return even_numbers+ odd_numbers
'''
'''
def count_frequencies(inputlist:list):
    freq={}
    for item in inputlist:
        freq[item]=freq.get(item,0)+1
    return sorted(list(freq.items()), key=lambda x: (-x[1],x[0]))
'''
'''
def most_frequent(inputlist:list):
    freq={}
    for item in inputlist:
        freq[item]=freq.get(item,0)+1
    max_freq=max(freq.values())
    result= sorted([(item, count) for item, count in freq.items() if count==max_freq])
    return result
'''
'''
def even_squared(inputlist: list):
    even_num=list(filter(lambda x : x%2==0,inputlist))
    even_square=[even**2 for even in even_num]
    return even_square
'''
'''
def sorted_adult_names(personlist:list):
    ''''''
    function to sort and filter out adults for the list of person
    defination of adults: age>=18
    ''''''
    length_personlist=len(personlist)
    sorted_person=sorted(personlist,key=lambda x : -x[1])
    sorted_adults=list(filter(lambda x: x[1]>=18,sorted_person))
    sorted_adults=[person for person,age in sorted_adults if age>=18]
    length_sorted_adults=len(sorted_adults)
    percentage_of_adults=round((length_sorted_adults/length_personlist)*100,2)

    # 🎯 Bar Chart
    adult_count = length_sorted_adults
    non_adult_count = length_personlist - adult_count

    labels = ['Adults (18+)', 'Non-Adults']
    values = [adult_count, non_adult_count]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['green', 'red'])
    plt.title('📊 Population Breakdown')
    plt.ylabel('Count')
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    plt.show()
    return (sorted_adults,percentage_of_adults)
'''


if __name__ == "__main__":
    '''
    Example usage of the Library class.
    lib.add_book("The Hobbit")
    lib.add_book("1984")
    print(lib.list_books())
    print(lib.search_book("1984"))
    print(lib.search_book("Dune"))
    lib.remove_book("The Hobbit")
    print(lib.list_books())
    lib.remove_book("Dune") 
    numberslist = [10, 3, 5, 8, 2, 7, 6, 1, 4, 9]
    print(even_odd_sort(numberslist))
    print(count_frequencies(["banana","banana","kiwi","apple"]))
    print (most_frequent(["a","a","a","b","b","b","c"]))
    vote=VotingSystem(["java","java","python"])
    print(vote)
    print(even_squared([1,2,3,4]))
    print(sorted_adult_names([("Alice", 17), ("Bob", 20), ("Charlie", 18), ("David", 15)]))
    '''
    print(Person("alice","30"))