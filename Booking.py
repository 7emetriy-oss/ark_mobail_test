from tkinter import *                          # імпортування всіх класів та функцій з модуля tkinter
from tkinter import messagebox                 # імпортування модуля messagebox з tkinter
from tkinter import filedialog                 # імпортування модуля messagebox з tkinter


# region  ----------- DEF
def chenge_theme(theme):                              # функція для зміни теми
    text_fild['bg']=view_color[theme]['test_bg']                  # зміна кольору фону відповідно до обраної теми
    text_fild['fg']=view_color[theme]['test_fg']                  # зміна кольору фону та тексту відповідно до обраної теми
    text_fild['insertbackground']=view_color[theme]['cursor']     # зміна кольору курсору відповідно до обраної теми
    text_fild['selectbackground']=view_color[theme]['select_bg']  # зміна кольору виділеного тексту відповідно до обраної теми

def chenge_fonts(fontss):                              # функція для зміни шрифту
    text_fild['font'] = fonts[fontss]['font']          # зміна шрифту відповідно до обраного шрифту

def notepad_exit():                                                   # функція для закриття вікна
    answer = messagebox.askyesno('Вихід', 'Ви дійсно хочете вийти?')  # запит користувача на підтвердження виходу з програми
    if answer:                                                        # якщо користувач підтвердив вихід, закриваємо вікно
        root.destroy()                                                # закриття головного вікна

def open_file():                                                        # функція для відкриття файлу
    file_path = filedialog.askopenfilename(title="Відкрити файл", filetypes=(('Текст документи (*.txt)', '*.txt'), ('Усі файли', '*.*')))  # відкриття діалогового вікна для вибору файлу з фільтром на текстові документи та всі файли
    if file_path:                                                      # якщо користувач вибрав файл
            text_fild.delete(1.0, END)                                 # очищаємо текстове поле
            text_fild.insert('1.0', open(file_path, encoding='utf-8').read())       # вставляємо вміст файлу в текстове поле

def save_file():                                                        # функція для збереження файлу
     file_path = filedialog.asksaveasfilename(filetypes=(('Текст документи (*.txt)', '*.txt'), ('Усі файли', '*.*')))  # відкриття діалогового вікна для вибору файлу з фільтром на текстові документи та всі файли
     f =open(file_path, 'w', encoding='utf-8')
     text = text_fild.get(1.0, END)
     f.write(text)
     f.close()



# endregion
root = Tk()                                 # створення головного вікна
root.title("Редактор тексту")               # встановлення заголовку вікна
root.geometry("600x400")                    # встановлення розмірів вікна
root.iconbitmap("img/morda.ico")            # встановлення іконки вікна

#----------------------------------------------------------------------------------------------------------------------------------

#region ФУНКЦІЇ МЕНЮ

main_menu = Menu(root)                       # створення головного меню

# ФАЙЛ
file_menu = Menu(main_menu, tearoff=0)       # створення підменю "Файл"
file_menu.add_command(label="Відкрити", command=open_file)      # додавання пункту "Відкрити" в підменю "Файл"
file_menu.add_separator()                    # додавання роздільника
file_menu.add_command(label="Зберегти", command=save_file)      # додавання пункту "Зберегти" в підменю "Файл"
file_menu.add_separator()                    # додавання роздільника
file_menu.add_command(label="Вийти", command=notepad_exit)         # додавання пункту "Вийти" в підменю "Файл" з прив'язкою до функції закриття вікна

# ВИД
view_menu = Menu(main_menu, tearoff=0)        # створення підменю "Вид"
view_menu_sub = Menu(view_menu, tearoff=0)    # створення підменю "Вид" з підпунктами
font_menu_sub = Menu(view_menu, tearoff=0)    # створення підменю "Шрифт" з підпунктами
#--------------------------------------------------------------------------------------------------------------------------------------------
#Тема
view_menu_sub.add_command(label='Темна', command=lambda: chenge_theme('dark'))                 # додавання пункту "Темна" в підменю "Вид"
view_menu_sub.add_command(label='Світла', command=lambda: chenge_theme('light'))                # додавання пункту "Світла" в підменю "Вид"
view_menu.add_cascade(label="Тема", menu=view_menu_sub)  # додавання підменю "Тема" в підменю "Вид"
#---------------------------------------------------------------------------------------------------------------------------------------------
# Шрифти
font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))                    # додавання пункту "Arial" в підменю "Шрифт"
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))            # додавання пункту "Comic Sans MS" в підменю "Шрифт"
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))          # додавання пункту "times new roman" в підменю "Шрифт"
view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub) # додавання підменю "Шрифт" в підменю "Вид"
root.config(menu=view_menu)                                 # встановлення підменю "Вид" в головне меню

#---------------------------------------------------------------------------------------------------------------------------------------------
view_menu.add_separator()                     # додавання роздільника
view_menu.add_command(label="Нормальний")     # додавання пункту "Нормальний" в підменю "Вид"
view_menu.add_command(label="Повний екран")   # додавання пункту "Повний екран" в підменю "Вид"





#---------------------------------------------------------------------------------------------------------------------------------------------
root.config(menu=file_menu)                  # встановлення підменю "Файл" в головне меню
# Додавання списку меню
main_menu.add_cascade(label="Файл", menu=file_menu)  # додавання підменю "Файл" в головне меню
main_menu.add_cascade(label="Вид", menu=view_menu)   # додавання підменю "Вид" в головне меню
root.config(menu=main_menu)                  # встановлення головного меню в головне вікно

#endregion

#----------------------------------------------------------------------------------------------------------------------------------

# region НАЛАШТУВАННЯ ВІЗУАЛУ КОДУ

f_text = Frame(root)                        # рамка для текстового поля
f_text.pack(fill=BOTH,  expand=1)           # розтягування рамки на весь простір вікна

view_color = {
    'dark': {
        'test_bg': 'black', 'test_fg': 'lime', 'cursor': 'red', 'select_bg': 'orange'
    },
    'light': {
        'test_bg': 'white', 'test_fg': 'black', 'cursor': 'blue', 'select_bg': 'yellow'
    }

}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }

}




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
                 font='Arial 14 bold'       # шрифт та розмір тексту
                 

                 )

# endregion

#----------------------------------------------------------------------------------------------------------------------------------


text_fild.pack(fill=BOTH, expand=1, side=LEFT)      # розтягування текстового поля на весь простір рамки

scroll = Scrollbar(f_text, command=text_fild.yview) # створення вертикальної смуги прокрутки
scroll.pack(side=LEFT, fill=Y)                      # розтягування смуги прокрутки на всю висоту рамки
text_fild.config(yscrollcommand=scroll.set)         # зв'язування смуги прокрутки з текстовим полем


root.mainloop()                                     # запуск головного циклу обробки подій