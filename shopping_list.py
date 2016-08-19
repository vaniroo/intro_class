"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = ["cheese"]


def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list()


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list()

def file_creation(shopping_list_file, shopping_listitems):
    with open(shopping_list_file, mode = 'a') as  my_file:
        for item in shopping_list:
            my_file.write(item)
            my_file.write("\n")
#read master shopping list file, compare items in file to shopping_list global, if different, update global list
def read_file(shopping_list_file):
    with open(shopping_list_file) as my_file:
        output = my_file.read()
        return output

def parse_output_add_to_shopping_list(output):
    global shopping_list
    output_parts = output.split("\n")
    return shopping_list + output_parts



def main():

    # TEST FUNCTIONS
    # 1 - add 4 times to your shopping list
    print add_shopping_list("apple")
    print add_shopping_list("steak")
    print add_shopping_list("beef")
    print add_shopping_list("mustard")

    # 2 - Add an item that is already in the list. what happens?
    print add_shopping_list("apple")

    # 3 - Remove an item on your list
    print remove_item("apple")

    # 4 - Remove an item that is not in the list. what happens?
    print remove_item("chicken")

    # name of new shopping list to write
    shopping_list_file = "new_shopping_list.txt"
    # write new shopping list file using global shopping)list=[]
    file_creation(shopping_list_file, shopping_list)
    
    # read stored stored shopping list
    output = read_file("melissa_list.txt")

    # parse stored shopping list and add to global shopping_list = []
    print parse_output_add_to_shopping_list(output)

if __name__ == "__main__":
    main()