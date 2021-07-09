class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sumof=0
        while n>0:
            i=n%10
            product*=i
            sumof+=i
            n/=10
        res=product-sumof
        return res