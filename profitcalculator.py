import csv


def main():
    filename = input('Enter relative filepath for your CSV file:\n>>> ')
    print(getCsvReader(filename))


def calculateProfit(data):
    pass


def getCsvReader(filename):
    """Return a CSV reader for the given file (type = _csv.reader)."""

    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')

    return csv_reader


if __name__ == '__main__':
    main()