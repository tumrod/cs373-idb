import json
import urllib
import subprocess

from urllib.request import Request, urlopen, URLError

def test_controller():
    print("Running tests")
    script = subprocess.Popen("make test", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = script.communicate()
    except:
        script.kill()
    print(outs.decode())
    return errs.decode()

def league_controller():
    champions_url = urllib.request.urlopen("http://leagueofdowning.link/api/champions/")
    champions = json.loads(champions_url.read().decode('utf-8'))

    items_url = urllib.request.urlopen("http://leagueofdowning.link/api/items/")
    items = json.loads(items_url.read().decode('utf-8'))

    all_champions = {}

    for champ_id, champ_info in champions.items():
        champ_name = champ_info['name']
        champ_dict = {}

        champ_dict['champ_img'] = champ_info['image']

        champ_items = champ_info['recommended_items']
        total_cost = 0
        items_img_list = []

        for i in champ_items:
            items_info = items[str(i)]
            total_cost += items_info['total_gold']
            i_name = items_info['name']
            i_img = items_info['image']
            i_name_img = [i_name, i_img]
            items_img_list.append(i_name_img)

        champ_dict['total_cost'] = total_cost
        champ_dict['items_img_list'] = items_img_list
        all_champions[champ_name] = champ_dict
        return all_champions

def search_controller(query):

    search_results = {}
    search_terms = query.split('+')

    if len(search_terms) == 1:
        request = Request('http://api.swiftype.com/api/v1/public/engines/search.json?q=' + query +
                          '&engine_key=kyg84sUxAL9zE2ACjK4c')
        try:
            response = urlopen(request)
            string = response.read().decode('utf-8')
            search_results['single'] = json.loads(string)
            return search_results
        except URLError:
            print('Error')

    elif len(search_terms) > 1:

        and_query = '+AND+'.join(search_terms)
        or_query = '+OR+'.join(search_terms)

        and_request = Request('http://api.swiftype.com/api/v1/public/engines/search.json?q=' + and_query +
                          '&engine_key=kyg84sUxAL9zE2ACjK4c')

        or_request = Request('http://api.swiftype.com/api/v1/public/engines/search.json?q=' + or_query +
                          '&engine_key=kyg84sUxAL9zE2ACjK4c')

        try:
            and_response = urlopen(and_request)
            or_response = urlopen(or_request)

            and_string = and_response.read().decode('utf-8')
            or_string = or_response.read().decode('utf-8')

            search_results['AND'] = json.loads(and_string)
            search_results['OR'] = json.loads(or_string)

            return search_results
        except URLError:
            print('Error')