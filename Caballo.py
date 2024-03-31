import tkinter as tk
import time
import winsound

def play_tick_sound():
    winsound.Beep(2000, 100)  # Reproduce un tono de 1000 Hz durante 100 ms

def matrix_to_vector(matrix):
    vector = []
    for row in matrix:
        vector.extend(row)
    return vector

def is_valid_move(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def get_possible_moves(x, y, board, n):
    moves = [(x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)]
    valid_moves = []
    for move in moves:
        if is_valid_move(move[0], move[1], board, n):
            valid_moves.append(move)
    return valid_moves

def solve_knight_tour(n, start_x, start_y):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_count = 0
    x, y = start_x, start_y
    board[x][y] = move_count

    while move_count < n * n - 1:
        possible_moves = get_possible_moves(x, y, board, n)
        if not possible_moves:
            break
        
        # Heuristic: Choose the move with the fewest next moves.
        possible_moves.sort(key=lambda move: len(get_possible_moves(move[0], move[1], board, n)))
        
        x, y = possible_moves[0]
        move_count += 1
        board[x][y] = move_count

    return board

def fill_cells(root, cells_to_fill, vector_solution, index, a):
    if index >= len(cells_to_fill):
        return
    b = str(a-1)
    row, col, label = cells_to_fill[index]
    if int(a) < 11:
        b = "0" + b
    label.config(text=b, fg="gray")  # Cambiar el texto y el color
    i=0
    for i, value in enumerate(vector_solution):
        if(vector_solution[i]==a):
            x=i     
    play_tick_sound()
    root.after(300, fill_cells, root, cells_to_fill, vector_solution, x ,a+1)
    

def create_chess_board(root, size):
    cells_to_fill = []
    colors = ["white", "black"]
   
    for row in range(size):
        for col in range(size):
            color = colors[(row + col) % 2]
            frame = tk.Frame(root, width=5000, height=5000, bg=color, )
            frame.grid(row=row, column=col+1)
            
            label = tk.Label(frame, text="    ", font=("Helvetica", 24), bg=color,  fg="gray")
            label.pack(fill="both", expand=True)
            
            cells_to_fill.append((row, col, label))
            
            
    # Agregar un cuadro de texto a la derecha
    for columna_izquierda in range(size):
        texto_de_la_columna = tk.Frame()
        aux=8-columna_izquierda
        texto_de_la_columna.grid(row=columna_izquierda, column=0)  # Coloca el cuadro de texto a la izquierda
        text_label = tk.Label(texto_de_la_columna, text=" "+str(aux)+" ", font=("Arial", 20))
        text_label.grid(row=0, column=0)
        
    # Agregar las coordenadas abajo

    for fila_arriba in range(size):
        texto_de_la_columna = tk.Frame()
        aux=chr(65+fila_arriba)
        texto_de_la_columna.grid(row=size, column=fila_arriba+1)  # Coloca el cuadro de texto arriba
        text_label = tk.Label(texto_de_la_columna, text=str(aux), font=("Arial", 20))
        text_label.grid(row=0, column=0)
            
    # Agregar un cuadro de texto abajo

    text_frame = tk.Frame()
    text_frame.grid(row=size+1, columnspan=size+1)
    texto_Inferior = "Los números que aparecen a continuación indican la ubicación y el número de la jugada efectuada por la pieza de caballo."
    text_label = tk.Label(text_frame, text=texto_Inferior, font=("Arial", 12), wraplength=350)
    text_label.pack()
    
    
    solution = solve_knight_tour(8, 0, 0)
    vector_solution = matrix_to_vector(solution)
    
    fill_cells(root, cells_to_fill,  vector_solution, 0, 1)
                        
def main():
    juego = tk.Tk()
    juego.title("Juego de ajedrez")
    
    tamanoTablero = 8  # Tamaño del tablero n x n
    create_chess_board(juego, tamanoTablero)
    juego.mainloop()

if __name__ == "__main__":
    main()
