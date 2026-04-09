import tkinter as tk
import random
import turtle
import math
T=turtle.turtles
class Ruleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta de la Fortuna: Distancia & Intimidad")
        self.root.configure(bg="black")
        
        # 1. Lista ampliada con 15 opciones para parejas (románticas e íntimas)
        self.opciones = [
            "Cena por Videollamada", "Dormir Juntos (Llamada)", "Ver una Peli juntos",
            "penitencia", "Escribir una carta de Amor", "Verdad o Reto Picante",
            "Comprar un Regalo Online", "declaracion en cámara", "Contar una Fantasía",
            "pregunta y respuesta", "Pregunta Íntima", "Snapchat con filtro",
            "Planear la próxima visita", "Mandar un Audio tierno", "hacer algo tierno"
        ]
        
        # Colores variados para las 15 casillas
        self.colores = ["#7C0808", "#33FF57", "#3357FF", "#F3FF33", "#FF33F6", 
                        "#751959", "#AA8213", "#FF6F0F", "#00FFFF", "#808000",
                        "#C0C0C0", "#FFD700", "#FF4500", "#9400D3", "#00FF00"]
        
        # Canvas ajustado para que la ruleta se vea completa
        self.canvas = tk.Canvas(root, width=500, height=500, bg="black", highlightthickness=0)
        self.canvas.pack(pady=5)
        
        # Etiqueta para el resultado en GRANDE
        self.resultado_label = tk.Label(root, text="¡Haz girar la ruleta!", font=("Arial", 20, "bold"), 
                                        fg="white", bg="black", wraplength=500)
        self.resultado_label.pack(pady=10)
        
        self.angulo_actual = 0
        self.dibujar_ruleta(0)
        
        self.boton = tk.Button(root, text="¡GIRAR!", command=self.animar_giro, 
                               bg="#e74c3c", fg="white", font=("Arial", 14, "bold"), width=12)
        self.boton.pack(pady=10)

    def dibujar_ruleta(self, angulo_offset):
        self.canvas.delete("all")
        num_opciones = len(self.opciones)
        amplitud = 360 / num_opciones
        centro_x, centro_y = 250, 250
        radio = 230
        
        for i in range(num_opciones):
            inicio = angulo_offset + (i * amplitud)
            # Dibujar el arco
            self.canvas.create_arc(centro_x - radio, centro_y - radio, 
                                   centro_x + radio, centro_y + radio, 
                                   start=inicio, extent=amplitud, 
                                   fill=self.colores[i % len(self.colores)], outline="white", width=1)
            
            # Calcular posición del texto (ajustado para que quepan 15)
            angulo_texto = math.radians(inicio + amplitud/2)
            tx = centro_x + (radio/1.4) * math.cos(angulo_texto)
            ty = centro_y - (radio/1.4) * math.sin(angulo_texto)
            
            # Texto más pequeño para las casillas reducidas
            self.canvas.create_text(tx, ty, text=self.opciones[i], font=("Arial", 7, "bold"), 
                                    fill="black", width=70, justify="center")
            
        # Indicador superior
        self.canvas.create_polygon(centro_x - 20, 20, centro_x + 20, 20, centro_x, 60, fill="yellow")

    def animar_giro(self):
        self.boton.config(state="disabled")
        self.resultado_label.config(text="veamos tu suerte...", fg="red")
        impulso = random.randint(2000, 4000) 
        self.ejecutar_animacion(impulso)

    def ejecutar_animacion(self, velocidad):
        if velocidad > 5:
            self.angulo_actual += velocidad
            self.dibujar_ruleta(self.angulo_actual)
            self.root.after(20, self.ejecutar_animacion, velocidad * 0.99)
        else:
            self.boton.config(state="normal")
            self.determinar_ganador()

    def determinar_ganador(self):
        num_opciones = len(self.opciones)
        amplitud = 360 / num_opciones
        # Lógica para detectar qué opción quedó bajo la flecha amarilla (90 grados)
        ganador_idx = int(((90 - self.angulo_actual) % 360) / amplitud)
        resultado = self.opciones[ganador_idx]
        
        # Mostrar resultado final en grande
        self.resultado_label.config(text=f"🔥 {resultado.upper()} 🔥", fg="#FF33F6")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x700") # Tamaño de ventana para que quepa todo
    app = Ruleta(root)
    root.mainloop()