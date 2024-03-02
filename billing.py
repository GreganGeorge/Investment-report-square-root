totalcost=0;
stock={"pen":10,"pencil":5,"eraser":20,"book":0};
price={"pen":10,"pencil":5,"eraser":5,"book":30};
print("The items available are :");
for key in stock:
    if(stock[key]>0):
        print(key,":",stock[key]);
while True:
    item=input("Enter the item to be bought");
    n=int(input("Enter the number of items to be bought"));
    if(item in stock and stock[item]>=n):
        stock[item]=stock[item]-n;
        if(item in price):
            totalcost+=price[item]*n;
    for key2 in stock:
        if(stock[key2]>0):
            print(key2,":",stock[key2]);
    if(input("Enter y to continue or n to break")=='n'):
        break;
print("Total cost is ",totalcost);

        
        
        

