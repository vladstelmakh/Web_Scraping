
# Flask Product Scraping and Visualization App

This Flask application allows users to scrape product data from [Flagma.pl](https://flagma.pl/), visualize the data using various graphs, and download the results as a CSV file. The app is designed to be user-friendly and offers several features to explore and analyze product information.

## Features

- Scrape product data from [Flagma.pl](https://flagma.pl/) based on a user-provided query.
- Display scraped product data in a table with options to edit or delete individual entries.
- Visualize data through various graphs, including:
  - Bar chart of product prices
  - Histogram of price distribution
  - Pie chart of company distribution
- Download scraped data as a CSV file for further analysis.
- Responsive design using Bootstrap for an optimal user experience on any device.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:

   \`\`\`bash
   git clone 
   \`\`\`

2. Navigate to the project directory:

   \`\`\`bash
   cd web
   \`\`\`

3. Create and activate a virtual environment:

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   \`\`\`

4. Install the required dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. Run the Flask application:

   \`\`\`bash
   python app.py
   \`\`\`

6. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to start using the app.

## Usage

On the home page, enter a search query to scrape product data from [Flagma.pl](https://flagma.pl/). After the search is complete, you will be redirected to the results page where you can:

- View the scraped data in a table format.
- Edit or delete individual product entries.
- Download the data as a CSV file.
- Visualize the data using different types of graphs.

## Screenshots

Here are some screenshots of the application:

- **Home Page**: A clean and simple interface to enter your search query.
- **Results Page**: Displaying scraped data with options to edit, delete, or download.
- **Graphs Page**: Visualizations of product data through various graphs.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **BeautifulSoup**: A library for parsing HTML and XML documents.
- **Pandas**: A data manipulation and analysis library.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations.
- **Bootstrap**: A CSS framework for building responsive and mobile-first websites.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact

If you have any questions or need further information, feel free to contact me at vlad0067vlad@gmail.com
