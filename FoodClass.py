class Customer():
    def __init__(self, customer_id, name, address, email, phone, status):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
    
    def get_id(self):
        return self.__customer_id
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_status(self):
        return self.__status

class Transaction():
    def __init__(self, date, item_name, cost, customer_id):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__customer_id = customer_id
    
    def get_date(self):
        return self.__date
    
    def get_item_name(self):
        return self.__item_name

    def get_cost(self):
        return self.__cost
    
    def get_customer_id(self):
        return self.__customer_id