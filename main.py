import csv
def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    
    f=open(file_name)
    data=csv.reader(f)
    l=[]
    for i in data:
        l.append(i[-1])
    return sorted(l)
print(get_country_column("data.csv"))
