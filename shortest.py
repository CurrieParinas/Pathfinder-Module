import tkinter as tk
from tkinter import messagebox
from queue import PriorityQueue

class Cell:
    def __init__(self, x, y):
        self.reset(x, y)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.state = "empty"  # Can be "empty", "obstacle", "portal_entry", "portal_exit"
        self.parent = None
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')
        self.portal_partner = None

    def __lt__(self, other):
        return self.f < other.f

    def is_walkable(self):
        return self.state not in ["obstacle"]

class GridWithAStar:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(x, y) for y in range(cols)] for x in range(rows)]
        self.start = None
        self.end = None
        self.portals = []
        self.init_gui()

    def init_gui(self):
        self.canvas = tk.Canvas(self.master, width=self.cols*20, height=self.rows*20)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart)
        self.restart_button.pack()
        self.find_path_button = tk.Button(self.master, text="Find Path", command=self.a_star_search)
        self.find_path_button.pack()
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for x in range(self.rows):
            for y in range(self.cols):
                cell = self.cells[x][y]
                color = "white"
                if cell.state == "obstacle":
                    color = "black"
                elif cell == self.start:
                    color = "green"
                elif cell == self.end:
                    color = "red"
                elif cell.state == "portal_entry":
                    color = "orange"
                elif cell.state == "portal_exit":
                    color = "purple"
                self.canvas.create_rectangle(y*20, x*20, y*20+20, x*20+20, fill=color, outline="gray")

    def on_canvas_click(self, event):
        x, y = event.y // 20, event.x // 20
        cell = self.cells[x][y]
        if cell == self.start:
            self.start = None
        elif cell == self.end:
            self.end = None
        elif cell.state == "empty":
            if not self.start:
                self.start = cell
            elif not self.end:
                self.end = cell
            else:
                cell.state = "obstacle"
        elif cell.state == "obstacle":
            cell.state = "portal_entry"
            self.portals.append(cell)
        elif cell.state == "portal_entry":
            cell.state = "portal_exit"
            # Link the last two portal cells as partners
            if len(self.portals) % 2 == 0:
                entry, exit = self.portals[-2], self.portals[-1]
                entry.portal_partner = exit
                exit.portal_partner = entry
        elif cell.state == "portal_exit":
            cell.state = "empty"
        self.draw_grid()


    def heuristic(self, cell):
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def find_neighbors(self, cell, use_portals):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = cell.x + dx, cell.y + dy
            if 0 <= x < self.rows and 0 <= y < self.cols:
                neighbor = self.cells[x][y]
                if neighbor.is_walkable():
                    neighbors.append(neighbor)
            if use_portals and cell.state == "portal_entry" and cell.portal_partner is not None:
                neighbors.append(cell.portal_partner)
        return neighbors

    
    def reconstruct_path(self, current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        path.append(self.start)
        path.reverse()
        for cell in path:
            if cell.state not in ["start", "end"]:
                self.canvas.create_rectangle(cell.y*20, cell.x*20, cell.y*20+20, cell.x*20+20, fill="blue", outline="gray")

    def a_star_search(self, use_portals=True):
        if not self.start or not self.end:
            messagebox.showinfo("Pathfinder", "Please designate a start and an end point.")
            return

        open_set = PriorityQueue()
        closed_set = set()
        self.start.g = 0
        self.start.h = self.heuristic(self.start)
        self.start.f = self.start.h
        open_set.put((self.start.f, self.start))

        while not open_set.empty():
            current = open_set.get()[1]
            closed_set.add(current)

            if current == self.end:
                self.reconstruct_path(current)
                return

            for neighbor in self.find_neighbors(current, use_portals):
                if neighbor in closed_set:
                    continue
                # Check if the neighbor is a portal exit
                if use_portals and current.state == "portal_entry" and current.portal_partner is neighbor:
                    tentative_g_score = current.g + 0.1
                    neighbor.parent = current
                else:
                    tentative_g_score = current.g + 1

                if tentative_g_score < neighbor.g:
                    neighbor.parent = current
                    neighbor.g = tentative_g_score
                    neighbor.h = self.heuristic(neighbor)
                    neighbor.f = neighbor.g + neighbor.h
                    open_set.put((neighbor.f, neighbor))

        messagebox.showinfo("Pathfinder", "No path found.")

    def restart(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.cells[x][y].reset(x, y)
        self.start = None
        self.end = None
        self.portals = []
        self.draw_grid()

def main():
    root = tk.Tk()
    grid = GridWithAStar(root, 20, 30)  # Example grid size
    root.mainloop()

if __name__ == "__main__":
    main()
