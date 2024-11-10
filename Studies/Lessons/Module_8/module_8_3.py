class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__is_valid_vin(vin)    #Возврат True
        self.__numbers = numbers
        self.__is_valid_numbers(numbers)    #Возврат True