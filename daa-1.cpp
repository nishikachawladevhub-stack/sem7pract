
//practical 1 Fibonacci Series and Step Count

#include <iostream>
using namespace std;

int main() {
    int n;
    int a = 0, b = 1, c;
    int stepCount = 0;

    // Read number of terms
    cout << "Enter the number of terms: ";
    cin >> n;

    // Display Fibonacci series
    cout << "Fibonacci Series: ";

    if (n >= 1)
        cout << a << " ";

    if (n >= 2)
        cout << b << " ";

    // Calculate remaining Fibonacci numbers
    for (int i = 2; i < n; i++) {
        c = a + b;
        cout << c << " ";

        a = b;
        b = c;

        stepCount++; // Count each addition
    }

    // Display step count
    cout << "\nStep Count: " << stepCount << endl;

    return 0;
}



// python code 

// # Fibonacci Series and Step Count

// # Read number of terms
// n = int(input("Enter the number of terms: "))

// a = 0
// b = 1
// step_count = 0

// # Display Fibonacci series
// print("Fibonacci Series:", end=" ")

// if n >= 1:
//     print(a, end=" ")

// if n >= 2:
//     print(b, end=" ")

// # Calculate remaining Fibonacci numbers
// for i in range(2, n):
//     c = a + b
//     print(c, end=" ")

//     a = b
//     b = c

//     step_count += 1  # Count each addition

// # Display step count
// print("\nStep Count:", step_count)
