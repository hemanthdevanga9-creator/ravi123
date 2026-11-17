'''def create_stack():
    stack = []
    return stack
def check_empty(stack):
    return len(stack) == 0
def push(stack, data):
    stack.append(data)
    print("Pushed items are:", data)
def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()
stack = create_stack()
push(stack, 30)
push(stack, 90)
push(stack, 70)
print("Popped item is:", pop(stack))
print("Stack after popping:", stack)'''


graph = {'A': ['B', 'D', 'E', 'F'], 'D': ['A'], 'B': ['A', 'F', 'C'], 'F': ['B', 'A'], 'C': ['B'], 'E': ['A']}

print("Given graph is :",graph)
def dfs_traverse(input_graph, source):
    stack = []
    visited_list = []
    stack.append(source)
    visited_list.append(source)
    print("DFS traversal of graph with source:", source, "is:")
    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for neighbour in input_graph[vertex]:
            if neighbour not in visited_list:
                stack.append(neighbour)
                visited_list.append(neighbour)
dfs_traverse(graph, "A")
