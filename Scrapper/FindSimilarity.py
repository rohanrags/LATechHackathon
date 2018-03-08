import json
import heapq
import numpy as np

def gradesToIndex(grade):
   if grade=="F":
       return 0
   elif grade=="D-":
       return 1
   elif grade == "D":
       return 2
   elif grade == "D+":
       return 3
   elif grade == "C-":
       return 4
   elif grade == "C":
       return 5
   elif grade == "C+":
       return 6
   elif grade == "B-":
       return 7
   elif grade == "B":
       return 8
   elif grade == "B+":
       return 9
   elif grade == "A-":
       return 10
   elif grade == "A":
       return 11
   elif grade == "A+":
       return 12
   else:
       return -1


with open('Data/comp.json') as data_file:
    data = json.load(data_file)


features={}

# for dat in data:
#     for feat in data[dat]:
#         if feat not in features:
#             features[feat] = len(features)

features['Compensation'] = 0
features["PerkAndBenefits"] = 1
features["Retention"] = 2
features["ProfessionalDevelopment"] = 3
#features["eNPS"] = 4
#features["Sentiment"] = 4
features["Happiness"] = 4
features["Environment"] = 5
features["Leadership"] = 6
#features["CEORating"] = 6
#features["ExecutiveTeam"]=6
#features["Manager"]=6
features["WorkCulture"]=7
#features["OfficeCulture"]=7

num_feats = 8
company_details={}
company_features=[]
for dat in data:
    company_details[len(company_features)] = (dat, data[dat]["company_url"])
    feat = [0 for i in range(0,num_feats)]
    count = [0 for i in range(0,num_feats)]
    for fe in data[dat]:
        if (fe in features):
            feat[features[fe]] +=  gradesToIndex(data[dat][fe])
            count[features[fe]] += 1

    for index in range(0,len(feat)):
        if (count[index] != 0):
            feat[index] = float(feat[index])/count[index]
    norm = np.linalg.norm(feat,2)
    if(norm != 0):
        feat = feat/norm
    company_features.append(feat)


feat_array = np.transpose(np.array(company_features))
np.savetxt('data/weights.txt',feat_array, fmt='%10.5f')
np.save("data/company_dict.npy",company_details)

# print(np.shape(feat_array))
# print(len(company_details))


