import matplotlib.pyplot as plt

class DataVisualizer:
    def plot_data(self, data):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        keys = list(data.keys())
        values = list(data.values())
        
        print(f"Plotting data with {len(keys)} keys and {len(values)} values.")
        
        plt.plot(keys, values)
        plt.xlabel('Keys')
        plt.ylabel('Values')
        plt.title('Data Visualization')
    
    def show_plot(self):
        print("Displaying plot.")
        plt.show()