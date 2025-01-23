import os


def get_all_data():
    data_path = os.path.join('q-fastapi.csv')
    output = """
        "students": [
    """
    with open(data_path, 'r') as file:
        file_contents = file.read().splitlines()
        for line in file_contents:
            line.strip('\n')
            id = line.split(',')[0]
            cls = line.split(',')[1].strip()
            
            output += f"""
            {{
                "studentId": {id},
                "class": {cls} 
            }},"""
    output = output[:-1] 
    output += """
        ]
    }
    """
    return output
def get_data_for_class(class_list):
    data_path = os.path.join('q-fastapi.csv')
    output = """
        "students": [
    """
    with open(data_path, 'r') as file:
        file_contents = file.read().splitlines()
        for line in file_contents:
            line.strip('\n')
            id = line.split(',')[0]
            cls = line.split(',')[1].strip()
            if cls in class_list:
                output += f"""
                {{
                    "studentId": {id},
                    "class": {cls} 
                }},"""
    output = output[:-1] 
    output += """
        ]
    }
    """
    return output


if __name__ == '__main__':
    s = get_all_data()
    print(s)
    
    class_list = ['2H']
    s = get_data_for_class(class_list)
    print("For the given classes:")
    print(s)