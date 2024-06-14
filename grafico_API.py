import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Extrator de dados')
        self.root.geometry('400x500')

        self.fetch_button = tk.Button(self.root, text='Extrair dados', command=self.fetch_data)
        self.fetch_button.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=50, height=100, font=('Arial', 12))
        self.listbox.pack(pady=10)

    def fetch_data(self):
        import requests
        try:
            response = requests.get("http://127.0.0.1:5000/anime")
            if response.status_code == 200:
                data = response.json()
                self.listbox.delete(0, tk.END)
                for item in data:
                    if isinstance(item, dict) and 'name' in item:
                        self.listbox.insert(tk.END, item['name'])
                    else:
                        self.listbox.insert(tk.END, item) 
            else:
                messagebox.showerror('Erro', f"Código de status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Erro ao conectar', e)
        except Exception as ex:
            messagebox.showerror('Erro inesperado', str(ex))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()