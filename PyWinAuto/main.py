from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import time

def bot():
    # Application(backend="uia")
    try:
        app = Application().connect(path=r"C:\Program Files (x86)\Notepad++\notepad++.exe")
    except:
        # cmd_line=u'notepad++.exe')
        app = Application().start(r"C:\Program Files (x86)\Notepad++\notepad++.exe")

    app.Notepad.print_control_identifiers()
    app.Notepad.child_window(title="Selected Tab", class_name="#32770")

    # app.Notepad.menu_select('Arquivo->Salvar')
    # app.SalvarComo.edit.set_edit_text('aqui.txt')
    # app.SalvarComo.Trabalho.click()
    #app.Salvarcomo.edit.set_edit_text('aqui.txt')
    #app.Salvarcomo.Salvar.click()

    # dlg = app.window(title_re=".*Notepad.*")

    # dlg.menu_select("Linguagem -> XML")
    # dlg.Edit.type_keys('Welcome to Medium')


if __name__ == '__main__':
    bot()


