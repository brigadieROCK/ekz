//це мое
pragma solidity ^0.8.0;


contract SimpleContract 
{

    constructor(string memory name)
    {
        uint balance = 0;
        address owner = msg.sender;
        massOfUsers[msg.sender].role = 4;
        massOfUsers[msg.sender].userName = name;
    }
//Roles
// Admin = 4
// Ingeneer = 1
// Driver = 2
// Conductor = 3
// SimpleUser = 0
//
    struct User
    {
        string userName;
        uint role;
        uint balance;
    }

    struct Bus
    {
        uint number;
        bool condition;
        uint kolvoMest;
    }

    struct Trip
    {
        string punktA;
        string punktB;
        uint prise;
        uint numBus; 
        address []massUsers;
    }

    mapping (uint => Trip) massOfTrip; //все поездки
    mapping (address => User) massOfUsers;//все пользователи
    mapping (uint => Bus) massOfBus;//все абобусы
//----------МОДИФИКАТОРЫ(ну прикольные ребята, мне понравились)---------------------------------
    modifier OnlyAdmin
    {
        require(massOfUsers[msg.sender].role == 4, "Access denie");
        _;
    }

    modifier BusInfo
    {
        bool flag = false;
        if(massOfUsers[msg.sender].role == 1)
        {
            flag = true;
        }
        if(massOfUsers[msg.sender].role == 4)
        {
            flag = true;
        }
        require(flag, "Access denie");
        _;
    }

    modifier TripInfo
    {
        bool flag = false;
        if(massOfUsers[msg.sender].role == 1)
        {
            flag = true;
        }
        if(massOfUsers[msg.sender].role == 3)
        {
            flag = true;
        }
        if(massOfUsers[msg.sender].role == 4)
        {
            flag = true;
        }
        require(flag, "Access denie");
        _;
    }

//----------------------------------------------------------------------------------------------
    //сложение строк на вход две строки, на выход одна из двух разделенных пробелом
    function concat(string memory a, string memory b) internal returns (string memory) 
    {
        uint i;
        uint j = 0;
        string memory newValue = new string(bytes(a).length + bytes(b).length + 1);
        bytes memory value = bytes(newValue);
        bytes memory str1 = bytes(a);
        bytes memory str2 = bytes(b);
        for(i=0; i<str1.length; i++) 
        {
            value[j] = str1[i];
            j++;
        }
        value[j] = bytes(" ")[0];
        j++;
        for(i=0; i<str2.length; i++) 
        {
            value[j] = str2[i];
            j++;
        }
            return string(newValue);
    }

    
//------РАБОТА С  ДАННЫМИ О ПОЛЬЗОВАТЕЛЕ----------------------------------------------------
    function setSimpleUser(string memory us) public
    {
            massOfUsers[msg.sender].userName = us;
    }

    function setPersonUser(address rab, string memory us, uint r) OnlyAdmin public
    {
            massOfUsers[rab].userName = us;
            massOfUsers[rab].role = r;
    }

    function getUser(address addr) public returns(string memory)
    {
        if(keccak256(abi.encodePacked(massOfUsers[addr].userName)) != keccak256(abi.encodePacked("")))
        {
            return massOfUsers[addr].userName;
        }
        else
        {
            return "Nemae";
        }
    }

    function getUserRole(address addr) public returns(uint)
    {
        if(keccak256(abi.encodePacked(massOfUsers[addr].userName)) != keccak256(abi.encodePacked("")))
        {
            return massOfUsers[addr].role;
        }
        else
        {
            return 5;
        }
    }

//------------------------------------------------------------------------------------------

//------------------------------------------------------------------------------------------
    function setBus(uint num, bool cond,uint kM) public OnlyAdmin
    {
        Bus memory a;
        a.number = num;
        a.condition = cond;
        a.kolvoMest = kM;
        massOfBus[num] = a;
    }

    function getSostBus(uint num) public BusInfo returns(bool) 
    {
        if(massOfBus[num].condition == true)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    function setSostBus(uint num, bool cond) public BusInfo
    {
        massOfBus[num].condition = cond;
    }

//------СОЗДАНИЕ ПОЕЗДКИ---------------------------------------------------------------------
    function setTrip(uint numTrip, string memory A, string memory B, uint prs, uint bus) public OnlyAdmin
    {
        Trip memory a;
        a.punktA = A;
        a.punktB = B;
        a.prise = prs;
        a.numBus = bus;
        massOfTrip[numTrip] = a;
    }

    function getInfoOfTrip(uint numTrip) public TripInfo returns(string memory) 
    {
        return concat(massOfTrip[numTrip].punktA, massOfTrip[numTrip].punktB);
    }

    function getTripPrise(uint numTrip) public returns(uint) 
    {
        return massOfTrip[numTrip].prise;
    }
    
    function getPeopleInTrip(uint numTrip) public TripInfo returns(address [] memory)
    {
        return massOfTrip[numTrip].massUsers;
    }
//------------------------------------------------------------------------------------------

//------ОПЛАТА БИЛЕТА-----------------------------------------------------------------------
    function addUserInTrip(uint numTrip) public returns(bool)
    {
        if(massOfUsers[msg.sender].balance - massOfTrip[numTrip].prise >= 0)
        {
            massOfTrip[numTrip].massUsers.push(msg.sender);
            massOfUsers[msg.sender].balance = massOfUsers[msg.sender].balance - massOfTrip[numTrip].prise;
            return true;
        }
        else
        {
            return false;
        }
    }

    function pay() external payable
    {
        massOfUsers[msg.sender].balance = massOfUsers[msg.sender].balance + msg.value;
    }

    function getBalance() public returns(uint)
    {
        return massOfUsers[msg.sender].balance;
    }

    function moneyHome() OnlyAdmin external payable
    {
        payable(msg.sender).transfer(address(this).balance);
    }
    
//------------------------------------------------------------------------------------------    
//      варианты поездок
//      1, a, b, 50000000, 1234
//      1, a, b, 50000, 1234
//      1, a, b, 50000, 1234


//      Учетки
//      Vasya, Pupkin, 0
//      Sashka,EkarniyBabay,2
//      Nail, Shawkyatovich, 1
//      Galina, Ivanovna, 3

//      абобусы
//      117, 1, 12300
//      19, 0, 13
//      1,1,1
//      123, 1,20
//      


}