# a=int(input("enter a number: "))

# u= a%10;    
# a=a//10;       # integer division
# d= a%10;  
# a= a//10;   
# sum=u+d+a
# r=u*100+d*10+a
# print(f"sum od digit={sum} and reverse={r}")


# // **************** using loop*******************

# a=int(input("enter a number: "))
# sum=0

# while(a>0):
#     d=a%10
#     sum=sum+d
#     a=a//10

# print(f"sum of digit={sum}")   



# // **************** using for loop*******************
a=int(input("enter a number: "))
sum=0

for i in range(len(str(a))):
    d=a%10
    sum=sum+d
    a=a//10

print(f"sum of digit={sum}")   


# -----------using recursion------------
# public class Main
# {
# 	public static void main(String[] args) {
# 	    int ans=sum(1234);
# 		System.out.println(ans);
		
# 	}
	
# 	static int sum(int n){
# 	    if (n==0){
# 	        return 0;
# 	    }
# 	    else{
# 	        return (n%10) +sum(n/10);
# 	    }
# 	}
# }

