# lotto_lottery
## Level 1: Lotto Ticket Generator

### Introduction
Level 1 of the project requires to develop a lotto tickets generator: the software will have to generate from 1 to 5 tickets. 
For each ticket, the software will ask: 
- the **amount of numbers** to place and, based on the previous information, will give the user the opportunity to specify **which numbers** to place (each number must be between 1 and 90 and appear once in the sequence). Alternatively, the program will generate random sequences of numbers until the user confirms one.
- the **type of bet** (ambata, ambo, terna, quaterna or cinquina). The bet must be coherent with the chosen amount of numbers. For example, if the user places 3 numbers, the bet choices will be limited to ambata, ambo or terno. If the user places 5 number, he/she will be able to choose whichever bet.
- the **city** of extraction (napoli, firenze, bari, cagliari, venezia, milano, roma, genova, palermo or torino).
Check <https://www.sisal.it/lotto/come-si-gioca> for further information about the rules.

### How to Launch
The entry point *lotto_game.py* script can be launched through command line by specifying the amount of tickets to generate for the `n` argument. For example, writing ***python lotto_game.py 3*** will generate a bill of three tickets. 
After launching the script, the program will start constructing each ticket by asking the user all the information about each ticket.

### Classes and lotto Package
The project is built using an OOP approach.
Several *Classes* were used. All used *Classes* are inside their own *module*, and all modules are inside the **lotto package**.

Three main Classes were created in order to store lotto ticket informations:

* **`NumbersForTicket`**

    it represents a series of numbers which are generated and stored inside a ticket.

* **`BetType`**

    it represents the chosen bet for a specific ticket.

* **`City`** 

    It represents the chosen city for a specific ticket.

All previous Classes have their own validation method.

Another Class was created to build a single ticket object.

* **`Ticket`**

    It represents one single ticket. 
    It has three *attributes* that will correspond to instances of the three previously defined Classes: an object will represent its **numbers**, another one its **bet type** and the last one its **city** of extraction.  

    This Class uses a further validation method that checks the "coherence" of the information that are supposed to build the ticket:
    firstly, the stated amount of numbers must correspond to the amount of numbers that are present inside the chosen sequence (this applies only when numbers are chosen and not randomly generated);
    secondly, the bet type must be coherent with the amount of numbers.

A last Class was created in order to build the *business logic* behind the program:

* **`LottoManager`**
    it represents the *business logic* and stores each `Ticket` object inside its `tickets` attribute.
    An instance of it can be considered as a **Lotto bill** with a series of ticket (even one only) inside it.
    The Class uses a `ticket_creator` method to ask the user all the information about the current ticket, and a `ticket_confirmator` method where the user will have the chance to confirm the constructed ticket or to restart writing it from scratch.

    When the lotto bill is "ready", which means all tickets are constructed and stored inside it, a `bill_printer` method gets invoked. This method will create a dictionary that gathers all the details about all the tickets in one place. Such dictionary will then be passed as argument of the `print_lotto_bill` function, improted from the *lotto_table_lib* module.


    
    When printing an instance of `LottoManager`, its `__str__` method will invoke the `bill_printer` in order to display a **visual representation** of the bill.


### Output
The program is designed to render a **visual representation** of a lotto bill with one or more tickets inside it, after printing
an instance of the `LottoManager` *Class* with the amount of tickets to generate (even one only). It will display all generated tickets (and their details) organized into rows and columns.
