'''def arrange_year():
    pass                TEKA INIISIP KO PA TO KUNG NEED OR NO'''

def dmy(date):
    parts = date.split(" ")  # para ma manipulate kada word

    if len(parts) > 2:     # para mag skip sa 2nd word agad
        parts[0], parts[1] = parts[1], parts[0]  # switched day and month position
        parts[1] += "," # adds ung comma sa 2nd index

    print(" ".join(parts))  # para mawala sa list and magjoin ulit sila ganern


def ymd():
    pass

def iso():
    pass

def usa():
    pass

def eur():
    pass

def jis(date):
    if len(date) == 8 and date.isdigit():  #(carlito ito pacheck kung tama) chinecheck neto kung 8 characs ba ung ininput tas kung puro digit ba
        year, month, day = date[:4], date[4:6], date[6:] #iniisplit into 3 parts una 4 characters for Year susunod na dalawang charac for month susunod na 2 is for day
        return f"{month} {day}, {year}" #rearranging sa tamang format hehez

def main():
    '''
    FOR THE IFS STATEMENT ITONG MONTHS AND DAYS OR IF ILALAGAY KO PA SA ARRANGE YEAR FUNCTION
    '''
    months = []
    days = []
    
def main():
    user_input = " ".join(input("Enter date: ").title().split()) # used join and split para maremove ung mga whitespaces
    dmy(user_input)
    
main()