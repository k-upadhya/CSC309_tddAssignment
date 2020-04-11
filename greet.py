def greet(name):
    if name is None:
        return "Hello, my friend."
    elif isinstance(name, list):

        i = 0
        while (i < len(name)):
            if "\"" in name[i]:
                name[i] = name[i].strip("\"")
            elif ',' in name[i]:
                print(name[i])
                t = name[i].split(",")
                name.remove(name[i])
                name.append(t[0])
                name.append(t[1].strip())
            i += 1

        if len(name) > 2:
            temp = "Hello, "
            upper = []
            normal = []

            i = 0
            while(i < len(name)):
                if name[i].isupper() is True:
                    upper.append(name[i])
                else:
                    normal.append(name[i])
                i+=1

            if len(normal) > 2 :
                i = 0
                while(i < len(normal) - 1):
                    temp += normal[i] + ", "
                    i+=1
                temp+= "and " + normal[len(normal) - 1] + "."
            else:
                temp+= normal[0] + " and " + normal[1] + "."

            if len(upper) > 0:
                temp+= " AND HELLO "
                if len(upper) > 1:
                    i = 0
                    while (i < len(upper) - 1):
                        temp += upper[i] + ", "
                        i+= 1
                    temp += "AND " + upper[len(upper) - 1] + "!"
                else:
                    temp+= upper[0]+ "!"

            return temp

        return "Hello, " + name[0] +" and " + name[1] + "."
    elif name.isupper() is True:
        return "HELLO " + name + "."
    return "Hello, " + name + "."