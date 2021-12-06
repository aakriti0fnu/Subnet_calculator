# Subnet_calculator

**Introduction**: This is a subnet calculator program, which is created to fulfill Class B subnet requests. It is designed to cater the requirement for multiple custormers.

**Note**: You can choose multiple customer and enter the number of hosts corresponding to each customer.
For ex: if you choose 3 customers, you will get the subnet address for all 3 customers and you could choose different number of hosts for different customers.
You have to enter Network Id and Number of hosts seprately for separate customer.

## How To Run

- Clone the github repo `https://github.com/aakriti0fnu/Subnet_calculator.git`
- in the project directory run --> python3 Subnet_App.py



**To demonstrate**:

`Enter number of customers`: 2

Customer number =
 1

`Enter a valid network address:` 172.168.0.0

`Enter number of hosts required by customer`: 56

Number of Network bits = N =  16

Number of Host bits = H =  6

Number of Subnet bits = S =  10

First subnet Network ID =  172.168.0.0

First subnet Broadcast ID =  172.168.0.63

Customer number =
 2

`Enter a valid network address:` 152.135.0.0

`Enter number of hosts required by customer:` 300

Number of Network bits = N =  16

Number of Host bits = H =  9

Number of Subnet bits = S =  7

First subnet Network ID =  152.135.0.0

First subnet Broadcast ID =  152.135.1.255

-------------------------------------------

### How to run the program

- run `python Subnet_App.py`
- On the prompt of `Customer number =` Enter the number of customers(not hosts) you want to allocate hosts

- On the prompt of `Enter a valid network address:`  enter a valid Class B network ID to proceed. It should be within range`(128.0.0.0 - 191.255.0.0)`

- On the prompt of `Enter number of hosts required by customer: ` , enter the number of hosts you want for your customer

- Now you will get the following details for your selected choice

    - `Number of Network bits = N =` 

   - `Number of Host bits = H = `

   - `Number of Subnet bits = S =` 

   - `First subnet Network ID = `

    - `First subnet Broadcast ID = ` 

### Team Members
- Aakriti Aakriti
- Ashwin kumar Munniswamy