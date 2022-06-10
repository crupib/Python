class Solution(object):
    def mySqrt(self,number):
        if(number == 0):
            return 0;
        g = number/2.0;
        g2 = g + 1;
        while(g != g2):
            n = number/ g;
            g2 = g;
            g = (g + n)/2;
        return int(g);
def main():
  ob1 = Solution()
  print(ob1.mySqrt(20))
if __name__ == "__main__":
    main()
