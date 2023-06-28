import os
import sys
import csv
import tkinter

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import customtkinter


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.title("Steam Games Trending Finder")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo labels
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Steam Trending", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # SideBar widgets
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Show trends", command=self.bfsData)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # Textbox
        self.textBox = customtkinter.CTkTextbox(self, width = 250)
        self.textBox.grid(row=0, column=1, padx=(20,0), pady=(20,20), sticky="nsew")

        # Input field
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Type a game title")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20,0), pady=(20,20), sticky="nsew")

        self.entry_button = customtkinter.CTkButton(master=self, fg_color="transparent", text="Search", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.entry_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Member list
        self.sidebar_team = customtkinter.CTkLabel(self.sidebar_frame, text="Software Engineering UPC", anchor="w")
        self.sidebar_team.grid(row=3, column=0, padx=20, pady=(10, 0))




    def bfsData(self):
        print("Showing trending games")


class Record:
    def __init__(self,game,year,month,avg,gain,peak,avg_peak_perc):
        self.game = game
        self.year = year
        self.month = month
        self.avg = avg
        self.gain = gain
        self.peak = peak
        self.avg_peak_perc = avg_peak_perc
    
    def returnName(self):
        return self.name
    
    def returnYear(self):
        return self.year
    
    def returnMonth(self):
        return self.month
    
    def returnGain(self):
        return self.gain
    
    def returnPeak(self):
        return self.peak
    
    def returnAvg(self):
        return self.avg_peak_perc

def createRecord(row):
    return Record(row['gamename'], row['year'],row['month'],row['avg'],row['gain'],row['peak'],row['avg_peak_perc'])

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, game):
        self.graph.add_node(game)


def bfs(graph, start_node):
    pass


labels = ['game name', 'year', 'month', 'avg', 'gain', 'peak', 'avg_peak_perc']
steam_data = pd.read_csv('SteamCharts.csv', encoding='unicode_escape', names=labels)




def main():

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")





    # Empty graph
    G = nx.Graph()

    # Data to convert 
    games = steam_data.apply(createRecord,axis=1).tolist()

    # insert data into the graph
    for game in games:
        G.add_node(game)


    
    bfs(G)

    

if __name__=='__main__':
    app = App()
    app.mainloop()