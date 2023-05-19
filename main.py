import web3
import json
import rsa
class Smart():

    url = "HTTP://127.0.0.1:8545"

    webber = web3.Web3(web3.HTTPProvider(url))

    address_contract = '0xAeC7B46AAe412eb34916161Ef6458c94F8C5c394'
    address_contract = web3.Web3.toChecksumAddress(address_contract)


    with open('abi.json') as f:
        abi = json.load(f)

    contract = webber.eth.contract(address=address_contract, abi = abi)

    def __init__(self):
        pass

    def accounts(self):
        return self.webber.eth.accounts

    def getBalance(self, address :str):
        address = web3.Web3.toChecksumAddress(address)
        return self.webber.eth.getBalance(address)

#---Регистрация и авторизация---------------------------------------------------------------------------------------

#---Данные о пользователях------------------------------------------------------------------------------------------
    def setSimpleUser(self, name : str, your_address : str):
        self.contract.functions.setSimpleUser(name).transact({'from':str(your_address)})

    def setPersonUser(self,address: str, name: str, role: int, your_address: str):
        address = web3.Web3.toChecksumAddress(address)
        self.contract.functions.setPersonUser(address, name, role).transact({'from': your_address})

    def getUser(self, address:str):
        address = web3.Web3.toChecksumAddress(address)
        return self.contract.functions.getUser(address).call()

    def getUserRole(self, address:str):
        address = web3.Web3.toChecksumAddress(address)
        return self.contract.functions.getUserRole(address).call()
#-------------------------------------------------------------------------------------------------------------------

#----Данные о автобусах---------------------------------------------------------------------------------------------
    def setBus(self, number : int, sost : bool, kolvoMest: int, your_address : str):
        self.contract.functions.setBus(number, sost, kolvoMest).transact({'from': your_address})

    def getSostBus(self, number: int, your_address : str):
        sost = self.contract.functions.getSostBus(number).call({'from': your_address})
        print(sost)
        return sost

    def setSostBus(self, number : int, sost : bool, your_address : str):
        self.contract.functions.setSostBus(number, sost).transact({'from': your_address})

#-------------------------------------------------------------------------------------------------------------------

#----Информация о поездке-------------------------------------------------------------------------------------------
    def setTrip(self, numTrip : int, punktA: str, punktB : str, prise : int, numBus: int, your_address : str):
        self.contract.functions.setTrip(numTrip, punktA, punktB, prise, numBus).transact({'from': your_address})

    def getInfoOfTrip(self, numTrip : int):
        return self.contract.functions.getInfoOfTrip(numTrip).call()

    def getTripPrise(self, numTrip : int):#, your_address : str):
        return self.contract.functions.getTripPrise(numTrip).call()

    def getPeopleInTrip(self, numTrip : int, your_address : str):
        return self.contract.functions.getPeopleInTrip(numTrip).call({'from': your_address})

#-------------------------------------------------------------------------------------------------------------------



#----Финансовая часть-----------------------------------------------------------------------------------------------

    def addUserInTrip(self, numTrip: int, your_address : str):
        return self.contract.functions.addUserInTrip(numTrip).transact({'from': your_address})

    def pay(self, money:str, your_address : str):
        return self.contract.functions.pay().transact({'from': your_address, 'value': str(money)})

    def moneyHome(self, your_address : str):
        return self.contract.functions.moneyHome().call({'from': your_address})
#-------------------------------------------------------------------------------------------------------------------


ob = Smart()

#
# ob.setSimpleUser('Vitaly','0x44D42f5769f71444d8Fac345Fd14d12cC3cecB4a')
# print(ob.getUser('0x44D42f5769f71444d8Fac345Fd14d12cC3cecB4a','0x44D42f5769f71444d8Fac345Fd14d12cC3cecB4a'))
# try:
#     acc = ob.accounts()
#     print(acc[0])
#     a = acc[0]
#     print(ob.getBalance(a))
    # ob.setSimpleUser('leha', '0x1766cCE8b60f7967CAB8521131cB4AC4A539eB51')


#----Проверка пользователей
# ob.setSimpleUser('Alisa', '0xbd38eec83f594eb07067459a95Ee9b6C841fC848')
# print(ob.getUser('0xbd38eec83f594eb07067459a95Ee9b6C841fC848'))
    #
    # print("Имя админа: ", ob.getUser('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
    # print("Роль админа: ", ob.getUserRole('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
    # try:
    # # ошибка доступа
    #     ob.setPersonUser('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8', 'Sanya', 2, '0xBFdfB7684b9f00b972cFde3a8003C7776E1a6C86')
    #     print(ob.getUser('0xBFdfB7684b9f00b972cFde3a8003C7776E1a6C86'))
    # except:
    #     print('ошибка доступа')
    # print("Ну ошибка")
    # print("Имя админа: ", ob.getUser('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
    # print("Роль админа: ", ob.getUserRole('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
    #
    # ob.setPersonUser('0xBFdfB7684b9f00b972cFde3a8003C7776E1a6C86', 'Sanya', 2, '0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8')
    # print(ob.getUser('0xBFdfB7684b9f00b972cFde3a8003C7776E1a6C86'))
    #
    # print("Имя админа: ", ob.getUser('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
    # print("Роль админа: ", ob.getUserRole('0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))

#----Проверка автобусов
# ob.setBus(2134, False, 100, "0x866B1529537e4176117fBEDD188231681533Bda9")
# print(ob.getSostBus(2134, "0x866B1529537e4176117fBEDD188231681533Bda9"))

#     print(ob.getPeopleInTrip(1234, '0xDB5208C94315DAC8cF0aE0Cf73F79DBD3d2c09C8'))
#
# except:
#     print("Ну ошибка")