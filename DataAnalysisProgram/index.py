import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
first_row = ""
with open("data.csv" , 'r') as f : 
    first_row  = f.readline()
    print(f.readline() , type(f.readline()))
print(first_row)

with open('data.csv', 'r') as csv_file:
    data = csv_file.readlines()

file_data = []
for i in data : 
    file_data.append(i.split(","))
print(file_data)
row = first_row.split(",")
print(row)
class CSVDisplayApp(App):
    def build(self):

        # Main_layout  = BoxLayout(orientation = 'horizontal')
        grid_layout =BoxLayout(orientation = 'vertical' )
        
        # for i in range(len(row)) :
        #     grid_layout.add_widget(Button(text=f"{row[i]}", size = (10,10)))
        
        for i in file_data : 
            row_layout = GridLayout(cols = 4)
            for j in i : 
                
                
                row_layout.add_widget(Label(text = f"{j}" , size_hint_x = 700))
            grid_layout.add_widget(row_layout)
    
        # Add the ScrollView to the Main_layout
        root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))
        root.add_widget(grid_layout)
        # Main_layout.add_widget(scroll_view)
        # Main_layout.add_widget(grid_layout)
        # Main_layout.add_widget(Button(text = "ClickMe"))
        

        return root

if __name__ == '__main__':
    CSVDisplayApp().run()
