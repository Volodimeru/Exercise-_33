import sys
import csv
from tabulate import tabulate
d=[]
def main():
    cla_check()
def cla_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len (sys.argv) >2:
        sys.exit("Too fmany command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        tabulat()

def tabulat():
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d.append({"Sicilian Pizza":row["Pizza"], "Small":row["Size1"], "Large":row["Size2"]})
                print(tabulate(d, tablefmt = "grid"))
        except FileNotFoundError:
             sys.exit("File does not exist")
if __name__=="__main__":
    main()