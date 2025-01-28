from web_scraper.data_visualization import DataVisualizer
from web_scraper.data_analysis import DataAnalyzer

def main():
    # Step 4: Analyze data
    analyzer = DataAnalyzer()
    cleaned_text = "your cleaned text here"  # Replace with actual cleaned text
    analysis_results = analyzer.analyze_data(cleaned_text)
    report = analyzer.generate_report(analysis_results)

    # Step 5: Visualize data
    visualizer = DataVisualizer()
    visualizer.plot_data(analysis_results)
    visualizer.show_plot()

if __name__ == "__main__":
    main()