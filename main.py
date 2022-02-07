from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivymd.uix.dialog import MDDialog

Config.set('kivy', 'keybord_mode', 'systemanddock')

def pez(start, percent, kapa, time, popoln):#функция принмает значение
    i = float(percent/100)#перевод процентов в необходимый для вычислений вид
    vsego = str("{0:.2f}".format((popoln*(kapa/i)*(((1+(i/kapa))**(time*kapa))-1)+start*(1+(i/kapa))**(kapa*time))))
    profit = str("{0:.2f}".format(float(float(vsego)-(start+(popoln*time*kapa)))))
    incom = str("{0:.2f}".format(float(float(profit)/(start + (popoln*time*kapa)))*100))

    return {'all': vsego, 'profit': profit, 'incom': incom}# возвращаемые значения

class Calc(BoxLayout):
    def Calc(self):#присвоение переменным значений из полей MDTextField
            try:#проверка значений в полях MDTextField
                start = int(self.start.text)
            except:
                start = 0.001
            try:
                percent = float(self.percent.text)
            except:
                percent = 1
            try:
                time = float(self.time.text)
            except:
                time = 0
            try:
                kapa = int(self.kapa.text)
            except:
                kapa = -1
            try:
                popoln = int(self.popoln.text)
            except:
                popoln = 0
                #вывод результатов вычислений в поля TextLabel
            out = pez(start, percent, kapa, time, popoln)
            self.profit.text =out.get('profit')
            self.total.text = out.get('all')
            self.incom.text = str(out.get('incom')+'%')

class MainApp(MDApp):
    def __init__(self, **kwargs):
            self.title = "My first app v0.1"
            self.theme_cls.primary_palette = "Green"
            super().__init__(**kwargs)
            #список заполняюший поля выпадающего меню
            self.menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": "О программе",
                "text_color": [1,1,1,1],
                "callback": MDApp.get_running_app().callback_for_menu_items,#вызов функиции вызывающей MDDialog
            },
            {
                "viewclass": "MDMenuItem",
                "text": "Руководство пользователя",
                "text_color": [1,1,1,1],
                "callback": MDApp.get_running_app().callback_for_menu_items1,#вызов функиции вызывающей MDDialog
            }
        ]

    def callback_for_menu_items(self, *args):
        from kivymd.uix.dialog import MDDialog

        self.alert_dialog = MDDialog(
            title="О программе ",
            size_hint=(0.8, 0.4),
            text_button_ok="Ok",
            text="Версия программы: 1.0\nПрограмма разработана студентом\n3-го курса СВГУ группы ПИБ-71\nПоповым Александром. ",
            #events_callback=self.app.callback_for_menu_items,К
        )
        self.alert_dialog.open()

    def callback_for_menu_items1(self, *args):


        self.alert_dialog = MDDialog(
            title="Руководство пользователя",
            size_hint=(0.8, 0.8),
            text_button_ok="Ok",
            text='Для того чтобы получить результаты расчетов необходимо заполнить поля:\nПервоначальная сумма", "Процентная ставка", "Срок инвестирования в годах", "Количество капитализаций в году".\n\nЕсли предполагается довложение средств в течение расчетного срока следует заполнить строку "Сумма пополнения".\n\nДля получения результата необходимо нажать на кнопку "Рассчитать"\nПри необходимости произвести расчет на срок менее одного года можно указывать дробные числа, так например 0.5 в строке "Срок инвестирования в годах" будет означать 6 месяцев, при этом расчет количества капитализаций в году остается прежним.'
            #events_callback=self.app.callback_for_menu_items,К
        )
        self.alert_dialog.open()



    def build(self):

        return Calc()




if __name__ == "__main__":
    MainApp().run()
