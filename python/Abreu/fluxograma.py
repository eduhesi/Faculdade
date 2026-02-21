import graphviz as a

# Creating a directed graph for the process flowchart
flowchart = a.Digraph(format="png")
flowchart.attr(rankdir="TB", size="10,10")

# Adding nodes and edges for each step in the process
flowchart.node("A", "Start")
flowchart.node("B", "Mix activator solution\n(NaOH + Na₂SiO₃)\nfor 5 minutes")
flowchart.node("C", "Add solution to metakaolin\nand mix for 10 minutes")
flowchart.node("D", "Pause mixing at 5 minutes\nand stir manually for 1 minute")
flowchart.node("E", "Resume mechanical mixing\nfor remaining 5 minutes")
flowchart.node("F", "Add aluminum powder\nand mix for 2 minutes")
flowchart.node("G", "Add fibers and mix\nfor final 2 minutes")
flowchart.node("H", "End")

# Defining the connections between the nodes
flowchart.edge("A", "B")
flowchart.edge("B", "C")
flowchart.edge("C", "D")
flowchart.edge("D", "E")
flowchart.edge("E", "F")
flowchart.edge("F", "G")
flowchart.edge("G", "H")

# Render the flowchart and display the file path
flowchart_file_path = './fluxogram_process.png'
flowchart.render(filename=flowchart_file_path, cleanup=False)
flowchart_file_path