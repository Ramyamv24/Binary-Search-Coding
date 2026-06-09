#include <iostream>
#include <set>
using namespace std;

class MyCalendar {
public:
    set<pair<int, int>> bookings;

    bool book(int start, int end) {
        auto it = bookings.lower_bound({start, end});

        // Check overlap with next interval
        if (it != bookings.end() && it->first < end) {
            return false;
        }

        // Check overlap with previous interval
        if (it != bookings.begin()) {
            auto prevIt = prev(it);
            if (prevIt->second > start) {
                return false;
            }
        }

        bookings.insert({start, end});
        return true;
    }
};

int main() {
    MyCalendar cal;

    int n;
    cout << "Enter number of bookings: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        int start, end;
        cout << "Enter start and end time: ";
        cin >> start >> end;

        if (cal.book(start, end))
            cout << "Booking successful\n";
        else
            cout << "Booking failed (overlap)\n";
    }

    return 0;
}