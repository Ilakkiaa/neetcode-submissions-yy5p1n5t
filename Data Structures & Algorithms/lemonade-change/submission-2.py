class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        tt=0
        for i in bills:
            if i== 5:
                f+=1
            elif i==10:
                if f==0:
                    return False
                t+=1
                f-=1
            elif i==20:
                if t>0 and f>0:
                    t-=1
                    f-=1
                    tt+=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True


        