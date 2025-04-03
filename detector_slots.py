import tkinter as tk from tkinter import messagebox import threading import time

class SlotDetector: def init(self, root): self.root = root self.root.title("Detector de Slots") self.root.geometry("300x200")

self.running = False
    
    self.label = tk.Label(root, text="Detector Desligado", font=("Arial", 12))
    self.label.pack(pady=20)
    
    self.btn_on = tk.Button(root, text="ON", command=self.start_detection, bg="green", fg="white", width=10)
    self.btn_on.pack(pady=5)
    
    self.btn_off = tk.Button(root, text="OFF", command=self.stop_detection, bg="red", fg="white", width=10)
    self.btn_off.pack(pady=5)

def detection_logic(self):
    while self.running:
        print("Analisando padrões...")  # Aqui entra a lógica real do detector
        time.sleep(2)  # Simula análise de padrões
    print("Detector parado.")
    
def start_detection(self):
    if not self.running:
        self.running = True
        self.label.config(text="Detector Ligado")
        threading.Thread(target=self.detection_logic, daemon=True).start()
    else:
        messagebox.showinfo("Info", "O detector já está rodando!")
    
def stop_detection(self):
    self.running = False
    self.label.config(text="Detector Desligado")

if name == "main": root = tk.Tk() app = SlotDetector(root) root.mainloop()