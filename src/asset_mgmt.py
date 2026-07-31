import os, shutil

def copy_contents(source: str, destination: str):
    print(os.path.exists(source))
    if not os.path.exists(source):
        raise Exception("source directory does not exist!")
    # delete destination
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_recurse(source, destination)
    pass

def copy_recurse(source:str, destination:str):
    print(f"source: {source}")
    print(f"destination: {destination}")
    if not os.path.exists(destination):
        os.mkdir(destination)
    for content in os.listdir(source):
        if os.path.isdir(f"{source}/{content}"):
            copy_recurse(f"{source}/{content}", f"{destination}/{content}")
        else:
            shutil.copy(f"{source}/{content}", destination)
    pass
