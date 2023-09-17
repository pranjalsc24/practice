import math

# n= int(input("Enter a number: "))

# count=0
# for i in  range(1,n//2):
#     if(n%i==0):
#         count+=1


# if(count==1):
#     print("prime")

# else:
#     print('NO')   
# 
# 
# ------------another solution-----------


def prime(n):
    for i in range(2,n//2+1):       # for i in range(2,n//2)  or for i in range(2,math.sqrt(n))
        if n%i==0:
            return False
    return True
n=40
for i in range(2,n+1):
    if (prime(i)):
        print(i)

# --------------java---------------
# public class Main
# {
# 	public static void main(String[] args) {
# 		System.out.println("Hello World");
# 		int n=20;
# 		for(int i=2;i<=20;i++){
# 		  //  prime(i);
# 		    if(prime(i)){
# 		        System.out.println(i);
# 		    }
# 		}
		
# 	}
	
	# static boolean prime(int n){
	#     for(int i=2;i<=n/2;i++){
	#         if (n%i==0){
	#             return false;
	#         }
	#     }
	#     return true;
	# }
# }	    











