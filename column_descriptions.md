# Loan Dataset Column Descriptions

## Loan Identification
- **Unnamed: 0**: Index or row identifier
- **id**: Unique loan identification number
- **url**: URL for the loan listing
- **issue_d**: Month the loan was funded

## Loan Basic Information
- **loan_amnt**: The listed amount of the loan applied for by the borrower
- **funded_amnt**: The total amount committed to the loan
- **funded_amnt_inv**: The total amount committed by investors for the loan
- **term**: The number of payments on the loan (in months)
- **int_rate**: Interest rate on the loan
- **installment**: The monthly payment owed by the borrower
- **grade**: LC assigned loan grade (A-G)
- **sub_grade**: LC assigned loan subgrade (A1-G5)
- **pymnt_plan**: Indicates if borrower is on a payment plan
- **purpose**: A category provided by the borrower for the loan request
- **title**: The loan title provided by the borrower
- **loan_status**: Current status of the loan
- **application_type**: Indicates if the loan is individual or joint application
- **policy_code**: Publicly available policy code designations

## Borrower Information
- **emp_title**: The job title supplied by the borrower
- **emp_length**: Employment length in years
- **home_ownership**: The home ownership status provided by the borrower
- **annual_inc**: The self-reported annual income provided by the borrower
- **verification_status**: Indicates if the borrower's income was verified by LC
- **dti**: Debt-to-Income ratio
- **zip_code**: The first 3 numbers of the zip code provided by the borrower
- **addr_state**: The state provided by the borrower in the loan application

## Joint Applicant Information
- **annual_inc_joint**: Combined annual income of co-borrowers
- **dti_joint**: Combined debt-to-income ratio
- **verification_status_joint**: Indicates if the co-borrowers' incomes were verified
- **revol_bal_joint**: Combined revolving balance of the co-borrowers
- **sec_app_fico_range_low**: Co-borrower FICO score lower range
- **sec_app_fico_range_high**: Co-borrower FICO score upper range
- **sec_app_earliest_cr_line**: Co-borrower earliest credit line opening date
- **sec_app_inq_last_6mths**: Co-borrower number of inquiries in last 6 months
- **sec_app_mort_acc**: Co-borrower number of mortgage accounts
- **sec_app_open_acc**: Co-borrower number of open credit accounts
- **sec_app_revol_util**: Co-borrower revolving credit utilization
- **sec_app_open_act_il**: Co-borrower number of currently active installment accounts
- **sec_app_num_rev_accts**: Co-borrower number of revolving accounts
- **sec_app_chargeoff_within_12_mths**: Co-borrower charge-offs within last 12 months
- **sec_app_collections_12_mths_ex_med**: Co-borrower collections excluding medical in last 12 months

## Credit History
- **earliest_cr_line**: The month the borrower's earliest reported credit line was opened
- **fico_range_low**: The lower boundary of the borrower's FICO range
- **fico_range_high**: The upper boundary of the borrower's FICO range
- **last_fico_range_low**: The lower boundary of the borrower's last reported FICO range
- **last_fico_range_high**: The upper boundary of the borrower's last reported FICO range
- **delinq_2yrs**: Number of 30+ days past-due payments in the past 2 years
- **inq_last_6mths**: Number of credit inquiries in past 6 months
- **mths_since_last_delinq**: Months since most recent delinquency
- **mths_since_last_record**: Months since most recent public record
- **open_acc**: Number of open credit lines
- **pub_rec**: Number of derogatory public records
- **revol_bal**: Total credit revolving balance
- **revol_util**: Revolving line utilization rate
- **total_acc**: Total number of credit lines in the borrower's credit file
- **collections_12_mths_ex_med**: Number of collections excluding medical in last 12 months
- **mths_since_last_major_derog**: Months since most recent 90-day or worse rating
- **pub_rec_bankruptcies**: Number of public record bankruptcies
- **tax_liens**: Number of tax liens

