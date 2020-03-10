
import os 

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
 
    found_list = []
    
    items = os.listdir(path)    
    for item in items: 
        
        item_path = path+'/'+item
    
        if os.path.isfile(item_path):
            if item.endswith(suffix):
                found_list.append(item_path)
        else:
            list_to_add = find_files(suffix, item_path)
            if len(list_to_add) > 0: 
                found_list.extend(list_to_add) 

    return found_list


suffix = 'c'
path = './testdir'

find_files(suffix, path)

suffix = 'a'
path = './testdir'

find_files(suffix, path)

suffix = 'p'
path = './testdir'

find_files(suffix, path)