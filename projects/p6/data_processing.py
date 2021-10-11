FORMAT_STRING = "{:<12s}{:>10.2f}{:>10.2f}"

def main():
    filename_list = input("Enter filenames: ").split()
    process_all_files(filename_list)

def process_all_files(filename_list):
    '''Processes all the files in the given list'''
    for filename in filename_list:
        file_object = open_file(filename)
        if file_object is not None:
            print("\nFile {}:".format(filename))
            process_one_file(file_object)
            file_object.close()
        else:
            print("\nFile {} not found".format(filename))

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

def process_one_file(file_object):
    '''Processes one file'''
    str_list = get_data(file_object)
    name_list, height_list, weight_list = get_columns(str_list)

    height_list_float = get_floats(height_list)
    weight_list_float = get_floats(weight_list)
    
    average_height = get_average(height_list_float)
    average_weight = get_average(weight_list_float)

    print_averages(average_height, average_weight)
    print()
    print_data(name_list, height_list_float, weight_list_float)

  
def get_data(file_object):
    '''Returns a list of strings found in each line in the given file_oject''' 
    str_list = []
    for a_str in file_object:
        str_list.append(a_str.strip()) 	# strips newline
    return str_list

def get_columns(str_list):
    '''Returns three separate lists extracted from the given list of strings,
    i.e. three lists are extracted from "Joe 1.82 72.57" '''

    name_list = []
    height_list = []
    weight_list = []
    for a_str in str_list:
        name, height, weight = a_str.split()
        name_list.append(name)
        height_list.append(height)
        weight_list.append(weight)
    
    return name_list, height_list, weight_list
    
def get_floats(str_list):
    '''Returns a new list with float numbers from str_list.
    If an invalid float is found, it is changed to 0.0'''
    num_list = []
    for a_str in str_list:
        try:
            float_num = float(a_str)
            num_list.append(float_num)
        except ValueError:
            num_list.append(0.0)
    return num_list

def get_average(float_list):
    '''Returns the average of the numbers in the given list, ignoring zeros'''
    length = 0
    the_sum = 0
    for num in float_list:
        if num != 0:
            length += 1
            the_sum += num

    return the_sum / length

def print_averages(height, weight):
    print(FORMAT_STRING.format('Average', height, weight))

def print_data(name_list, height_list_float, weight_list_float):
    for i in range(len(name_list)):        
        print(FORMAT_STRING.format(name_list[i], height_list_float[i], weight_list_float[i]))    

# Main program starts here
if __name__ == "__main__":
    main()