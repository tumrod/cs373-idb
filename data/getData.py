from urllib.request import urlopen
import json
import sys
import subprocess


def load_json (filename) :
    """
    load a json file from filename into id_dict
    return dict
    """

	id_dict = {}
	with open(filename) as data_file:
		info_dict = json.load(data_file)

	for i in info_dict["items"]:
		#print(i["title"],end="\t")
		#print(i["id"])							# get the id of the page
		id_dict[i["id"]] = i["title"]

	return id_dict


def wget_id(category, id_dict):
    """
    makedir <category_name> to put coresponding files in that directory
    wget -O category/<id>.json "http://starwars.wikia.com/api/v1/Articles/AsSimpleJson?id=<id>"

    category: category's name
    id_dict: 
    """

    category = category.replace("(","").replace(")","")
    mkdir = "mkdir " + category
    p = subprocess.Popen(mkdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # run the wget command for each file
    url_root = "http://starwars.wikia.com/api/v1/Articles/AsSimpleJson?id="
    for k in id_dict:
        command = "wget -O "+ category +"/"+str(k) + ".json \"" + url_root + str(k) + "\""
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        index = 0;

        # wait until finished
        retval = p.wait()



def wget_category(category):
    """
    wget -O category/<category>.json "http://starwars.wikia.com/api/v1/Articles/List?category=<category>&limit=200"

    """

    # run the wget command for each file
    url_root = "http://starwars.wikia.com/api/v1/Articles/List?category=" + category + "&limit=200"
    category = category.replace("(","").replace(")","")
    command = "wget -O " +"categories/"+category + ".json \"" + url_root + "\""
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    index = 0;

    retval = p.wait()


def run(category_name):
    """
    running wget_category and then uses the id to run wget_id
    category_name:

    """
    wget_category(category_name)
    category_name = category_name.replace("(","").replace(")","")
    id_dict = load_json("./categories/"+category_name+".json")
    wget_id(category_name, id_dict)


def cate_cate(category_name):
    """
    usage: category within category
    category_name: the larger scope category_name
    """
    wget_category(category_name)
    category_name = category_name.replace("(","").replace(")","")
    id_dict = load_json("./categories/"+category_name+".json")

    j = 0;                                      # for testing to get only 3
    for i in id_dict:
        if (j!=3):
            run(str(id_dict[i]))
            j+=1


def main():
    """
    running each category by run("<category_name>")
    """
    #run("Sentient_species_by_name")
    #run("Colonies_planets")

    #run("Individuals_by_species")

    #cate_cate("Individuals_by_species")
    
    '''
    cate = "Sentient_species_("
    alpha = ["A", "B", "C"]
    #alpha = ["A", "B","C","D","E","F","G","H","I","J","K","L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in alpha:
        rename = cate+i+")"
        run(rename)
    '''
main()