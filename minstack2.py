####### FileName = MinStack2.py

'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.'''


class NewMinStack:
      def __init__(self):
            self.stack = []
            self.minstack = []


      def push(self, x):
            self.stack.append(x)
            if len(self.minstack) == 0 or x < self.minstack[-1][0]: 
                  self.minstack.append((x, 1))
                  
            elif x == self.minstack[-1][0]:
                  self.minstack[-1] = (x, self.minstack[-1][1] + 1)
                  ##### x = min, the fequency of x add by 1

      def pop(self):
            p = self.stack.pop()
            if p == self.minstack[-1][0]:
                  if self.minstack[-1][1] > 1:
                        self.minstack[-1] = (self.minstack[-1][0], self.minstack[-1][1]-1)
                  else:
                        self.minstack.pop()
            
      def top(self):
            return self.stack[-1]

      def getMin(self):
            return self.minstack[-1][0]


if __name__ == "__main__":
      L = NewMinStack()
      L.push(2)
      L.push(0)
      L.push(0)
      L.getMin()
      L.pop()
      L.getMin()

      print(L.getMin())
      print(L.top())
                  
