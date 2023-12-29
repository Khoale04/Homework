sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# adict = {"a": 1, "b": 12}
# print(adict['a'])
# print(sampleDict)
# print(sampleDict.keys())
# print(sampleDict.values())
print(sampleDict['class'])
sample2 = sampleDict['class']
print(sample2['student'])
print(sample2['student']['marks'])
print(sample2['student']['marks']['history'])