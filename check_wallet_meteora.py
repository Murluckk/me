def load_wallet_data(file_path):
    wallet_data = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                wallet = parts[0]
                try:
                    amount = float(parts[1])
                    wallet_data[wallet] = amount
                except ValueError:
                    print(f"Ошибка в строке: {line.strip()}")
    return wallet_data

def process_wallets(wallets_file, wallet_data, output_file):
    total_sum = 0
    results = []
    with open(wallets_file, "r", encoding="utf-8") as file:
        wallets = [line.strip() for line in file]
    with open(output_file, "w", encoding="utf-8") as out_file:
        for wallet in wallets:
            amount = wallet_data.get(wallet, 0)
            total_sum += amount
            results.append(f"{wallet} {amount}")
            out_file.write(f"{wallet} {amount}\n")
        out_file.write(f"\nОбщая сумма: {total_sum}\n")
        results.append(f"\nОбщая сумма: {total_sum}")
    return total_sum, results

filtered_file = "2024_filtered.txt" #Закинуть приложенный тхт
wallets_file = "wallets.txt"  #Создать такой тхт со своими кошельками
output_file = "results.txt"

wallet_data = load_wallet_data(filtered_file)
total_sum, results = process_wallets(wallets_file, wallet_data, output_file)

for result in results:
    print(result)