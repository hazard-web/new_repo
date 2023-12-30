class Employee:
    #Write the code here
    
    def __intit__(self,name,year,address):
        self.name = name
        self.year = year
        self.address = address

        
    

#Do Not change the Below code Method


def main():
    t=Employee("ram",1992,"Bangalore");
    t.print_details();
    
    x=Employee("shyam",2010,"Lucknow");
    x.print_details();
    
    y=Employee("babu_rao",2015,"Delhi");
    y.print_details();
main()

from calendar import*

year = int(input("Enter the year: "))
print(calendar(year))


print("20" + "23" + "5000")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return len(self.items) == 0

    def get_first_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. No first element to retrieve.")

#     def size(self):
#         return len(self.items)

# Example usage of the Queue class:
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue elements:", my_queue.items)

first_element = my_queue.get_first_element()
print("First element:", first_element)

dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)

print("Updated queue elements:", my_queue.items)

print("Is the queue empty?", my_queue.is_empty())



def calculate_sum_recursive(i, n, current_sum):
    if i >= 11 or i == n:
        return current_sum  # Base case: return the current sum when i is greater than or equal to 11 or i is equal to n

    current_sum += i
    print(current_sum)  # Print the current sum at each step (remove this line if you want to print only the final sum)
    
    return calculate_sum_recursive(i + 2, n, current_sum)  # Recursive case: add i to the sum of the rest of the sequence

# Initial values
sum_result = calculate_sum_recursive(1, 6, 0)
print("Final Sum:", sum_result)

def get_permutations(s):
    result = []
    generate_permutations(s, "", result)
    return result

def generate_permutations(remaining, current, result):
    if not remaining:
        result.append(current)
        return

    for i in range(len(remaining)):
        new_current = current + remaining[i]
        new_remaining = remaining[:i] + remaining[i+1:]
        generate_permutations(new_remaining, new_current, result)

# Example usage
input_string = "abc"
permutations_list = get_permutations(input_string)

print(f"Permutations for {input_string}:")
for permutation in permutations_list:
    print(permutation)


def print_all_subsequences(arr, current, index):
    if index == len(arr):
        print(current)
        return

   
    print_all_subsequences(arr, current + [arr[index]], index + 1)

    
    print_all_subsequences(arr, current, index + 1)

# Example usage
input_array = [1, 2, 3]

print("All Subsequences:")
print_all_subsequences(input_array, [], 0)



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Function to sort employees by salary in descending order
def sort_employees_by_salary_descending(employees):
    return sorted(employees, key=lambda x: x.salary, reverse=True)

# Create 5 Employee objects with random values
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
employee3 = Employee("Charlie", 45000)
employee4 = Employee("David", 70000)
employee5 = Employee("Eva", 55000)

# Store the objects in an array
employees_array = [employee1, employee2, employee3, employee4, employee5]

# Sort the employees based on salary in descending order
sorted_employees = sort_employees_by_salary_descending(employees_array)

# Print the names of employees in sorted order
print("Names of Employees Sorted by Salary (Descending Order):")
for employee in sorted_employees:
    print(employee.name)


def find_vlaues(s):
    n = len(s)

    for i in range(1,n):
        a_str = s[:i]
        b_str = s[i:]
        a,b = int(a_str), int(b_str)


        if a>0 and b>0 and b>a and str(a) + str(b) == s:
            return a,b
          
        return -1,-1

def solve_testcase(t,testcases):
    results = []

    for i in range(t):
        s = testcases[i]
        a, b = find_vlaues(s)
        results.append((a,b))

    return results 

if __name__ == "__main__":
    t = int(input())
    testcases = [input().strip() for _ in range(t)]

    results = solve_testcase(t, testcases)

    for a, b in results:
        if  a == -1:
            print(-1)
        else:
            print(f"{a} {b}")





















def min_cost_to_make_good(t, testcases):
    results = []
    for i in range(t):
        s = testcases[i]
        n = len(s)


        count_0 = s.count('0')
        count_1 = n - count_0

  
        cost = min(count_0, count_1)

        results.append(cost)

    return results

if __name__ == "__main__":
    t = int(input())
    testcases = [input().strip() for _ in range(t)]

    results = min_cost_to_make_good(t, testcases)

    for result in results:
        print(result)



