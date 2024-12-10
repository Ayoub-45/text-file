def write(file_name):   
    lines=[]
    while True:
        line=input("Enter a line: ")
        line=line.strip()
        if line.upper()=="END":
            break
        lines.append(line)
    try:
        with open(file_name,"w") as file:
            file.write("\n".join(lines))
    except Exception as e:
        print(f"There is an error : {e}")
def read(file_name):
    with open(file_name,"r") as file:
        for line in file:
            line=line.lstrip()
            line=line.strip()
            print(line)
if __name__=="__main__":
    choice=input("1.Read file\n2.Write file\n->")
    if choice == "1":
        file_name=input("Enter a file name (with extension txt): ")
        read(file_name)
            