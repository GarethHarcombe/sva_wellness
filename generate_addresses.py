import pandas as pd

def pretty_print_list(dct):
    for key, values in dct.items():
        print(key)
        values.sort(key=addr_sort)
        for v in values:
            print(f"    - {v}")


def addr_sort(x):
    i = x.find(" ")
    return x[i:]


def main():
    suburb_df = pd.read_excel("Delivery suburb sorted.xlsx", sheet_name="Sheet1")
    packs_df = pd.read_excel("SVA welfare pack distribution.xlsx", sheet_name="Proactive")
    #print(suburb_df.iloc[0])
    
    for _, row in suburb_df.iterrows():
        if type(row["TO SORT"]) == str:
            components = row["TO SORT"].replace("(", "").replace(")", "").split(",")
            comps = [c.strip() for c in components]
            if len(comps) > 1:
                for id in comps:
                    if id != '':
                        index = packs_df.index[packs_df["Delivery ID."] == int(id)].tolist()[0]
                        packs_df.at[index, "Unnamed: 3"] = row["TO DO:"]
    
    inpt = input("Enter the numbers of orders you would like to get addresses for: ").replace(")", "").replace("(", "").split(",")
    
    inpt_list = [int(i.strip()) for i in inpt if i.strip().isnumeric()]
    print(inpt_list)
    out_addresses = {}
    
    for i in inpt_list:
        matching = packs_df.loc[packs_df["Delivery ID."] == i]
        for index, row in matching.iterrows():
            packs_df.at[index, "SVA: delivery status (yes / no)"] = "UNDERWAY"
            out_addresses.setdefault(row["Unnamed: 3"], []).append(row["TermAddressDisplay"].replace("\n", " ").replace("_x000D_", ""))
            
    packs_df.to_excel("UPDATED: SVA welfare pack distribution.xlsx")
    print("Addresses:")
    pretty_print_list(out_addresses)
        

if __name__ == "__main__":
    main()