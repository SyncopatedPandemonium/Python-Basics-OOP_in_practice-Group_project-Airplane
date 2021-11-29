def singleton(class_):
    instances = {}
    def getinstance():
        if class_ not in instances:
            instances[class_] = class_()
        return instances[class_]
    return getinstance