import secrets
from flask import Flask, render_template, request
import pickle
import pandas as pd

# Loading the trained model
model = pickle.load(open('credit_scores_MLproj.pkl', 'rb'))
# Generate a random secret key
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Getting data from form
        data = {
            'Age': [request.form.get('Age')],
            'Month': [request.form.get('Month')],
            'Occupation': [request.form.get('Occupation')],
            'Annual_Income': [request.form.get('Annual_Income')],
            'Monthly_Inhand_Salary': [request.form.get('Monthly_Inhand_Salary')],
            'Num_Bank_Accounts': [request.form.get('Num_Bank_Accounts')],
            'Num_Credit_Card': [request.form.get('Num_Credit_Card')],
            'Interest_Rate': [request.form.get('Interest_Rate')],
            'Delay_from_due_date': [request.form.get('Delay_from_due_date')],
            'Num_of_Delayed_Payment': [request.form.get('Num_of_Delayed_Payment')],
            'Changed_Credit_Limit': [request.form.get('Changed_Credit_Limit')],
            'Num_Credit_Inquiries': [request.form.get('Num_Credit_Inquiries')],
            'Credit_Mix': [request.form.get('Credit_Mix')],
            'Outstanding_Debt': [request.form.get('Outstanding_Debt')],
            'Credit_Utilization_Ratio': [request.form.get('Credit_Utilization_Ratio')],
            'Credit_History_Age': [request.form.get('Credit_History_Age')],
            'Payment_of_Min_Amount': [request.form.get('Payment_of_Min_Amount')],
            'Total_EMI_per_month': [request.form.get('Total_EMI_per_month')],
            'Amount_invested_monthly': [request.form.get('Amount_invested_monthly')],
            'Payment_Behaviour': [request.form.get('Payment_Behaviour')],
            'Monthly_Balance': [request.form.get('Monthly_Balance')],
            'Count_Auto Loan': [request.form.get('Count_Auto Loan')],
            'Count_Credit-Builder Loan': [request.form.get('Count_Credit-Builder Loan')],
            'Count_Personal Loan': [request.form.get('Count_Personal Loan')],
            'Count_Home Equity Loan': [request.form.get('Count_Home Equity Loan')],
            'Count_Not Specified': [request.form.get('Count_Not Specified')],
            'Count_Mortgage Loan': [request.form.get('Count_Mortgage Loan')],
            'Count_Student Loan': [request.form.get('Count_Student Loan')],
            'Count_Debt Consolidation Loan': [request.form.get('Count_Debt Consolidation Loan')],
            'Count_Payday Loan': [request.form.get('Count_Payday Loan')]
        }
        # Converting data into a DataFrame
        df = pd.DataFrame(data)
        # Using the model to make a prediction
        prediction = model.predict(df)
        return render_template('prediction.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Running the application