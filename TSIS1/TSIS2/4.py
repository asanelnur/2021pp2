class Solution(object):
    def largestAltitude(self, gain):
        a=[]
        sums=0
        for i in range(len(gain)):
            a.append(sums)
            sums+=gain[i]
        highest=-1000000001
        for i in range(len(a)):
            if a[i]>highest:
                highest=a[i]
        return highest  