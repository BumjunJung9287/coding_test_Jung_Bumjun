if __name__ == "__main__":
    a_string = []
    with open("input.txt", "r") as f:
        while True:
            line = f.readline()
            if ":" not in line:
                num = int(line)
                break
            else:
                a, string = line.split(":")
                a = int(a)
                a_string.append((a, string[:-1]))
    ans_string = ""
    a_string = sorted(a_string, key=lambda x:x[0])
    for set in a_string:
        #print(set)
        a = set[0]
        string = set[1]
        #print(a,string)
        if num%a == 0:
            ans_string+=string
    if len(ans_string) == 0:
        print(num)
    else:
        print(ans_string)
