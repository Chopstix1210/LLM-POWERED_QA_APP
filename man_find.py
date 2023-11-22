import subprocess
import tempfile

def find_man_page(command): 
    try:
        # using subprocess to find location of man page (possible ambiguity) 
        result = subprocess.run(['man', '-w', command], capture_output=True, text=True, check=True)
        path = result.stdout.strip()
        #return load_man_page(path)
        return convert_to_txt(path)

    except FileNotFoundError: 
        return None

def convert_to_txt(path):
    try: 
        with open(path, 'r') as f: 
            file_content = f.read()
            with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='/tmp', suffix='.txt') as tf: 
                tf.write(file_content)

                temp_file_path = tf.name
                return temp_file_path
    except FileNotFoundError:
        return None

# might not need this function since I need to load the file not the text 
def load_man_page(path):
    try:
        with open(path, 'r') as f: 
            man_page_contetent = f.read() 
        return man_page_contetent
    except FileNotFoundError:
        # print('Man Page not found!')
        return None

def find_documentation(command):
    return find_man_page(command)