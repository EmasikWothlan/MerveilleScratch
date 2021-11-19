# implement of solution and container of solution.


class Container:
    _mass = 0  # g
    _volume = 0  # mL
    _solution = None  # empty by default
    _category = None  # another class family...
    
    def __init__(self, mass, category, volume, solution=None) -> None:
        self._mass = mass
        self._category = category
        self._volume = volume
        if solution:
            self.fill_by(solution)
    
    def describe(self):
        # 这很可能是所有 object 都具备的一个方法。
        if self._solution:
            filling_ratio = self._solution.amount / self._volume
            if filling_ratio < 0.25:
                approx = '一点'
            elif filling_ratio < 0.5:
                approx = '半瓶'
            elif filling_ratio < 0.75:
                approx = '大半瓶'
            elif filling_ratio == 1:
                approx = '满满一瓶'
            else:
                approx = '满溢出来的'
            return f'在{self._volume}mL的{self._category}中装着{approx}{self._solution.describe()}。'
        else:
            return f'{self._volume}mL的{self._category}中空空如也。'
    
    def fill_by(self, solution):
        available_amount = self._volume - (self._solution.amount if self._solution else 0)
        if solution.amount > available_amount:
            solution.set_amount(available_amount)
        self._solution = (self._solution + solution) if self._solution else solution


class Solution:
    amount = 0
    _description = ''
    
    def __init__(self, amount, desc) -> None:
        self.amount = amount
        self._description = desc
    
    def set_amount(self, amount):
        self.amount = amount
    
    def describe(self):
        return f'{self._description}的液体'

    def __add__(self, other):
        self.set_amount(other.amount + self.amount)
        return self


c = Container('玻璃瓶')
c.describe()

s = Solution(1000, '橙红色、透明')
s2 = Solution(500, '橙红色、透明')
c.fill_by(s)

c.describe()
print(c._solution.amount)
c.fill_by(s2)
print(c._solution.amount)


