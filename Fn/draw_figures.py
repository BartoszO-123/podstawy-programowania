import figures
import turtle

# Konfiguracja ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")


mover = turtle.Turtle()
mover.speed(0)
mover.penup()

# Ustawienia rozmiarów
SIDE = 70
LONG_A = 120
SHORT_B = 60

## Rysowanie figur w różnych miejscach

# --- 1. KWADRATY ---
# Kwadrat 1 (Start)
mover.goto(-200, 150)
mover.pendown()  # Ustaw żółwia do rysowania
figures.draw_square(SIDE)
mover.penup()  # Podnieś żółwia, by przenieść bez rysowania

# Kwadrat 2 (Drugie miejsce)
mover.goto(100, 150)
mover.pendown()
figures.draw_square(SIDE)
mover.penup()

# --- 2. TRÓJKĄTY ---
# Trójkąt 1
mover.goto(-200, 0)
mover.pendown()
figures.draw_trangle(SIDE)
mover.penup()

# Trójkąt 2
mover.goto(100, 0)
mover.pendown()
figures.draw_trangle(SIDE)
mover.penup()

# --- 3. PROSTOKĄTY ---
# Prostokąt 1
mover.goto(-200, -150)
mover.pendown()
figures.draw_rectangle(LONG_A, SHORT_B)
mover.penup()

# Prostokąt 2
mover.goto(100, -150)
mover.pendown()
figures.draw_rectangle(LONG_A, SHORT_B)
mover.penup()


# Ukrycie żółwia i zakończenie
mover.hideturtle()
window.mainloop()
