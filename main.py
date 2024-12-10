def write_to_file():
    file_name=input("Enter a file name (with extension txt): ")
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
        
if __name__=="__main__":
    write_to_file()      
        
            