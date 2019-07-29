from flask import Flask, render_template, request
import mlcode_new
import pandas as pd

app = Flask(__name__,template_folder='template')

@app.route('/')
def myfunction():
    return render_template('index.html')
def home():
		return render_template('index.html')
		
@app.route('/about')
def about():
		return render_template('about.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')
@app.route('/bank')
def bank():
    return render_template('bank.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')
	
@app.route('/dashboard2')	
def dashboard2():
    return render_template('dashboard2.html')
	
@app.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html')
@app.route('/home')
def home1():
		return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def DefaulterorNot():
       
    NAME_INCOME_TYPE = request.form.get('NAME_INCOME_TYPE')
    print("NAME_INCOME_TYPE : {}    {}".format(NAME_INCOME_TYPE,type(NAME_INCOME_TYPE)))

    AMT_CREDIT = float(request.form.get('AMT_CREDIT'))
    print("AMT_CREDIT : {}    {}".format(AMT_CREDIT, type(AMT_CREDIT)))

    NAME_FAMILY_STATUS = request.form.get('NAME_FAMILY_STATUS')
    print("NAME_FAMILY_STATUS : {}    {}".format(NAME_FAMILY_STATUS, type(NAME_FAMILY_STATUS)))

    CODE_GENDER = request.form.get('CODE_GENDER')
    print("CODE_GENDER : {}    {}".format(CODE_GENDER, type(CODE_GENDER)))

    FLAG_DOCUMENT_3 = int(request.form.get('FLAG_DOCUMENT_3'))
    print("FLAG_DOCUMENT_3 : {}    {}".format(FLAG_DOCUMENT_3, type(FLAG_DOCUMENT_3)))

    REGION_RATING_CLIENT = int(request.form.get('REGION_RATING_CLIENT'))
    print(" REGION_RATING_CLIENT : {}    {}".format( REGION_RATING_CLIENT, type(REGION_RATING_CLIENT)))

    NAME_HOUSING_TYPE = request.form.get('NAME_HOUSING_TYPE')
    print(" NAME_HOUSING_TYPE : {}    {}".format( NAME_HOUSING_TYPE, type(NAME_HOUSING_TYPE)))

    CNT_FAM_MEMBERS = float(request.form.get('CNT_FAM_MEMBERS'))
    print(" CNT_FAM_MEMBERS : {}    {}".format( CNT_FAM_MEMBERS, type(CNT_FAM_MEMBERS)))

    OCCUPATION_TYPE = request.form.get('OCCUPATION_TYPE')
    print(" OCCUPATION_TYPE : {}    {}".format( OCCUPATION_TYPE, type(OCCUPATION_TYPE)))

    DAYS_BIRTH = int(request.form.get('DAYS_BIRTH'))
    DAYS_BIRTH = DAYS_BIRTH*(-365)
    print(" DAYS_BIRTH : {}    {}".format( DAYS_BIRTH, type(DAYS_BIRTH)))

    DAYS_EMPLOYED = int(request.form.get('DAYS_EMPLOYED'))
    DAYS_EMPLOYED = DAYS_EMPLOYED*(-30)
    print(" DAYS_EMPLOYED : {}    {}".format( DAYS_EMPLOYED, type(DAYS_EMPLOYED)))

    AMT_INCOME_TOTAL = float(request.form.get('AMT_INCOME_TOTAL'))
    print(" AMT_INCOME_TOTAL : {}    {}".format( AMT_INCOME_TOTAL, type(AMT_INCOME_TOTAL)))

    NAME_CONTRACT_TYPE = request.form.get('NAME_CONTRACT_TYPE')
    print(" NAME_CONTRACT_TYPE : {}    {}".format( NAME_CONTRACT_TYPE, type(NAME_CONTRACT_TYPE)))

    AMT_ANNUITY = float(35698.5)
    print(" AMT_ANNUITY : {}    {}".format( AMT_ANNUITY, type(AMT_ANNUITY)))

    FLAG_DOCUMENT_7 = int(request.form.get('FLAG_DOCUMENT_7'))
    print(" FLAG_DOCUMENT_7 : {}    {}".format( FLAG_DOCUMENT_7, type(FLAG_DOCUMENT_7)))

    NAME_EDUCATION_TYPE = request.form.get('NAME_EDUCATION_TYPE')
    print(" NAME_EDUCATION_TYPE : {}    {}".format( NAME_EDUCATION_TYPE, type(NAME_EDUCATION_TYPE)))
    
    DOCUMENT_17 = request.form.get('FLAG_DOCUMENT_17')
    if not DOCUMENT_17 :
        FLAG_DOCUMENT_17 = 0
    else:
        FLAG_DOCUMENT_17 = 1
    print(" FLAG_DOCUMENT_17 : {}    {}".format( FLAG_DOCUMENT_17, type(FLAG_DOCUMENT_17)))
    
    EXT_SOURCE_2 = float(request.form.get('EXT_SOURCE_2'))
    EXT_SOURCE_2 = EXT_SOURCE_2/1000000
    print(" EXT_SOURCE_2 : {}    {}".format( EXT_SOURCE_2, type(EXT_SOURCE_2)))
    
    EXT_SOURCE_3 = float(request.form.get('EXT_SOURCE_3'))
    EXT_SOURCE_3 = EXT_SOURCE_3/1000000
    print(" EXT_SOURCE_3 : {}    {}".format( EXT_SOURCE_3, type(EXT_SOURCE_3)))
    
    DAYS_ID_PUBLISH = int(request.form.get('DAYS_ID_PUBLISH'))
    DAYS_ID_PUBLISH = DAYS_ID_PUBLISH*(-30)
    print(" DAYS_ID_PUBLISH : {}    {}".format( DAYS_ID_PUBLISH, type(DAYS_ID_PUBLISH)))
    
    AMT_GOODS_PRICE = float(request.form.get('AMT_GOODS_PRICE'))
    print(" AMT_GOODS_PRICE : {}    {}".format( AMT_GOODS_PRICE, type(AMT_GOODS_PRICE)))
	
    status = int(request.form.get('status'))
    print("status : {}    {}".format(status, type(status)))
	
    print("creating dataframe")
    #creating test dataframe using input from user    
    test_obs = pd.DataFrame({'NAME_CONTRACT_TYPE': NAME_CONTRACT_TYPE,'CODE_GENDER': CODE_GENDER,'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL,
                'AMT_CREDIT': AMT_CREDIT,'AMT_ANNUITY': AMT_ANNUITY,'AMT_GOODS_PRICE': AMT_GOODS_PRICE,'NAME_INCOME_TYPE': NAME_INCOME_TYPE,
                'NAME_EDUCATION_TYPE': NAME_EDUCATION_TYPE,'NAME_FAMILY_STATUS':NAME_FAMILY_STATUS,'NAME_HOUSING_TYPE': NAME_HOUSING_TYPE,
                'DAYS_BIRTH': DAYS_BIRTH,'DAYS_EMPLOYED': DAYS_EMPLOYED,'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,
                'OCCUPATION_TYPE': OCCUPATION_TYPE,'CNT_FAM_MEMBERS': CNT_FAM_MEMBERS,'REGION_RATING_CLIENT': REGION_RATING_CLIENT,
                'EXT_SOURCE_2': EXT_SOURCE_2,'EXT_SOURCE_3': EXT_SOURCE_3,'FLAG_DOCUMENT_3':FLAG_DOCUMENT_3,'FLAG_DOCUMENT_7':FLAG_DOCUMENT_7,
                'FLAG_DOCUMENT_17':FLAG_DOCUMENT_17}, index=[0]) 

    #dummying the dataframe	
	#C:/Users/WIN10/Desktop/credit/imputed_app_train_ui.csv''
    test_obs = pd.get_dummies(test_obs,drop_first=True)    
    print("before alignment")
    imputed_train_new=pd.read_csv('C:/Users/dbda/Desktop/Project/credit/imputed_app_train_ui.csv')
    train_labels=imputed_train_new['TARGET']
    imputed_train_new.drop(['SK_ID_CURR','TARGET'], inplace=True, axis=1)
    imputed_train_new, test_obs = imputed_train_new.align(test_obs, join = 'inner', axis = 1)
	
    print("after alignment")
    classifier = mlcode_new.CatBoostingClassification(imputed_train_new,train_labels) 
    prediction = classifier.predict(test_obs)

    if prediction[0] == 0:
        if status==0:
            prediction ='Loan can be granted!'
        else:
            prediction ='You can come to bank with for further proceedings!'
    else:
        if status==0:
            prediction ='Can be a defaulter'
        else:
            prediction='Sorry! Loan will not be granted!'
    print(prediction)
    print(prediction[0])
	
    return render_template('result.html', prediction=prediction)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
