class DataAnalyzer:
    def analyze_data(self, data):
        # Perform analysis on the scraped data
        analysis_results = {
            'total_items': len(data),
            'average_length': sum(len(item) for item in data) / len(data) if data else 0
        }
        return analysis_results

    def generate_report(self, analysis_results):
        # Generate a report based on the analysis
        report = f"Data Analysis Report:\n"
        report += f"Total Items: {analysis_results['total_items']}\n"
        report += f"Average Length of Items: {analysis_results['average_length']:.2f}\n"
        return report