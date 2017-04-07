# Precedence Graph Generation

This project was created as a part of the Clemson University BMW Creative Inquiry. The project is to visualize precedence relationships in manufacturing data. The code reads in data from an Excel workbook, discovers precedence relationships, and visualizes these relationships using Graphviz (App, not Python library).

## Installation

This code requires customization. The original input was an Excel workbook with two pages that contained manufacturing data. The code will have to be modified for your input. It uses Python 2.7, networkx, matplotlib, and xlrd.

## Usage

Use your (modified) Excel Extraction file to extract the data. Then use DotGeneration to create the .dot file for use with Graphviz. Graphviz is responsible for the actual visualization.  

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

Open use.
