# Create: • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS, each implementing a different
# logic method. Demonstrate how polymorphism can be achieved without inheritance by using interchangeable strategy objects.

class BS:
    def logic(self,arr):
        print("Bubble Sort")
        arr.sort()
        return arr
class MS:
    def logic(self,arr):
        print("Merge Sort")
        arr.sort()
        return arr
class QS:
    def logic(self,arr):
        print("Quick Sort")
        arr.sort()
        return arr
class Sorter:
    def change(self,strategy,arr):
        print(strategy.logic(arr))
a=[5,3,4,2,1]
s=Sorter()
l=[BS(),MS(),QS()]
for i in l:
    (s.change(i,a))
