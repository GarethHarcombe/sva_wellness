import pandas as pd

def pretty_print_list(lst):
    for item in lst:
        print(f"    - {item}")


def addr_sort(x):
    i = x.find(" ")
    return x[i:]


def main():
    suburb_df = pd.read_excel("Delivery suburb sorted.xlsx")
    packs_df = pd.read_excel("SVA welfare pack distribution.xlsx", sheet_name="Proactive")
    #print(packs_df.iloc[0])
    inpt = input("Enter the numbers of orders you would like to get addresses for: ").replace(")", "").replace("(", "").split(",")
    
    inpt_list = [int(i.strip()) for i in inpt if i.strip().isnumeric()]
    print(inpt_list)
    out_addresses = []
    
    for i in inpt_list:
        matching = packs_df.loc[packs_df["Delivery ID."] == i]
        for _, row in matching.iterrows():
            out_addresses.append(row["TermAddressDisplay"].replace("\n", " ").replace("_x000D_", ""))
            
    out_addresses.sort(key=addr_sort)
    print("Addresses:")
    pretty_print_list(out_addresses)
        

if __name__ == "__main__":
    main()