def process_queries(m, queries):
    multiset = set()
    total_sum = 0

    results = []

    for i in range(m):
        t, v = queries[i]

        if t == 1:
            multiset.add(2 * v)
            total_sum += 2 * v
        else:
            if v == 0 or v % 2 == 1 or v > total_sum or (v % 2 == 0 and v // 2 not in multiset):
                results.append("NO")
            else:
                results.append("YES")

    return results

if __name__ == "__main__":
    m = int(input())
    queries = [list(map(int, input().split())) for _ in range(m)]

    results = process_queries(m, queries)

    for result in results:
        print(result)




MOD = 998244353

def count_reachable_arrays(t, test_cases):
    results = []

    for i in range(t):
        n, p = test_cases[i]

     
        result = 1

    
        stack = []

 
        for j in range(n):
            while stack and p[j] < p[stack[-1]]:
             
                stack.pop()

            if stack:
            
                result = (result * (j - stack[-1] + 1)) % MOD
            else:
             
                result = (result * (j + 1)) % MOD

    
            stack.append(j)

        results.append(result)

    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []

    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        test_cases.append((n, p))

    results = count_reachable_arrays(t, test_cases)

    for result in results:
        print(result)


def solve(n, m, matrix, target_row, target_col):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(m)]

    operations = 0

    for i in range(n):
        if row_sums[i] > target_row[i]:
            operations += row_sums[i] - target_row[i]

    for j in range(m):
        if col_sums[j] > target_col[j]:
            operations += col_sums[j] - target_col[j]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and row_sums[i] > target_row[i] and col_sums[j] > target_col[j]:
                operations -= 1
                row_sums[i] -= 1
                col_sums[j] -= 1

    for i in range(n):
        if row_sums[i] < target_row[i]:
            return -1

    for j in range(m):
        if col_sums[j] < target_col[j]:
            return -1

    return operations


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    target_row = list(map(int, input().split()))
    target_col = list(map(int, input().split()))

    result = solve(n, m, matrix, target_row, target_col)
    print(result)




def solve(n, s):
    max_palindromes = 0
    result = ""

    for i in range(26):
        char = chr(ord("a") + i)
        modified_string = s.replace(char, "*")

        left_pointer = 0
        right_pointer = n - 1
        palindromes = 0

        while left_pointer <= right_pointer:
            if modified_string[left_pointer] == modified_string[right_pointer]:
                if modified_string[left_pointer] == "*" and left_pointer != right_pointer:
                    palindromes += 25
                elif left_pointer == right_pointer:
                    palindromes += 1
            elif modified_string[left_pointer] == "*" or modified_string[right_pointer] == "*":
                palindromes += 1
            else:
                break

            left_pointer += 1
            right_pointer -= 1

        if palindromes > max_palindromes:
            max_palindromes = palindromes
            result = modified_string.replace("*", char)

    return max_palindromes, result


if __name__ == "__main__":
    n = int(input())
    s = input().strip()

    max_palindromes, result = solve(n, s)

    print(max_palindromes)
    print(result)



def solve(s):
    n = len(s)
    dp = [[0]*27 for _ in range(n)]
    min_char = 97

    for i in range(n):
        for j in range(27):
            if j == ord(s[i]) - min_char:
                dp[i][j] = 1 + (i >= 1 and dp[i-1][j])
            elif j > ord(s[i]) - min_char:
                dp[i][j] = dp[i][j-1] + (i >= 1 and dp[i-1][j])
            else:
                dp[i][j] = dp[i][j]

    res = ''
    total = 0
    min_total = 0

    for i in range(n-1, -1, -1):
        min_total = float('inf')
        min_char = ord(s[i]) - 97

        for j in range(27):
            if j >= min_char:
                if dp[i][j] < min_total:
                    min_total = dp[i][j]
                    min_char = j + 97

        res = chr(min_char) + res
        total += min_total

    return total, res

def main():
    n = int(input())
    s = input()
    total, res = solve(s)
    print(total)
    print(res)

if __name__ == "__main__":
    main()






def find_values(ab):
    a = 0
    b = 0

    # Find the first non-zero digit of b
    for i in range(len(ab)):
        if ab[i] != '0':
            a = int(ab[:i])
            b = int(ab[i:])
            break

    # If b is all zeros, it is not valid
    if b == 0:
        return -1

    # If a is a single digit and is 0, it is not valid
    if len(str(a)) == 1 and a == 0:
        return -1

    # If b is a single digit and is 0, it is not valid
    if len(str(b)) == 1 and b == 0:
        return -1

    # If a and b are both valid, return them
    return a, b

t = int(input())
for _ in range(t):
    ab = input()
    result = find_values(ab)
    if isinstance(result, tuple):
        print(*result)
    else:
        print(result)


def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

numbers = [20002001, 391125, 200200, 2001000, 12, 5, 20002001, 391125, 200200, 2001000, 12]

for num in numbers:
    print(f"Divisors of {num}: {find_divisors(num)}")


def find_values(ab):
    # Remove trailing zeros from the string ab
    while ab[-1] == '0':
        ab = ab[:-1]

    # Calculate the minimum possible value for a and the maximum possible value for b
    min_a = int('1' + '0' * (len(ab) - 1))
    max_b = int('1' + '0' * len(ab)) - 1

    # Iterate over the possible values of a and b and check if there is a pair that satisfies the conditions a≠b and b>a
    for a in range(min_a, 10**len(ab)):
        for b in range(a+1, max_b+1):
            if str(a) + str(b) == ab:
                return a, b

    # If no such pair is found, return -1
    return -1

t = int(input())
for _ in range(t):
    ab = input()
    print(find_values(ab))








print("We need to understand", "how to print multiple output in a single line")