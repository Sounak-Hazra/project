import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from multiprocessing import Process


class tic_tac_to(FloatLayout,Widget):
    i=1
    fpalyerscore=0
    splayerscore=0
    drawn=0
    alredyclicked=[]#all alredy clicked buttons instance are saved hear 
    gameEnd=0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def change_text(self, instance,button):
        if instance not in self.alredyclicked:#if the button is alredy clicked then for next click it will not change 
            if self.gameEnd>0:
                pass
            elif (self.i%2)!=0:
                instance.text = "X"
                instance.id="X"
                self.alredyclicked.append(instance)
            else:
                instance.text="O"
                self.alredyclicked.append(instance)
            self.i+=1
            self.whomeTurn()
    def whomeTurn(self):
        if (self.i%2)!=0:
            return "First Player Turn !"
        else:
            return "Second Player Turn !"

    def whowin(self,instance,instance1,instance2,instance3,instance4,instance5,instance6,instance7,instance8,instance9,firsplayertbutton,secondplayerbutton,drawnbutton):
        animation=Animation(
            background_color=(0, 1, 0, 1),
            duration=1
        )
        if self.gameEnd>1:
            pass
        elif ((instance1.text=="X" and instance5.text=="X" and instance9.text=="X") or (instance3.text=="X" and instance5.text=="X" and instance7.text=="X") or (instance4.text=="X" and instance5.text=="X" and instance6.text=="X") or (instance1.text=="X" and instance2.text=="X" and instance3.text=="X") or (instance7.text=="X" and instance8.text=="X" and instance9.text=="X") or (instance1.text=="X" and instance4.text=="X" and instance7.text=="X") or (instance3.text=="X" and instance6.text=="X" and instance9.text=="X") or (instance2.text=="X" and instance5.text=="X" and instance8.text=="X")):
            if((instance1.text=="X" and instance5.text=="X" and instance9.text=="X")):
                animation.start(instance1)
                animation.start(instance5)
                animation.start(instance9)
                self.gameEnd+=1
            elif((instance3.text=="X" and instance5.text=="X" and instance7.text=="X")):
                animation.start(instance3)
                animation.start(instance5)
                animation.start(instance7)
                self.gameEnd+=1
            elif((instance4.text=="X" and instance5.text=="X" and instance6.text=="X")):
                animation.start(instance4)
                animation.start(instance5)
                animation.start(instance6)
                self.gameEnd+=1
            elif((instance1.text=="X" and instance2.text=="X" and instance3.text=="X")):
                animation.start(instance1)
                animation.start(instance2)
                animation.start(instance3)
                self.gameEnd+=1
            elif(((instance7.text=="X" and instance8.text=="X" and instance9.text=="X"))):
                animation.start(instance7)
                animation.start(instance8)
                animation.start(instance9)
                self.gameEnd+=1
            elif((instance1.text=="X" and instance4.text=="X" and instance7.text=="X")):
                animation.start(instance1)
                animation.start(instance4)
                animation.start(instance7)
            elif((instance3.text=="X" and instance6.text=="X" and instance9.text=="X")):
                animation.start(instance3)
                animation.start(instance6)
                animation.start(instance9)
                self.gameEnd+=1
            elif ((instance2.text=="X" and instance5.text=="X" and instance8.text=="X")):
                animation.start(instance2)
                animation.start(instance5)
                animation.start(instance8)
                self.gameEnd+=1
            if self.gameEnd==1:
                self.fpalyerscore+=1
            firsplayertbutton.text=f"First Player Score : {self.fpalyerscore}"
        elif ((instance1.text=="O" and instance5.text=="O" and instance9.text=="O") or (instance3.text=="O" and instance5.text=="O" and instance7.text=="O") or (instance4.text=="O" and instance5.text=="O" and instance6.text=="O") or (instance1.text=="O" and instance2.text=="O" and instance3.text=="O") or (instance7.text=="O" and instance8.text=="O" and instance9.text=="O") or (instance1.text=="O" and instance4.text=="O" and instance7.text=="O") or (instance3.text=="O" and instance6.text=="O" and instance9.text=="O") or (instance2.text=="O" and instance5.text=="O" and instance8.text=="O")):
            if((instance1.text=="O" and instance5.text=="O" and instance9.text=="O")):
                animation.start(instance1)
                animation.start(instance5)
                animation.start(instance9)
                self.gameEnd+=1
            elif((instance3.text=="O" and instance5.text=="O" and instance7.text=="O")):
                animation.start(instance3)
                animation.start(instance5)
                animation.start(instance7)
                self.gameEnd+=1
            elif((instance4.text=="O" and instance5.text=="O" and instance6.text=="O")):
                animation.start(instance4)
                animation.start(instance5)
                animation.start(instance6)
                self.gameEnd+=1
            elif((instance1.text=="O" and instance2.text=="O" and instance3.text=="O")):
                animation.start(instance1)
                animation.start(instance2)
                animation.start(instance3)
                self.gameEnd+=1
            elif(((instance7.text=="O" and instance8.text=="O" and instance9.text=="O"))):
                animation.start(instance7)
                animation.start(instance8)
                animation.start(instance9)
                self.gameEnd+=1
            elif((instance1.text=="O" and instance4.text=="O" and instance7.text=="O")):
                animation.start(instance1)
                animation.start(instance4)
                animation.start(instance7)
                self.gameEnd+=1
            elif((instance3.text=="O" and instance6.text=="O" and instance9.text=="O")):
                animation.start(instance3)
                animation.start(instance6)
                animation.start(instance9)
                self.gameEnd+=1
            elif ((instance2.text=="O" and instance5.text=="O" and instance8.text=="O")):
                animation.start(instance2)
                animation.start(instance5)
                animation.start(instance8)
                self.gameEnd+=1
            if self.gameEnd==1:
                self.splayerscore+=1
            secondplayerbutton.text=f"Second Player Score : {self.splayerscore}"
        elif((instance1.text=="X" or instance1.text=="O") and (instance2.text=="X" or instance2.text=="O" ) and (instance3.text=="X" or instance3.text=="O") and (instance4.text=="X" or instance4.text=="O") and (instance5.text=="X" or instance5.text=="O") and (instance6.text=="X" or instance6.text=="O") and (instance7.text=="X" or instance7.text=="O") and (instance8.text=="X" or instance8.text=="O") and (instance9.text=="X" or instance9.text=="O")):
            instance1.text=""
            instance2.text=""
            instance3.text=""
            instance4.text=""
            instance5.text=""
            instance6.text=""
            instance7.text=""
            instance8.text=""
            instance9.text=""
            self.alredyclicked=[]
            self.drawn+=1
            drawnbutton.text=f"Drawn games :{self.drawn}"
    def all_clear(self,instance,instance1,instance2,instance3,instance4,instance5,instance6,instance7,instance8,instance9,firsplayertbutton,secondplayerbutton,drawnbutton):
        instance1.background_color=(0.0, 0.8, 1.0, 1.0)
        instance2.background_color=(0.0, 0.8, 1.0, 1.0)
        instance3.background_color=(0.0, 0.8, 1.0, 1.0)
        instance4.background_color=(0.0, 0.8, 1.0, 1.0)
        instance5.background_color=(0.0, 0.8, 1.0, 1.0)
        instance6.background_color=(0.0, 0.8, 1.0, 1.0)
        instance7.background_color=(0.0, 0.8, 1.0, 1.0)
        instance8.background_color=(0.0, 0.8, 1.0, 1.0)
        instance9.background_color=(0.0, 0.8, 1.0, 1.0)
        instance1.text=""
        instance2.text=""
        instance3.text=""
        instance4.text=""
        instance5.text=""
        instance6.text=""
        instance7.text=""
        instance8.text=""
        instance9.text=""
        self.alredyclicked=[]
        self.gameEnd=0
class P(GridLayout):# pop up window function this make the popup after one player wins.
    rows=2
    def __init__(self,winner):
        super().__init__()
        self.add_widget(Label(text=winner))
        self.button=Button(text="TAP ANYWHARE FOR NEXT GAME")
        self.add_widget(self.button)
    def pressed(self,instance):
        dismiss=Popup()
        dismiss.dismiss()
def show_popup(winner):
    popupwindow=Popup(title="GAME END !", content=P(winner),size_hint=(None,None),size=(400,400),background_color = (1, 0, 0, 0))
    popupwindow.open()  
class Tic_Tac_To(App):
    def build(self):
        return tic_tac_to()
if __name__=="__main__":
    Tic_Tac_To().run()