
// Job Sequencing with Deadlines using Greedy Method

#include <iostream>
#include <algorithm>
using namespace std;

// Structure to store job details
struct Job {
    char id;
    int deadline;
    int profit;
};

// Sort jobs according to descending profit
bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int main() {
    int n;

    cout << "Enter number of jobs: ";
    cin >> n;

    Job jobs[n];

    // Input job details
    for (int i = 0; i < n; i++) {
        cout << "Enter Job ID, Deadline and Profit: ";
        cin >> jobs[i].id >> jobs[i].deadline >> jobs[i].profit;
    }

    // Sort jobs by profit
    sort(jobs, jobs + n, compare);

    // Find maximum deadline
    int maxDeadline = 0;
    for (int i = 0; i < n; i++) {
        maxDeadline = max(maxDeadline, jobs[i].deadline);
    }

    // Initialize time slots
    char slot[maxDeadline + 1];
    for (int i = 0; i <= maxDeadline; i++) {
        slot[i] = '-';
    }

    int totalProfit = 0;
    int jobCount = 0;

    // Schedule jobs in available slots
    for (int i = 0; i < n; i++) {
        for (int j = min(maxDeadline, jobs[i].deadline); j >= 1; j--) {
            if (slot[j] == '-') {
                slot[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                jobCount++;
                break;
            }
        }
    }

    // Display scheduled jobs
    cout << "\nScheduled Jobs: ";
    for (int i = 1; i <= maxDeadline; i++) {
        if (slot[i] != '-') {
            cout << slot[i] << " ";
        }
    }

    cout << "\nTotal Jobs Scheduled: " << jobCount;
    cout << "\nMaximum Profit: " << totalProfit << endl;

    return 0;
}



// # Job Sequencing with Deadlines using Greedy Method python code 

// # Read number of jobs
// n = int(input("Enter number of jobs: "))

// jobs = []

// # Input job details
// for i in range(n):
//     job_id, deadline, profit = input(
//         "Enter Job ID, Deadline and Profit: "
//     ).split()

//     jobs.append((job_id, int(deadline), int(profit)))

// # Sort jobs by descending profit
// jobs.sort(key=lambda x: x[2], reverse=True)

// # Find maximum deadline
// max_deadline = max((job[1] for job in jobs), default=0)

// # Initialize time slots
// slots = [None] * (max_deadline + 1)

// total_profit = 0
// job_count = 0

// # Schedule jobs in the latest available slot
// for job_id, deadline, profit in jobs:
//     for j in range(min(max_deadline, deadline), 0, -1):
//         if slots[j] is None:
//             slots[j] = job_id
//             total_profit += profit
//             job_count += 1
//             break

// # Display scheduled jobs
// print("\nScheduled Jobs:", end=" ")
// for i in range(1, max_deadline + 1):
//     if slots[i] is not None:
//         print(slots[i], end=" ")

// print("\nTotal Jobs Scheduled:", job_count)
// print("Maximum Profit:", total_profit)


// 
// Enter number of jobs: 5
// Enter Job ID, Deadline and Profit: A 2 100
// Enter Job ID, Deadline and Profit: B 1 19
// Enter Job ID, Deadline and Profit: C 2 27
// Enter Job ID, Deadline and Profit: D 1 25
// Enter Job ID, Deadline and Profit: E 3 15