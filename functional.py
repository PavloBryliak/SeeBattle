import string


def read_file2(file_name):
    """
    Function for reading txt file and creating a game field
    due to this information.
    :param file_name: txt
    :return: list
    """
    s1 = ''
    lst1 = []
    with open(file_name, 'r') as file:
        for line in file:
            s1 += line
    lst1 = [j for i in s1 for j in i]
    for i in lst1:
        if i == '\n':
            lst1.remove(i)
    result = []
    for i in range(10):
        lst = [lst1[i] for i in range(10)]
        result.append(lst)
    return result


#def read_field(file_name):
#    return read_File(file_name)


def field_string(lst):
    """
    Function that converts field to string.
    :param lst: list
    :return: string
    """
    st = ""
    for i in lst:
        st += "[ "
        for j in i:
            st += j
        st += "]\n"
    return st


lstGrid = read_file2("sage.txt")

print(lstGrid)


def has_ship(lstGrid, tupleCord):
    """
    Function that checks whether given point has a ship.
    :param lstGrid: list
    :param tupleCord: tuple
    :return: boolean
    """
    #str = string.ascii_uppercase
    #lstApercase = [str[i] for i in range(10)]
    #tpl = tuple([tupleCord[1],lstApercase.index(tupleCord[0])])
    if lstGrid[tupleCord[0]][tupleCord[1]] == '*':
        return True
    elif lstGrid[tupleCord[0]][tupleCord[1]] == ' ':
        return False
#for i in range(10):
#    print(Has_Ship(lstGrid,("D",i)))


def ship_size(data, tuple1):
    """
    Function that defines given ship size.
    :return: int
    """
    str = string.ascii_uppercase
    lstApercase = [str[i] for i in range(10)]
    tpl = tuple([tuple1[1], lstApercase.index(tuple1[0])])
    lenght = 0
    if not has_ship(data,tpl):
        return 0
    else:
        for i in range(3):
            if has_ship(data, tuple([tpl[0] + i, tpl[1]])):
                lenght += 1
            elif has_ship(data, tuple([tpl[0] - i, tpl[1]])):
                lenght += 1
            elif has_ship(data, tuple([tpl[0], tpl[1] + i])):
                lenght += 1
            elif has_ship(data, tuple([tpl[0], tpl[1] - i])):
                lenght += 1
    return lenght


def is_valid(data):
    """
    Function that defines if given field can be valid.
    :return: boolean
    """
    str = string.ascii_uppercase
    lstApercase = [str[i] for i in range(10)]
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
           if has_ship(lstGrid, tuple([i, j])):
               sum += ship_size(lstGrid, tuple([lstApercase[i], j]))
    return 32 == sum


print(ship_size(lstGrid, ("A", 5)))

