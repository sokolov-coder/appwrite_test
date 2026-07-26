import os

def main(context):
    files = []

    for root, dirs, filenames in os.walk("."):
        for f in filenames:
            files.append(os.path.join(root, f))

    return context.res.json({
        "cwd": os.getcwd(),
        "files": files
    })