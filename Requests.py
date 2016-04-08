# -*- coding: utf-8 -*-
import unittest
import requests
import json
import xmlrunner
import csv
import datetime

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


  def test_IsClassify_PerformanceTest(self):
   print("Loading....")
   ClassifyDoc=open('classifyUnitTests.csv')
   GivenInputs=csv.DictReader(ClassifyDoc)
   BODYS1=[]
   CATID=[]
   for row in GivenInputs:
    CATID.append(row['categoryId'])
    BODYS1.append(row['bodyS1'])
   ClassifyDoc.close()
   lenInputRows=len(CATID)

   #StartTime
   StartTime = datetime.datetime.now()

   for i in range(1,lenInputRows):
    expected = CATID[i]
    bodys1=BODYS1[i]
    Actuval=self.Ontobi_API(bodys1)

   #EndTime
   EndTime = datetime.datetime.now()
   #TakenTime
   TimeTaken=EndTime-StartTime
   #InSeconds
   TakenSeconds=int(TimeTaken.total_seconds())
   self.assertTrue(TakenSeconds<10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InequalityTest)
    xmlrunner.XMLTestRunner(output='test-reports').run(suite)