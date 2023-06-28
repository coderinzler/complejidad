import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


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

class Graph():
    def __init__(self):
        self.graph =  nx.Graph()

    def addNode(self):
        self.graph.a
    
labels = ['gamename','year','month','avg','gain','peak','avg_peak_perc']
steam_data = pd.read_csv('SteamCharts.csv', encoding = 'unicode_escape', names = labels)


def main():
    # Empty graph
    G = nx.Graph()

    # Data to convert 
    games = steam_data.apply(createRecord,axis=1).tolist()

    # insert data into the graph
    for game in games:
        G.add_node(game)

    nx.draw_networkx(G)
    plt.show()



    #for row in steam_data.iterrows():
    #   G.addnode()

if __name__ == '__main__':
    main()