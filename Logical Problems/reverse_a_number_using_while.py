n=int(input("Enter a number to reverse:"));
rev=0;
while n!=0:
    rev=rev*10+n%10;
    n=n//10;
print(rev);

//or
//    rev=int(str(n)[::-1]);

