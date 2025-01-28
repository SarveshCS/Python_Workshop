# main.py

from web_scraper.content import ContentScraper
from web_scraper.metadata import MetadataExtractor
from web_scraper.utils import clean_text, save_to_file
from web_scraper.data_analysis import DataAnalyzer
from web_scraper.data_visualization import DataVisualizer
from web_scraper.machine_learning import ModelTrainer

def main():
    url = "http://example.com"  # Replace with the target URL

    # Step 1: Scrape content
    scraper = ContentScraper()
    html_content = scraper.fetch_content(url)
    parsed_content = scraper.parse_content(html_content)

    # Step 2: Extract metadata
    metadata_extractor = MetadataExtractor()
    metadata = metadata_extractor.extract_metadata(parsed_content)
    title = metadata_extractor.get_title(metadata)

    # Step 3: Clean text
    cleaned_text = clean_text(parsed_content)

    # Step 4: Analyze data
    analyzer = DataAnalyzer()
    analysis_results = analyzer.analyze_data(cleaned_text)
    report = analyzer.generate_report(analysis_results)

    # Step 5: Visualize data
    visualizer = DataVisualizer()
    visualizer.plot_data(analysis_results)
    visualizer.show_plot()

    # Step 6: Save report to file
    save_to_file(report, "report.txt")

if __name__ == "__main__":
    main()