# Loan-Defaulter-Prediction

###HOW TO INTERPRET BUREAU DATA
This table talks about the Loan data of each unique customer with all financial institutions other than Home Credit For each unique SK_ID_CURR we have multiple SK_ID_BUREAU Id's, each being a unique loan transaction from other financial institutions availed by the same customer and reported to the bureau.

#UNDERSTANDING OF VARIABLES
CREDIT_ACTIVE - Current status of a Loan - Closed/ Active (2 values)

CREDIT_CURRENCY - Currency in which the transaction was executed - Currency1, Currency2, Currency3, Currency4 ( 4 values)

CREDIT_DAY_OVERDUE - Number of overdue days

CREDIT_TYPE - Consumer Credit, Credit card, Mortgage, Car loan, Microloan, Loan for working capital replemishment, Loan for Business development, Real estate loan, Unkown type of laon, Another type of loan. Cash loan, Loan for the purchase of equipment, Mobile operator loan, Interbank credit, Loan for purchase of shares ( 15 values )

DAYS_CREDIT - Number of days ELAPSED since customer applied for CB credit with respect to current application Interpretation - Are these loans evenly spaced time intervals? Are they concentrated within a same time frame?

DAYS_CREDIT_ENDDATE - Number of days the customer CREDIT is valid at the time of application CREDIT_DAY_OVERDUE - Number of days the customer CREDIT is past the end date at the time of application

AMT_CREDIT_SUM - Total available credit for a customer AMT_CREDIT_SUM_DEBT - Total amount yet to be repayed AMT_CREDIT_SUM_LIMIT - Current Credit that has been utilized AMT_CREDIT_SUM_OVERDUE - Current credit payment that is overdue CNT_CREDIT_PROLONG - How many times was the Credit date prolonged

NOTE:
For a given loan transaction 'AMT_CREDIT_SUM' = 'AMT_CREDIT_SUM_DEBT' +'AMT_CREDIT_SUM_LIMIT'

AMT_ANNUITY - Annuity of the Credit Bureau data DAYS_CREDIT_UPDATE - Number of days before current application when last CREDIT UPDATE was received DAYS_ENDDATE_FACT - Days since CB credit ended at the time of application AMT_CREDIT_MAX_OVERDUE - Maximum Credit amount overdue at the time of application
