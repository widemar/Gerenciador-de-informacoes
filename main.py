from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

COR_AZUL = "#24ffff"


# ---------------------------- PROCURAR EMAIL E SENHA ------------------------------- #
def encontrar_senha():
	capturar_site = site_entrada.get()
	try:
		with open("dados.json", "r") as dados:
			obtendo_dados = json.load(dados)
			if capturar_site not in obtendo_dados:
				messagebox.showwarning(title="Alerta", message=f"{capturar_site} não está cadastrado")
			else:
				email = obtendo_dados[capturar_site]["email"]
				senha = obtendo_dados[capturar_site]["senha"]
				messagebox.showinfo(title="Dados do Cliente", message=f"Email: {email}\nSenha: {senha}")
	except FileNotFoundError:
		messagebox.showwarning(title="Alerta", message="Nenhum site cadastrado ainda")


# ---------------------------- GERADOR DE SENHAS ------------------------------- #


def gerador_senha():
	letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			  'v',
			  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
			  'R',
			  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letras = random.randint(8, 10)
	nr_simbolos = random.randint(2, 4)
	nr_numeros = random.randint(2, 4)

	password_list = [random.choice(letras) for _ in range(nr_letras)]
	password_list += [random.choice(simbolos) for _ in range(nr_simbolos)]
	password_list += [random.choice(numeros) for _ in range(nr_numeros)]

	random.shuffle(password_list)

	password = "".join(password_list)

	if len(senha_entrada.get()) == 0:
		senha_entrada.insert(0, password)
		pyperclip.copy(password)


# ---------------------------- SALVAR SENHA ------------------------------- #
def salvar():
	capturar_site = site_entrada.get()
	capturar_email = email_entrada.get()
	capturar_senha = senha_entrada.get()

	novos_dados = {capturar_site: {
		"email": capturar_email,
		"senha": capturar_senha
	}}

	if capturar_site == "" or capturar_email == "" or capturar_senha == "":
		messagebox.showwarning(title="Alerta", message="Por favor não deixe campos em branco")
	else:
		try:
			with open("dados.json", "r") as dados:
				carregando_dados = json.load(dados)
				carregando_dados.update(novos_dados)
		except FileNotFoundError:
			with open("dados.json", "w") as dados:
				json.dump(novos_dados, dados, indent=4)
		else:
			with open("dados.json", "w") as dados:
				json.dump(carregando_dados, dados, indent=4)
		finally:
			site_entrada.delete(0, END)
			email_entrada.delete(0, END)
			senha_entrada.delete(0, END)


# ---------------------------- INTERFACE GRÁFICA ------------------------------- #
# Criando tela
tela = Tk()
tela.title("Gerador de Senhas")
tela.configure(padx=50, pady=50, bg=COR_AZUL)
tela.maxsize(width=800, height=500)
tela.minsize(width=800, height=500)

# Adicionando Imagem
imagem = PhotoImage(file="cadeado.png")
canvas = Canvas(width=200, height=200, bg=COR_AZUL, highlightthickness=0)
canvas.create_image(100, 100, image=imagem)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
site_texto = Label(text="Site:", font=("Courier", 13, "normal"), bg=COR_AZUL)
site_texto.grid(row=1, column=0)
email_texto = Label(text="Email/Username:", font=("Courier", 13, "normal"), bg=COR_AZUL)
email_texto.grid(row=2, column=0)
senha_texto = Label(text="Senha:", font=("Courier", 13, "normal"), bg=COR_AZUL)
senha_texto.grid(row=3, column=0)

# Entrys
site_entrada = Entry(width=30, font=("Courier", 15, "normal"))
site_entrada.grid(row=1, column=1, pady=10)
site_entrada.focus()
email_entrada = Entry(width=39, font=("Courier", 15, "normal"))
email_entrada.grid(row=2, column=1, columnspan=2)
senha_entrada = Entry(width=30, font=("Courier", 15, "normal"))
senha_entrada.grid(row=3, column=1, pady=10)

# Buttons
procurar_button = Button(
	text="Procurar",
	font=("Courier", 10, "normal"),
	bg="yellow",
	width=12,
	command=encontrar_senha
)
procurar_button.grid(row=1, column=2)
gerar_senha = Button(
	text="Gerar Senha",
	font=("Courier", 10, "normal"),
	bg="yellow",
	width=12,
	command=gerador_senha
)
gerar_senha.grid(row=3, column=2)
add_senha = Button(
	text="Adicionar Senha",
	width=59,
	font=("Courier", 10, "normal"),
	bg="green",
	fg="white",
	command=salvar
)
add_senha.grid(row=4, column=1, columnspan=2)

tela.mainloop()
