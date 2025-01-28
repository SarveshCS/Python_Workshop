class DataVisualizer:
    def plot_data(self, data):
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        plt.plot(data)
        plt.title('Data Visualization')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid()
        plt.show()

    def show_plot(self):
        import matplotlib.pyplot as plt
        plt.show()