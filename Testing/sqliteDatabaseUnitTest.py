import unittest
import pandas as pd
from sqliteDatabase import sqliteDatabase as database

class unitTestingBreastCancerClass(unittest.TestCase):

    def testPatientTable(self):
        databaseObject = database()
        databaseObject.dropTable("patient")
        databaseObject.createPatientTable()
        rowCountPatientTable = databaseObject.getRowCount("patient")
        rowCountPatientCsvData = len(pd.read_csv('patients.csv', sep=","))
        self.assertEqual(rowCountPatientTable, rowCountPatientCsvData)
        
    def testConditionTable(self):
        databaseObject = database()
        databaseObject.dropTable("condition")
        databaseObject.createConditionTable()
        rowCountConditionTable = databaseObject.getRowCount("condition")
        rowCountConditionCsvData = len(pd.read_csv('conditions.csv', sep=","))
        self.assertEqual(rowCountConditionTable, rowCountConditionCsvData)
    
    def testProcedureTable(self):
        databaseObject = database()
        databaseObject.dropTable("procedure")
        databaseObject.createProcedureTable()
        rowCountProcedureTable      = databaseObject.getRowCount("procedure")
        rowCountProcedureCsvData    = len(pd.read_csv('procedures.csv', sep=","))
        self.assertEqual(rowCountProcedureCsvData, rowCountProcedureTable)
    
    def testMedicationTable(self):
        databaseObject = database()
        databaseObject.dropTable("medication")
        databaseObject.createMedicationTable()
        rowCountMedicationTable      = databaseObject.getRowCount("medication")
        rowCountMedicationCsvData    = len(pd.read_csv('medications.csv', sep=","))
        self.assertEqual(rowCountMedicationCsvData, rowCountMedicationTable)
    
    def testObservationTable(self):
        databaseObject = database()
        databaseObject.dropTable("observation")
        databaseObject.createObservationTable()
        rowCountObservationTable      = databaseObject.getRowCount("observation")
        rowCountObservationCsvData    = len(pd.read_csv('observations.csv', sep=","))
        self.assertEqual(rowCountObservationCsvData, rowCountObservationTable)
    
if __name__ == '__main__':
    unittest.main()
