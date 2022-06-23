import sqlite3
import pandas as pd

class sqliteDatabase:
    
    def __init__(self):
        self.createConnection()
        self.dropTables()
        self.createAllTables()
    
    def createAllTables(self):
        self.createConditionTable()
        self.createMedicationTable()
        self.createObservationTable()
        self.createPatientTable()
        self.createProcedureTable()
    
    def createConnection(self):
        self.connection = sqlite3.connect('breast_cancer.sqlite')
        result = self.checkConnection()
        if(not result):
            print("Datenbank wurde nicht erfolgreich geöffnet");
    
    def checkConnection(self):
        try:
            self.cursor = self.connection.cursor()
            return True
        except Exception as ex:
            return False

    def getRowCount(self, tableName):
        #Achtung Sicherheitslücke! Statdessen prepared Statemenets nutzen
        self.cursor.execute("SELECT * from " + tableName)
        return len(self.cursor.fetchall())
    
    def dropTables(self):
        self.cursor.execute("DROP TABLE IF EXISTS patient")
        self.cursor.execute("DROP TABLE IF EXISTS condition")
        self.cursor.execute("DROP TABLE IF EXISTS medication")
        self.cursor.execute("DROP TABLE IF EXISTS observation")
        self.cursor.execute("DROP TABLE IF EXISTS procedures")
    
    def dropTable(self, tableName):
        self.cursor.execute("DROP TABLE IF EXISTS " + tableName)
        
    def createPatientTable(self): 
        patient = pd.read_csv('BreastCancerData/patients.csv', sep=",")
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS patient (
                    Id nvarchar(36) primary key,
                    BIRTHDATE Date,
                    DEATHDATE Date,
                    SSN nvarchar(50),
                    DRIVERS nvarchar(50),
                    PASSPORT nvarchar(10),
                    PREFIX nvarchar(3),
                    FIRST nvarchar(50),
                    LAST nvarchar(50),
                    SUFFIX nvarchar(50),
                    MAIDEN nvarchar(50),
                    MARITAL nvarchar(1),
                    RACE nvarchar(10),
                    ETHNICITY nvarchar(20),
                    GENDER nvarchar(2),
                    BIRTHPLACE nvarchar(50),
                    ADDRESS nvarchar(50),
                    CITY nvarchar(50),
                    STATE nvarchar(50),
                    COUNTY nvarchar(50),
                    ZIP nvarchar(4),
                    LAT nvarchar(10),
                    LON nvarchar(10),
                    HEALTHCARE_EXPENSES float,
                    HEALTHCARE_COVERAGE float
                
                    )
                    ''')
        rowCountPatient = patient.to_sql('patient', self.connection, if_exists='append', index=False)
        return rowCountPatient

    def createConditionTable(self): 
        condition = pd.read_csv('BreastCancerData/conditions.csv', sep=",")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS condition (
                START Date,
                STOP Date,
                PATIENT nvarchar(36),
                ENCOUNTER nvarchar(50),
                DESCRIPTION nvarchar(50),
                CODE int,
                foreign key(PATIENT) references patient(Id) 
                )
                ''')
        rowCountCondition = condition.to_sql('condition', self.connection, if_exists='append', index=False)
        return rowCountCondition

    def createMedicationTable(self): 
        medication = pd.read_csv('BreastCancerData/medications.csv', sep=",")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS medication (
                START nvarchar(20),
                STOP nvarchar(20),
                PATIENT nvarchar(36),
                PAYER nvarchar(50),
                ENCOUNTER nvarchar(50),
                CODE int,
                DESCRIPTION nvarchar(50),
                BASE_COST float,
                PAYER_COVERAGE float,
                DISPENSES int,
                TOTALCOST float,
                REASONCODE float,
                REASONDESCRIPTION nvarchar(50),
                foreign key(PATIENT) references patient(Id) 
                )
                ''')
        medication.to_sql('medication', self.connection, if_exists='append', index=False)

        
        
    def createObservationTable(self):
        observation = pd.read_csv('BreastCancerData/observations.csv', sep=",")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS observation (
                DATE nvarchar(20),
                PATIENT nvarchar(36),
                ENCOUNTER nvarchar(50),
                CODE int,
                DESCRIPTION nvarchar(50),
                VALUE float,
                UNITS nvarchar(10),
                TYPE nvarchar(10),
                foreign key(PATIENT) references patient(Id) 
                )
                ''')
        observation.to_sql('observation', self.connection, if_exists='append', index=False)

    def createProcedureTable(self): 
        procedure = pd.read_csv('BreastCancerData/procedures.csv', sep=",")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS procedure (
                DATE nvarchar(20),
                PATIENT nvarchar(36),
                ENCOUNTER nvarchar(50),
                CODE int,
                DESCRIPTION nvarchar(50),
                BASE_COST float,
                REASONCODE float,
                REASONDESCRIPTION nvarchar(50),
                foreign key(PATIENT) references patient(Id) 
                )
                ''')
        procedure.to_sql('procedure', self.connection, if_exists='append', index=False)


    def createPatientCareplanTable(self): 
       
        self.cursor.execute('''
           CREATE TABLE IF NOT EXISTS patient_careplan (
            careplan_id INTEGER PRIMARY KEY AUTOINCREMENT,
			PATIENT_ID nvarchar(36),
            CARE_TYPE nvarchar(20),
            DESCRIPTION nvarchar(50),
            RESON nvarchar(50),
            ENCOUNTER nvarchar(50),
            DATE Date,
            foreign key(PATIENT_ID) references patient(Id) 
			)
             ''')
      
        self.cursor.execute('''
            INSERT INTO patient_careplan(PATIENT_ID,CARE_TYPE, DESCRIPTION,RESON,ENCOUNTER,DATE)
            SELECT patient.Id as PATIENT_ID, 'Medication' as CARE_TYPE, medication.DESCRIPTION, medication.REASONCODE as RESON, medication.ENCOUNTER, medication.START as DATE
            FROM patient 
            INNER JOIN 
            medication ON patient.Id = medication.PATIENT
    
            UNION
            SELECT patient.Id as PATIENT_ID,'Observation' as CARE_TYPE, observation.DESCRIPTION, observation.CODE as RESON, observation.ENCOUNTER, observation.DATE
            FROM patient 
            INNER JOIN 
            observation ON patient.Id = observation.PATIENT
            
            UNION
            SELECT patient.Id as PATIENT_ID, 'Procedure' as CARE_TYPE, procedure.DESCRIPTION, procedure.REASONDESCRIPTION as RESON, procedure.ENCOUNTER, procedure.DATE
            FROM patient 
            INNER JOIN 
            procedure ON patient.Id = procedure.PATIENT
            ''')
            
