import os

root = '' # add your root path
finish_file_path = '' # add path of file for save

def file_to_file (finish_file, root_path: str, files):
    for f in files:
        if f != '.DS_Store': 
            f_path = os.path.join(root_path, f)
            with open(f_path, mode='r', encoding='utf-8') as f_content:
                read_data = f_content.read()
                finish_file.write('\n\n' + f_path + '\n')
                finish_file.write(read_data)
                print(f_path, ' copied ->', finish_file_path)
        
if __name__ == "__main__":
    with open(finish_file_path, mode='a', encoding='utf-8') as finish_file:
        for r,d,f in os.walk(root):
            file_to_file(finish_file, r, f)

