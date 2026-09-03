def create_file():
    file = open("transactions.txt", "w")
    file.write("Deposit,5000\n")
    file.write("Withdrawal,1500\n")
    file.write("Deposit,3000\n")
    file.write("Withdrawal,1000\n")
    file.write("Deposit,2000\n")
    file.close()


def calculate_transactions():
    file = open("transactions.txt", "r")

    total_deposits = 0
    total_withdrawals = 0
    largest = 0

    for line in file:
        data = line.strip().split(",")
        transaction = data[0]
        amount = int(data[1])

        if transaction == "Deposit":
            total_deposits += amount
        else:
            total_withdrawals += amount

        if amount > largest:
            largest = amount

    file.close()

    final_balance = total_deposits - total_withdrawals

    print("Total Deposits:", total_deposits)
    print("Total Withdrawals:", total_withdrawals)
    print("Final Balance:", final_balance)
    print("Largest Transaction:", largest)


create_file()
calculate_transactions()