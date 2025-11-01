#include <pybind11/pybind11.h>
#include <iostream>
#include <vector>
#include <pybind11/stl.h>

std::vector<int> insertion_sort(std::vector<int> arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        for (int j = static_cast<int>(i) - 1; j >= 0; --j) {
            if (arr[j] < arr[j + 1])
                break;
            int temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
    }
    return arr;
}

std::vector<int> selection_sort(std::vector<int> arr) {
    size_t n = arr.size();
    for (size_t i = 0; i < n; ++i) {
        int m = arr[i];
        size_t m_idx = i;
        for (size_t j = i + 1; j < n; ++j) {
            if (arr[j] < m) {
                m = arr[j];
                m_idx = j;
            }
        }
        int temp = arr[m_idx];
        arr[m_idx] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

std::vector<int> quick_sort(std::vector<int> arr) {
    size_t n = arr.size();
    if (n == 0)
        return {};
    if (n == 1)
        return arr;
    if (n == 2)
        return (arr[0] <= arr[1]) ? arr : std::vector<int>{arr[1], arr[0]};

    std::vector<int> left, right, mid;
    int pivot = arr[std::rand() % n];

    for (int x : arr) {
        if (x < pivot)
            left.push_back(x);
        else if (x > pivot)
            right.push_back(x);
        else
            mid.push_back(x);
    }

    if (left.empty()) {
        auto merged = mid;  // copy mid
        auto sorted_right = quick_sort(right);
        merged.insert(merged.end(), sorted_right.begin(), sorted_right.end());
        return merged;
    }

    if (right.empty()) {
        auto sorted_left = quick_sort(left);
        sorted_left.insert(sorted_left.end(), mid.begin(), mid.end());
        return sorted_left;
    }

    std::vector<int> s_left = quick_sort(left);
    std::vector<int> s_right = quick_sort(right);

    std::vector<int> res = s_left;
    res.insert(res.end(), mid.begin(), mid.end());
    res.insert(res.end(), s_right.begin(), s_right.end());
    return res;
}

std::vector<int> merge_sort(std::vector<int> arr) {
    size_t n = arr.size();
    if (n == 1)
        return arr;

    std::vector<int> l(arr.begin() + n / 2, arr.end());
    std::vector<int> r(arr.begin(), arr.begin() + n / 2);
    l = merge_sort(l);
    r = merge_sort(r);
    std::vector<int> res;

    while (true) {
        if (l.empty())
            return [] (auto a, auto b) { a.insert(a.end(), b.begin(), b.end()); return a; }(res, r);
        if (r.empty())
            return [] (auto a, auto b) { a.insert(a.end(), b.begin(), b.end()); return a; }(res, l);

        if (l.front() < r.front()) {
            res.push_back(l.front());
            l.erase(l.begin());
        } else {
            res.push_back(r.front());
            r.erase(r.begin());
        }
    }
}

std::vector<int> counting_sort(const std::vector<int>& arr) {
    if (arr.empty()) return {};

    // Find min and max values in arr
    int minVal = *std::min_element(arr.begin(), arr.end());
    int maxVal = *std::max_element(arr.begin(), arr.end());

    // Create count array to store frequency of each value in range
    std::vector<int> count(maxVal - minVal + 1, 0);

    // Count frequency of each element
    for (int num : arr) {
        count[num - minVal]++;
    }

    // Reconstruct sorted array
    std::vector<int> sorted(arr.size());
    int idx = 0;
    for (int value = minVal; value <= maxVal; ++value) {
        int freq = count[value - minVal];
        for (int i = 0; i < freq; ++i) {
            sorted[idx++] = value;
        }
    }
    return sorted;
}

// Helper function to get digit at specific place
int getDigit(int number, int digitPos) {
    return (number / static_cast<int>(std::pow(10, digitPos))) % 10;
}

std::vector<int> radix_sort(std::vector<int> arr) {
    if (arr.empty()) return {};

    // Find maximum number to know number of digits
    int maxNum = *std::max_element(arr.begin(), arr.end());

    int maxDigits = 0;
    while (maxNum > 0) {
        maxNum /= 10;
        ++maxDigits;
    }

    // Radix sort by each digit from LSD to MSD
    for (int digitPos = 0; digitPos < maxDigits; ++digitPos) {
        // Counting sort on the digit at digitPos

        // Count array for digits 0 to 9
        std::vector<int> count(10, 0);

        // Count occurrences of each digit
        for (int num : arr) {
            int digit = getDigit(num, digitPos);
            count[digit]++;
        }

        // Cumulative count to get positions
        for (int i = 1; i < 10; ++i) {
            count[i] += count[i - 1];
        }

        std::vector<int> output(arr.size());

        // Build output array from right to left for stability
        for (int i = static_cast<int>(arr.size()) - 1; i >= 0; --i) {
            int digit = getDigit(arr[i], digitPos);
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        // Copy the output array to arr for next digit iteration
        arr = output;
    }
    return arr;
}

PYBIND11_MODULE(algorithms, m) {
    m.doc() = "sorting algorithms";
    
    // Expose individual sorting functions
    m.def("insertion_sort", &insertion_sort, "Sort array using insertion_sort");
    m.def("selection_sort", &selection_sort, "Sort array using selection_sort");
    m.def("merge_sort", &merge_sort, "Sort array using merge_sort");
    m.def("quick_sort", &quick_sort, "Sort array using quick_sort");
    m.def("counting_sort", &counting_sort, "Sort array using counting_sort");
    m.def("radix_sort", &radix_sort, "Sort array using radix_sort");

}