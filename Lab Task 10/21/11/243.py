class InvalidVoterException(Exception):
    def __init__(self, message="Invalid Voter"):
        self.message=message
try:
    age=int(input("Enter You Age: "))
    if age<18:
        raise InvalidVoterException()
    else:
        print("Valid Voter")
except InvalidVoterException as e:
    print(e)