a, b = [], []
# a and b are two empty stacks.

for _ in range(int(input())):
    # This loop runs as many times as the first input number.

    val = list(map(int, input().split()))
    # Read a line of input, split by spaces, and convert each part to an integer.

    if val[0] == 1:
        # If the first number in the input is 1, it's an enqueue operation.
        b.append(val[1])
        # Add the second number in the input to stack b.

    elif val[0] == 2:
        # If the first number is 2, it's a dequeue operation.
        if not a:
            # If stack a is empty, transfer all elements from b to a, reversing their order.
            while b:
                a.append(b.pop())
        a.pop()
        # Remove the top element from stack a.

    else:
        # For any other first number in the input, print the front element of the queue.
        if a:
            # If stack a is not empty, its top element is the front of the queue.
            print(a[-1])
        else:
            # If stack a is empty, the bottom element of b is the front of the queue.
            print(b[0])
