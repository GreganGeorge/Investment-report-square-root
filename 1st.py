investment=float(input("Enter the investment amount : "));
sums=0;
years=int(input("Enter the number of years : "));
rate=int(input("Enter the rate as a % : "));
print("Year\tStarting balance\tInterest\tEnding balance");
for i in range(1,years+1):
    print("%4s"%i,end="\t\t");
    print("%0.2f"%investment,end="\t");
    a=(investment*rate)/100;
    sums=sums+a;
    print("%7s"%"%0.2f"%a,end="\t")
    investment=investment+a;
    print("%11s"%"%0.2f"%investment);
print("Ending balance: $%0.2f"%investment);
print("Total interest earned: $%0.2f"%sums)
