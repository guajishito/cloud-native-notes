
def print_file_info(file_name):
    f = None
    try:
        f = open("file_name", "r", encoding="UTF-8")
        print(f.read())
    except:
        print("文件异常")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open("file_name", "a", encoding="UTF-8")
    f.write(data)
    f.close()
