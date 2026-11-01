
// Practical 3 – Fractional Knapsack using Greedy Method

#include <iostream>
#include <algorithm>
using namespace std;

// Structure to store item details
struct Item {
    int weight;
    int profit;
    double ratio;
};

// Sort items by profit-to-weight ratio
bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

int main() {
    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;

    Item items[n];

    // Input item details
    for (int i = 0; i < n; i++) {
        cout << "Enter weight and profit of item " << i + 1 << ": ";
        cin >> items[i].weight >> items[i].profit;

        items[i].ratio =
            (double)items[i].profit / items[i].weight;
    }

    // Input knapsack capacity
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Sort items by profit-to-weight ratio
    sort(items, items + n, compare);

    double totalProfit = 0.0;

    // Fill the knapsack greedily
    for (int i = 0; i < n; i++) {
        if (capacity == 0)
            break;

        if (items[i].weight <= capacity) {
            // Take the complete item
            capacity -= items[i].weight;
            totalProfit += items[i].profit;
        }
        else {
            // Take a fraction of the item
            double fraction =
                (double)capacity / items[i].weight;

            totalProfit += items[i].profit * fraction;
            capacity = 0;
        }
    }

    // Display maximum profit
    cout << "\nMaximum Profit: " << totalProfit << endl;

    return 0;
}

//sample input 
// Enter number of items: 3
// Enter weight and profit of item 1: 10 60
// Enter weight and profit of item 2: 20 100
// Enter weight and profit of item 3: 30 120
// Enter knapsack capacity: 50


// python code 

// # Fractional Knapsack using Greedy Method

// # Read number of items
// n = int(input("Enter number of items: "))

// items = []

// # Input item weights and profits
// for i in range(n):
//     weight, profit = map(
//         int,
//         input(f"Enter weight and profit of item {i + 1}: ").split()
//     )

//     ratio = profit / weight
//     items.append((weight, profit, ratio))

// # Read knapsack capacity
// capacity = int(input("Enter knapsack capacity: "))

// # Sort items by descending profit-to-weight ratio
// items.sort(key=lambda x: x[2], reverse=True)

// total_profit = 0

// # Fill the knapsack greedily
// for weight, profit, ratio in items:
//     if capacity == 0:
//         break

//     if weight <= capacity:
//         # Take the complete item
//         capacity -= weight
//         total_profit += profit
//     else:
//         # Take a fraction of the item
//         fraction = capacity / weight
//         total_profit += profit * fraction
//         capacity = 0

// # Display maximum profit
// print("\nMaximum Profit:", total_profit)

