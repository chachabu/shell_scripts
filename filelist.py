import os
file_list = []
def get_all_dir(path):

    fills_list = os.listdir(path)

    for file_name in fills_list:
        file_abs_path = os.path.join(path, file_name)
        if os.path.isdir(file_abs_path):
            get_all_dir(file_abs_path)
            pass
        else:
            if '0122' in file_abs_path:
                print(file_abs_path)
            



def main():
    user_dir = r"/root"
    get_all_dir(user_dir)
    print(file_list)


if __name__ == "__main__":
    main()
