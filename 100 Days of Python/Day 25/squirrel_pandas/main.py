import pandas

squirrel_data = pandas.read_csv("./Day 25/squirrel_pandas/squirrel_data.csv")

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [],
}

fur_color_occurrences = squirrel_data["Primary Fur Color"].to_list()

squirrel_dict["Count"].append(fur_color_occurrences.count("Gray"))
squirrel_dict["Count"].append(fur_color_occurrences.count("Cinnamon"))
squirrel_dict["Count"].append(fur_color_occurrences.count("Black"))

data = pandas.DataFrame(squirrel_dict)

data.to_csv("new_data.csv")
