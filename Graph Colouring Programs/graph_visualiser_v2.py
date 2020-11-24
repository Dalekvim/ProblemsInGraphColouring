"""
Graph Visualiser
By Vimal Vinod
"""

from command.basic import Graph

print("""
Welcome to Graph Visualiser Version 2.0.0!
Type "help" to know more about how this works.
""")


def main():
    instruction = input(">>> ").lower().split(" ")

    command = instruction[0]
    details = instruction[1:]

    graph = Graph(details)
    commands = ["draw", "colour", "save"]

    if command in commands:
        exec(f"graph.{command}()")
    else:
        print(f'"{command}" is not a valid command.')


while True:
    main()
