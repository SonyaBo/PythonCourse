class Phone:
    number: str = ""
    _calls: int = 0

    def change_number(self, new_num: str) -> None:
        self.number = new_num

    def return_call_num(self)-> int:
        return self._calls
    def take_call(self) -> None:
        self._calls += 1

def number_of_calls(phones: list[Phone]) -> int:
    result = 0
    """
    for phone in phones:
        result += phone.return_call_num()
    return result
    
    -- in on line with comprhension and sum()
    """
    return sum(ph.return_call_num() for ph in phones)

p1=Phone()
p1.change_number("+4201111111")
p1.take_call()
p2=Phone()
p2.change_number("+4201111111")
p1.take_call()
p1.take_call()
p3=Phone()
p3.change_number("+4201111111")
p1.take_call()
p1.take_call()
p1.take_call()
hh = [p1,p2,p3]
print(number_of_calls(hh))