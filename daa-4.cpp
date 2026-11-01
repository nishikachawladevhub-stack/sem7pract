
// # practical 4 0/1 Knapsack using Dynamic Programming


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;

    vector<int> weight(n), profit(n);

    // Input item weights and profits
    for (int i = 0; i < n; i++) {
        cout << "Enter weight and profit of item "
             << i + 1 << ": ";
        cin >> weight[i] >> profit[i];
    }

    // Input knapsack capacity
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Create DP table initialized with zeros
    vector<vector<int>> dp(
        n + 1, vector<int>(capacity + 1, 0)
    );

    // Fill DP table
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {

            // Exclude current item
            dp[i][w] = dp[i - 1][w];

            // Include current item if it fits
            if (weight[i - 1] <= w) {
                dp[i][w] = max(
                    dp[i][w],
                    profit[i - 1] +
                    dp[i - 1][w - weight[i - 1]]
                );
            }
        }
    }

    // Display maximum profit
    cout << "\nMaximum Profit: "
         << dp[n][capacity] << endl;

    // Find selected items
    cout << "Selected Items: ";

    int w = capacity;

    for (int i = n; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << i << " ";
            w -= weight[i - 1];
        }
    }

    cout << endl;

    return 0;
}

// sample input 

// Enter number of items: 3
// Enter weight and profit of item 1: 10 60
// Enter weight and profit of item 2: 20 100
// Enter weight and profit of item 3: 30 120
// Enter knapsack capacity: 50



// python code 

// # 0/1 Knapsack using Dynamic Programming

// # Read number of items
// n = int(input("Enter number of items: "))

// weight = []
// profit = []

// # Input item weights and profits
// for i in range(n):
//     w, p = map(
//         int,
//         input(f"Enter weight and profit of item {i + 1}: ").split()
//     )

//     weight.append(w)
//     profit.append(p)

// # Read knapsack capacity
// capacity = int(input("Enter knapsack capacity: "))

// # Create DP table
// dp = [[0] * (capacity + 1) for _ in range(n + 1)]

// # Fill DP table
// for i in range(1, n + 1):
//     for w in range(capacity + 1):

//         # Exclude current item
//         dp[i][w] = dp[i - 1][w]

//         # Include current item if it fits
//         if weight[i - 1] <= w:
//             dp[i][w] = max(
//                 dp[i][w],
//                 profit[i - 1] + dp[i - 1][w - weight[i - 1]]
//             )

// # Display maximum profit
// print("\nMaximum Profit:", dp[n][capacity])

// # Find selected items
// print("Selected Items:", end=" ")

// w = capacity

// for i in range(n, 0, -1):
//     if dp[i][w] != dp[i - 1][w]:
//         print(i, end=" ")
//         w -= weight[i - 1]

// print()
