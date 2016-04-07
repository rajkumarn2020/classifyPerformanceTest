# -*- coding: utf-8 -*-
import unittest
import requests
import json
import xmlrunner
import csv

class InequalityTest(unittest.TestCase):

  def Ontobi_API(self, S1):
        url = 'http://52.72.120.188:8080/classify'
        payload = {"msgId":"hello","bodyS1":S1}
        headers = {'content-type': 'application/json'}
        session = requests.Session()
        r = session.post(url, data = json.dumps(payload), headers = headers)
        j = r.json()
        output = j["data"]["categories"][0]["id"]
        return output

  def test_IsClassify_many(self):
   presig=open('classifyUnitTests.csv')
   Presigs=csv.DictReader(presig)
   BODYS1=[]
   CATID=[]
   for row in Presigs:
    CATID.append(row['categoryId'])
    BODYS1.append(row['bodyS1'])
   presig.close()
   lenPRESIG=len(CATID)

   for i in range(1,lenPRESIG):
    expected = CATID[i]
    bodys1=BODYS1[i]
    Actuval=self.Ontobi_API(bodys1)
    print(Actuval)
    #self.assertEqual(Actuval, int(expected))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InequalityTest)
    xmlrunner.XMLTestRunner(output='test-reports3').run(suite)