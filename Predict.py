import numpy as np
import heapq
import json
import collections

feat_array = np.loadtxt('Data/weights.txt', dtype=float)
company_details = np.load("Data/company_dict.npy").item()

dict_companies={}
dict_companies["Technology"]=["cisco","oracle","adobe","twitch","twitter","indeed.com","workday","dell","netflix","airbnb","apple","tesla","uber","salesforce","facebook","amazon","google","wepay","nvidia","intel corporation","expedia, inc.","netapp","nest","disney","cloudera","hp inc.","lenovo","linkedin","glassdoor","samsung","adp","fitbit","juniper networks","the mathworks","pocket gems"]
dict_companies["Medical"]=["johnson & johnson","ge healthcare","medtronic","baxter healthcare inc","siemens","philips","abbott","stryker medical","becton dickinson","fresenius medical care","st jude hospital","zimmer","terumo medical corporation","varian medical systems","novartis pharmaceuticals","miraca life sciences","dextera surgical","orthoHelix surgical designs","amgen ventures"]
dict_companies["Finance"]=["zestfinance","alfa finance","jpmorgan chase & co","wells fargo","bank of america","citigroup","prudential financial","goldman sachs","american express","allstate","morgan stanley","the travelers companies","abd insurance and financial services","bbva","anz bank australia","usaa","quicken","navy federal credit union","edward jones","capital one","nationwide financial","credit karma"]

features = {}
features['Compensation'] = 0
features["PerkAndBenefits"] = 1
features["Retention"] = 2
features["ProfessionalDevelopment"] = 3
features["Happiness"] = 4
features["Environment"] = 5
features["Leadership"] = 6
features["WorkCulture"] = 7
num_feats = 8

with open('Data/comp.json') as data_file:
    data = json.load(data_file)

def getResults(query):
    x = np.array([0 for i in range(0, num_feats)])
    for key in query:
        if key in features:
            x[features[key]] = float(query[key])
    x = x / np.linalg.norm(x, 2)
    res = np.matmul(x, feat_array)
    total = len(res)
    indices = heapq.nlargest(total, range(len(res)), res.take)

    count = 0
    result = collections.OrderedDict()
    for ind in indices:
        if count == 12:
            break
        if company_details[ind][0].lower() in dict_companies[query["domain"]]:
            result[company_details[ind][0]] = data[company_details[ind][0]]
            count+=1
    return(result)
#
# qu_dict={}
# qu_dict['Compensation'] = "12"
# qu_dict["PerkAndBenefits"] = "12"
# qu_dict["Retention"] = "12"
# qu_dict["ProfessionalDevelopment"] = "12"
# qu_dict["Happiness"] = "12"
# qu_dict["Environment"] = "12"
# qu_dict["Leadership"] = "12"
# qu_dict["WorkCulture"] = "12"
# qu_dict["domain"] = "Technology"
#
# print(getResults(qu_dict))