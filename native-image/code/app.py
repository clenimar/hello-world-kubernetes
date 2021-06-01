#!env python3
import click
import os

def write_int(filename, value):
    f = open(filename, "w")
    f.write(str(value))
    f.close()

def read_int(file):
    line = open(file).readline()
    return int(line)

@click.command()
@click.option('-v',  default='/V1/num', help='file number of executions.')
def main(v):
    if not os.path.exists(v):
        print("{} does not exist, creating ... ".format(v))
        os.mknod(v)
        print("And writing 1000 to it ... ")
        write_int(v,1000)

    num = read_int(v)
    print(f"Number of executions are {num}" )
    write_int(v, num+1)
    
if __name__ == '__main__':
    main()
