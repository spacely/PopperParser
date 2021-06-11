from ruamel import yaml
import ruamel
from yamlize import Object, Attribute
from collections import OrderedDict
import os


def prepend_multiple_lines(file_name, list_of_lines):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Iterate over the given list of strings and write them to dummy file as lines
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)








def convert_to_drone_format(_ordered_dict_popper_format):

    new_commented_seq = ruamel.yaml.comments.CommentedSeq() ## A CommentedSeq is the root of the structure of the Yaml using Yamlize toolkit

    ##new_commented_map = ruamel.yaml.comments.CommentedMap()
    kind_commented_map = ruamel.yaml.comments.CommentedMap()
    type_commented_map = ruamel.yaml.comments.CommentedMap()
    name_commented_map = ruamel.yaml.comments.CommentedMap()
    #steps_commented_map = ruamel.yaml.comments.CommentedMap()

    kind_commented_map["kind"] = "pipeline"
    type_commented_map["type"] = "docker"
    name_commented_map["name"] = "default"
    

    ##new_commented_seq.append(kind_commented_map)
    ##new_commented_seq.append(type_commented_map)
    ##new_commented_seq.append(name_commented_map)
    ##new_commented_seq.append("steps")

    new_ordered_dict = dict()

   
    

    for vals in _ordered_dict_popper_format:
        new_commented_map = ruamel.yaml.comments.CommentedMap() ## A commentedMap is embedded as an individual element within a commentedSeq
        for key,value in vals.items():

            if (key == 'id'):
                new_commented_map["name"] = value
                
            elif(key == 'uses'):
                value = value.partition("//")[2]
                new_commented_map["image"] = value

            elif(key == 'args'):
                new_commented_map["commands"] = value
            elif(key == 'env'):

                new_commented_map["environment"] = value ## If environment, call function(to be written) recur

            else:
                new_commented_map[key] = value

        new_commented_seq.append(new_commented_map)
    return new_commented_seq

## A class to extract the structure of the Yaml file for Popper YAML files.
class PopperFormat(Object):
    steps = Attribute()



        

with open('wf.yml') as f:

    popper = PopperFormat.load(f)
    ##a = popper.Inner()
   
    ##print(type(popper))   
    ordered_dict_popper = popper.steps ## an ordereddict ##ORdered dict as an argument to a function.
    ##print((ordered_dict_popper))
    
    drone_convert = convert_to_drone_format(ordered_dict_popper)
    print(drone_convert)
    
    

    with open('drone_format.yml', 'w') as yaml_file:
        yaml.dump(drone_convert, yaml_file,Dumper=ruamel.yaml.RoundTripDumper)
        
    
list_of_lines = ['kind: pipeline', "type: docker", "name: default","steps: "]
prepend_multiple_lines("drone_format.yml", list_of_lines)




    

    
    

