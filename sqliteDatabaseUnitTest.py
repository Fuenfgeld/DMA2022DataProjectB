import unittest
import pandas as pd
from sqliteDatabase import sqliteDatabase as database

class unitTestingBreastCancerClass(unittest.TestCase):

    def testPatientTable(self):
        databaseObject = database()
        databaseObject.dropTable("patient")
        databaseObject.createPatientTable()
        rowCountPatientTable = databaseObject.getRowCount("patient")
        rowCountPatientCsvData = len(pd.read_csv('BreastCancerData/patients.csv', sep=","))
        self.assertEqual(rowCountPatientTable, rowCountPatientCsvData)
        
    def testConditionTable(self):
        databaseObject = database()
        databaseObject.dropTable("condition")
        databaseObject.createConditionTable()
        rowCountConditionTable = databaseObject.getRowCount("condition")
        rowCountConditionCsvData = len(pd.read_csv('BreastCancerData/conditions.csv', sep=","))
        self.assertEqual(rowCountConditionTable, rowCountConditionCsvData)
    
    def testProcedureTable(self):
        databaseObject = database()
        databaseObject.dropTable("procedure")
        databaseObject.createProcedureTable()
        rowCountProcedureTable      = databaseObject.getRowCount("procedure")
        rowCountProcedureCsvData    = len(pd.read_csv('BreastCancerData/procedures.csv', sep=","))
        self.assertEqual(rowCountProcedureCsvData, rowCountProcedureTable)
    
if __name__ == '__main__':
    unittest.main()