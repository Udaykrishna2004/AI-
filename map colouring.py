Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_safe(graph, node, color, coloring):
...     for neighbor in graph[node]:
...         if neighbor in coloring and coloring[neighbor] == color:
...             return False
...     return True
... def map_coloring(graph, colors, coloring, nodes):
...     if not nodes:
...         return True
...     node = nodes[0]
...     for color in colors:
...         if is_safe(graph, node, color, coloring):
...             coloring[node] = color
...             if map_coloring(graph, colors, coloring, nodes[1:]):
...                 return True
...             coloring.pop(node, None)
...     return False
... def main():
...     graph = {
...         'A': ['B', 'C'],
...         'B': ['A', 'C', 'D'],
...         'C': ['A', 'B', 'D', 'E'],
...         'D': ['B', 'C', 'E', 'F'],
...         'E': ['C', 'D'],
...         'F': ['D']
...     }
...     colors = ['Red', 'Green', 'Blue', 'Yellow']
...     coloring = {}
...     nodes = list(graph.keys())
...     if map_coloring(graph, colors, coloring, nodes):
...         print("Map coloring solution:")
...         for node, color in coloring.items():
...             print(f"{node} -> {color}")
...     else:
...         print("No valid coloring found for the map.")
... if __name__ == "__main__":