## Detailed Credit Metrics
- **acc_now_delinq**: Number of accounts currently delinquent
- **tot_coll_amt**: Total collection amounts ever owed
- **tot_cur_bal**: Total current balance of all accounts
- **open_acc_6m**: Number of open credit lines in last 6 months
- **open_act_il**: Number of currently active installment accounts
- **open_il_12m**: Number of installment accounts opened in past 12 months
- **open_il_24m**: Number of installment accounts opened in past 24 months
- **mths_since_rcnt_il**: Months since most recent installment account opened
- **total_bal_il**: Total current balance of all installment accounts
- **il_util**: Ratio of installment accounts balance to credit limit
- **open_rv_12m**: Number of revolving accounts opened in past 12 months
- **open_rv_24m**: Number of revolving accounts opened in past 24 months
- **max_bal_bc**: Maximum current balance owed on all revolving accounts
- **all_util**: Balance to credit limit for all accounts
- **total_rev_hi_lim**: Total revolving high credit/credit limit
- **inq_fi**: Number of personal finance inquiries
- **total_cu_tl**: Number of credit union trades
- **inq_last_12m**: Number of credit inquiries in past 12 months
- **acc_open_past_24mths**: Number of trades opened in past 24 months
- **avg_cur_bal**: Average current balance of all accounts
- **bc_open_to_buy**: Total open to buy on revolving accounts
- **bc_util**: Ratio of credit card balance to credit limit
- **chargeoff_within_12_mths**: Number of charge-offs within 12 months
- **delinq_amnt**: Amount past due
- **mo_sin_old_il_acct**: Months since oldest installment account opened
- **mo_sin_old_rev_tl_op**: Months since oldest revolving account opened
- **mo_sin_rcnt_rev_tl_op**: Months since most recent revolving account opened
- **mo_sin_rcnt_tl**: Months since most recent account opened
- **mort_acc**: Number of mortgage accounts
- **mths_since_recent_bc**: Months since most recent credit card account opened
- **mths_since_recent_bc_dlq**: Months since most recent credit card delinquency
- **mths_since_recent_inq**: Months since most recent inquiry
- **mths_since_recent_revol_delinq**: Months since most recent revolving delinquency
- **num_accts_ever_120_pd**: Number of accounts ever 120+ days past due
- **num_actv_bc_tl**: Number of currently active credit card accounts
- **num_actv_rev_tl**: Number of currently active revolving trades
- **num_bc_sats**: Number of satisfactory credit card accounts
- **num_bc_tl**: Number of credit card accounts
- **num_il_tl**: Number of installment accounts
- **num_op_rev_tl**: Number of open revolving accounts
- **num_rev_accts**: Number of revolving accounts
- **num_rev_tl_bal_gt_0**: Number of revolving accounts with balance > 0
- **num_sats**: Number of satisfactory accounts
- **num_tl_120dpd_2m**: Number of accounts currently 120+ days past due
- **num_tl_30dpd**: Number of accounts currently 30+ days past due
- **num_tl_90g_dpd_24m**: Number of accounts 90+ days past due in last 24 months
- **num_tl_op_past_12m**: Number of accounts opened in past 12 months
- **pct_tl_nvr_dlq**: Percent of trades never delinquent
- **percent_bc_gt_75**: Percentage of credit card accounts > 75% of limit
- **tot_hi_cred_lim**: Total high credit/credit limit
- **total_bal_ex_mort**: Total account balance excluding mortgage
- **total_bc_limit**: Total credit card credit limit
- **total_il_high_credit_limit**: Total installment high credit/credit limit

## Payment Information
- **out_prncp**: Remaining outstanding principal
- **out_prncp_inv**: Remaining outstanding principal for investors
- **total_pymnt**: Payments received to date for the loan
- **total_pymnt_inv**: Payments received to date for portion of the loan funded by investors
- **total_rec_prncp**: Principal received to date
- **total_rec_int**: Interest received to date
- **total_rec_late_fee**: Late fees received to date
- **recoveries**: Post charge off gross recovery
- **collection_recovery_fee**: Collection recovery fee
- **last_pymnt_d**: Last month payment was received
- **last_pymnt_amnt**: Last total payment amount received
- **next_pymnt_d**: Next scheduled payment date
- **last_credit_pull_d**: The most recent month LC pulled credit for this loan
- **initial_list_status**: Initial listing status of the loan (W=Waiting, F=Fractional)

## Hardship Information
- **hardship_flag**: Indicates if a borrower has a hardship plan in place
- **hardship_type**: Type of hardship plan
- **hardship_reason**: Reason for the hardship
- **hardship_status**: Status of the hardship plan
- **deferral_term**: Amount of months the borrower is expected to pay under the hardship plan
- **hardship_amount**: The amount the borrower's payment was reduced by under the hardship plan
- **hardship_start_date**: The start date of the hardship plan
- **hardship_end_date**: The end date of the hardship plan
- **payment_plan_start_date**: The day the first payment is due under the hardship plan
- **hardship_length**: The number of months the borrower will make reduced payments
- **hardship_dpd**: Account days past due as of the hardship plan start date
- **hardship_loan_status**: Loan status as of the hardship plan start date
- **orig_projected_additional_accrued_interest**: The original projected additional interest that will accrue for the given hardship payment plan
- **hardship_payoff_balance_amount**: The payoff balance amount as of the hardship plan start date
- **hardship_last_payment_amount**: The last payment amount as of the hardship plan start date
- **debt_settlement_flag**: Indicates if a debt settlement is in place
