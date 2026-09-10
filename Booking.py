from tkinter import *                       # імпортування всіх класів та функцій з модуля tkinter

root = Tk()                                 # створення головного вікна
root.title("Редактор тексту")               # встановлення заголовку вікна
root.geometry("600x400")                    # встановлення розмірів вікна
root.iconbitmap("img/morda.ico")                # встановлення іконки вікна

f_text = Frame(root)                        # рамка для текстового поля
f_text.pack(fill=BOTH,  expand=1)           # розтягування рамки на весь простір вікна

text_fild = Text(f_text, 
                 bg='black',                # фоновий колір
                 fg='lime',                 # колір тексту
                 padx=10,                   # відступи по горизонталі
                 pady=10,                   # відступи по вертикалі
                 wrap=WORD,                 # перенесення слів на новий рядок
                 insertbackground='red',    # колір курсору
                 selectbackground='orange', # колір виділеного тексту
                 spacing3=10,               # відстань між рядками
                 width=30,                  # ширина текстового поля
                 
                 

                 )
text_fild.pack(fill=BOTH, expand=1, side=LEFT)      # розтягування текстового поля на весь простір рамки

scroll = Scrollbar(f_text, command=text_fild.yview) # створення вертикальної смуги прокрутки
scroll.pack(side=LEFT, fill=Y)                      # розтягування смуги прокрутки на всю висоту рамки
text_fild.config(yscrollcommand=scroll.set)         # зв'язування смуги прокрутки з текстовим полем


root.mainloop()                                     # запуск головного циклу обробки подій