class Node():
    def __init__(self, label=None, value=0):
        self.label = label
        self.value = value
        self.left = None
        self.right = None
    

def count_words(sentence):
    
    word_counts = dict()
    
    for c in sentence:
        if word_counts.get(c) is None: 
            word_counts[c] = 1
        else: 
            word_counts[c] += 1
      
    word_counts = sorted(word_counts.items(), key=lambda x:x[1])
    
    return word_counts 

def create_huffman_tree(word_counts):
    
    
    temp_list = [Node(x[0],x[1]) for x in word_counts]
    
    while len(temp_list) > 1:
        
        smallest_index = None
        second_index = None
        
        for i, item in enumerate(temp_list):
            if smallest_index is None: 
                smallest_index = i
            else:
                if temp_list[smallest_index].value > item.value:
                    smallest_index = i
        
        smallest_node = temp_list.pop(smallest_index)
        
        for i, item in enumerate(temp_list):
            if second_index is None: 
                second_index = i
            else:
                if temp_list[second_index].value > item.value:
                    second_index = i
        
        second_node = temp_list.pop(second_index)
    
        new_node = Node()
        new_node.value = smallest_node.value + second_node.value
        new_node.left = smallest_node
        new_node.right = second_node
  
        temp_list.append(new_node)
    
    tree = temp_list[0]
    
    return tree 


    def binary_search_encode(tree, d, count, encoded_d=''):
    
    ret = ''
    
    if tree.left is None and tree.right is None:
        if tree.label == d:
            ret = encoded_d
        else:
            ret = ''

    else:
        if tree.left is not None:
            ret += binary_search_encode(tree.left, d, count, encoded_d+'0')
        if tree.right is not None:
            ret += binary_search_encode(tree.right, d, count, encoded_d+'1')
            
    return ret


def binary_search_decode(tree, code):
            
    if tree.left is None and tree.right is None: 
        return tree.label 
    
    for c in code: 
        
        if c == '0': 
            if tree.left is None: 
                return None
            else:
                return binary_search_decode(tree.left, code[1:])
            
        if c == '1':
            if tree.right is None:
                return None 
            else:
                return binary_search_decode(tree.right, code[1:])


def huffman_encoding(data):
    
    word_counts = count_words(data)
    word_counts_dict = dict(word_counts)
    tree = create_huffman_tree(word_counts)
    
    encoded_data =''

    for d in data: 
        count = word_counts_dict[d]
        encoded_d = binary_search_encode(tree, d, count)
        encoded_data += encoded_d
    
    return encoded_data, tree

def huffman_decoding(data,tree):
    
    tmp_data = data
    
    decoded_data = ''
    
    for i in range(len(data)):
        
        for le in range(1, len(tmp_data)+1):
            code = tmp_data[:le]
            decoded = binary_search_decode(tree, code)
            
            if decoded is not None:
                decoded_data += decoded
                tmp_data = tmp_data[le:]
                break
        
        
        if len(tmp_data) <= 0: 
            break
        
    return decoded_data


import sys


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word. the word is the bird"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    a_great_sentence = "ab"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    a_great_sentence = "long long lo-----------------------------------------------------------------------------------ng sentence"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
        