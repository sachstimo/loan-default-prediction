import pandas as pd
 

### --- Preprocessing functions ###

def process_year_month_date(df, col_names):
    """
    Convert string date columns (e.g., '2005-01-23') to datetime format using vectorized operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing date columns
        col_names (str or list): Column name(s) with imto convert to datetime
        
    Returns:
        pandas.DataFrame: DataFrame with converted date columns
    """
    if isinstance(col_names, str):
        col_names = [col_names]
    
    if not isinstance(col_names, list):
        raise TypeError('col_names should be a string or a list of column names')
    
    # Check if each column exists in the dataframe
    valid_date_cols = []
    for col in col_names:
        if col in df.columns:
            valid_date_cols.append(col)
        else:
            raise ValueError(f"Column '{col}' not found in DataFrame")
    
    df[valid_date_cols] = df[valid_date_cols].apply(pd.to_datetime, format='%Y-%m-%d', errors='coerce')
    
    return df

def process_month_date(df, col_names):
    """
    Convert string date columns (e.g. 'Jul-2005') to datetime format using vectorized operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing date columns
        col_names (str or list): Column name(s) with dates to convert to datetime
        
    Returns:
        pandas.DataFrame: DataFrame with converted date columns
    """
    if isinstance(col_names, str):
        col_names = [col_names]
    
    if not isinstance(col_names, list):
        raise TypeError('col_names should be a string or a list of column names')
    
    # Check if each column exists in the dataframe
    valid_date_cols = []
    for col in col_names:
        if col in df.columns:
            valid_date_cols.append(col)
        else:
            raise ValueError(f"Column '{col}' not found in DataFrame")
    
    df[valid_date_cols] = df[valid_date_cols].apply(pd.to_datetime, format='%b-%Y', errors='coerce')
    
    return df

def process_percentages(df, col_names):

    """
    Convert percentage columns (e.g., '5.3%') to float format using vectorized operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing percentage columns
        col_names (str or list): Column name(s) containing to convert to float
        
    Returns:
        pandas.DataFrame: DataFrame with converted percentage columns
    """
    if isinstance(col_names, str):
        col_names = [col_names]
    
    if not isinstance(col_names, list):
        raise TypeError('col_names should be a string or a list of column names')
    
    # Check if each column exists in the dataframe
    valid_percentage_cols = []
    for col in col_names:
        if col in df.columns:
            valid_percentage_cols.append(col)
        else:
            raise ValueError(f"Column '{col}' not found in DataFrame")
    
    df[valid_percentage_cols] = df[valid_percentage_cols].apply(lambda x: x.str.rstrip('%').astype(float) / 100)
    
    return df


def create_target_columns(df, status_col, drop_target = False):
    """
    Create target columns based on the loan status column where active_loan = 1 if the loan is still active and default = 1 if the loan is not fully paid.
    
    Args:
        df (pandas.DataFrame): DataFrame containing loan status column
        status_col (str): Column name containing loan status
        
    Returns:
        pandas.DataFrame: DataFrame with target columns
    """
    df['active_loan'] = df[status_col].apply(lambda x: 0 if x in ['Fully Paid', 'Default', 'Charged Off'] else 1)
    df['default'] = df[status_col].apply(lambda x: 0 if x == 'Fully Paid' else 1)

    print('Target columns created: active_loan, default')

    if drop_target:
        df.drop(columns=[status_col], inplace=True)    
    return df
    
def process_term(df, term_col):
    """
    Convert term column (e.g., '36 months') to integer format using vectorized operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing term column
        term_col (str): Column name containing loan term
        
    Returns:
        pandas.DataFrame: DataFrame with converted term column
    """
    if df[term_col].dtype == int:  # Check if the column is already in integer format
        print('Term column already processed.')
    else:
        # Extract numerical part of the term (e.g., '36 months' -> 36)
        df[term_col] = df[term_col].str.extract(r'(\d+)').astype(int)

    return df

def drop_columns(df, drop_cols, verbose = False):
    """
    Custom function to drop columns from a DataFrame if they exist.
    """
    for col in drop_cols:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)
            if verbose:
                print(f"Column {col} dropped from dataset.")
        else:
            if verbose:
                print(f"Column {col} not found. Might have been dropped already.")  

def calculate_loan_end_date(df, issue_date_col, term_col):
    """
    Calculate loan end date based on issue date and loan term in months.
    
    Args:
        df (pandas.DataFrame): DataFrame containing issue date and term columns
        issue_date_col (str): Column name with issue date
        term_col (str): Column name with loan term in months
        
    Returns:
        pandas.DataFrame: DataFrame with a new column `loan_end_date` containing calculated end dates
    """
    # Check if columns exist in the DataFrame
    if issue_date_col not in df.columns or term_col not in df.columns:
        print(f"Error: Columns {issue_date_col} or {term_col} are missing from the DataFrame.")
        return df  # Return original DataFrame if columns are missing
    
    # Convert issue date to datetime and ensure the term is an integer
    df[issue_date_col] = pd.to_datetime(df[issue_date_col], errors='raise')
    df[term_col] = df[term_col].astype(int, errors='raise') 

    # Calculate the loan end date
    df['loan_end_date'] = df.apply(lambda x: x[issue_date_col] + pd.DateOffset(months=int(x[term_col])), axis=1)
    
    return df


def calculate_time_to_maturity(df, maturity_date_col, investment_date):
    """
    Calculate time to maturity in months based on maturity date and investment date.
    
    Args:
        df (pandas.DataFrame): DataFrame containing maturity date column
        maturity_date_col (str): Column name with maturity date
        investment_date (str or datetime): Reference date for time to maturity calculation
        
    Returns:
        pandas.DataFrame: DataFrame with a new column `time_to_maturity` containing time to maturity in months
    """
    # Check if the required column exists in the DataFrame
    if maturity_date_col not in df.columns:
        print(f"Error: Column '{maturity_date_col}' is missing from the DataFrame.")
        return df  # Return the original DataFrame if the column is missing
    
    # Ensure investment_date is a datetime object
    if isinstance(investment_date, str):
        investment_date = pd.to_datetime(investment_date, errors='coerce')
    if not isinstance(investment_date, pd.Timestamp):
        print(f"Error: Invalid investment date: {investment_date}")
        return df  # Return the original DataFrame if investment_date is invalid
    
    # Convert maturity dates to datetime
    df[maturity_date_col] = pd.to_datetime(df[maturity_date_col], errors='coerce')  # Handle invalid maturity dates
    
    # Calculate time to maturity in months
    df['time_to_maturity'] = (df[maturity_date_col] - investment_date).dt.days / 30
    
    return df


### --- Feature Engineering

def create_fico_features(df, verbose = False):
    """
    Create new features based on FICO scores."""
    try:
        df['avg_fico_start'] = (df['fico_range_high'] + df['fico_range_low']) / 2
        df['avg_fico_current'] = (df['last_fico_range_high'] + df['last_fico_range_low']) / 2
        df['fico_diff'] = df['avg_fico_current'] - df['avg_fico_start']
        df['fico_downgrade'] = (df['fico_diff'] < 0).astype(int)

        if verbose:
            print(f'New features created: avg_fico_start, avg_fico_current, fico_diff', 'fico_downgrade')
            print('FICO features summary:')
            print(df[['avg_fico_start', 'avg_fico_current', 'fico_diff', 'fico_downgrade']].describe())

    except KeyError as e:
        print(f"Error: {e}")
    return df


### --- Profit Calculations

def calculate_expected_profit(df, predictions, threshold, historical_fn_rate, recovery_rate=0.05, discount_rate=0.05):
    """Estimate profit for open loans based on historical performance metrics."""
    # Select loans with default probability below threshold
    pred_paid = predictions < threshold
    selected_loans = df[pred_paid].copy()
    
    # If no loans selected, return zeros
    if len(selected_loans) == 0:
        return {
            'purchase_price': 0,
            'num_loans_selected': 0,
            'expected_true_paid_count': 0,
            'expected_default_count': 0,
            'expected_return_true_paid': 0,
            'expected_return_defaults': 0,
            'total_expected_return': 0,
            'expected_profit': 0, 
            'expected_roi': 0,
            'threshold': threshold
        }
    
    # Calculate total purchase price with discount
    total_future_payments = selected_loans['installment'] * selected_loans['time_to_maturity']
    purchase_price_total = total_future_payments.sum() / (1 + discount_rate)

    # Expected counts of paid vs defaulted loans
    num_pred_paid = len(selected_loans)
    expected_true_paid_count = num_pred_paid * (1 - historical_fn_rate)
    expected_default_count = num_pred_paid * historical_fn_rate
    
    # Calculate total future payments
    total_future_value = total_future_payments.sum()
    
    # Expected returns from paid loans (full payment)
    expected_return_true_paid = total_future_value * (1 - historical_fn_rate)
    
    # Expected returns from defaulted (purchased) loans with partial recovery
    expected_return_defaults = purchase_price_total * historical_fn_rate * recovery_rate
    
    # Total expected return
    total_expected_return = expected_return_true_paid + expected_return_defaults
    
    # Expected profit
    expected_profit = total_expected_return - purchase_price_total
    
    # ROI
    roi = expected_profit / purchase_price_total if purchase_price_total > 0 else 0
    
    return {
        'threshold': threshold,
        'total_loans': len(df),
        'num_loans_selected': num_pred_paid,
        'pct_loans_selected': num_pred_paid / len(df),
        'expected_true_paid_count': expected_true_paid_count,
        'expected_default_count': expected_default_count,
        'expected_return_true_paid': expected_return_true_paid,
        'expected_return_defaults': expected_return_defaults,
        'total_expected_return': total_expected_return,
        'purchase_price': purchase_price_total,
        'expected_profit': expected_profit, 
        'expected_roi': roi,
    }

def calculate_profit_thresholds(df, predictions, thresholds, historical_fn_rate, recovery_rate=0.5, discount_rate=0.05):
    """
    Find threshold that maximizes expected profit based on historical metrics.
    
    Args:
        df (DataFrame): DataFrame with open loan data
        predictions (Series): Predicted probabilities of default
        thresholds (list): List of thresholds to evaluate
        historical_fn_rate (float): Historical false negative rate
        recovery_rate (float): Recovery rate for defaulted loans
        discount_rate (float): Discount rate
        
    Returns: Two dataframes
        DataFrame: Results with expected profit for each threshold
        DataFrame: Optimal threshold and expected profit
    """
    results = []
    
    for threshold in thresholds:
        profit_info = calculate_expected_profit(df, predictions, threshold, historical_fn_rate, recovery_rate, discount_rate)

        results.append({
            'threshold': threshold,
            'expected_profit': profit_info['expected_profit'],
            'num_loans': profit_info['num_loans_selected'],
            'expected_roi': profit_info['expected_roi'],
            'total_investment': profit_info['purchase_price']
        })
    
    results_df = pd.DataFrame(results)

    return results_df

def get_best_threshold(thresholds_df, kpi='profit'):
    """
    Find the optimal threshold based on the maximum expected profit.

    Args:
        results_df (DataFrame): DataFrame with expected return on invest for each threshold
        kpi (str): Key performance indicator to maximize (e.g., 'profit', 'roi')

    Output:
        Optimal threshold as float
    """
    
    if len(thresholds_df) > 0 and thresholds_df[f'expected_{kpi}'].max() > 0:
        optimal_idx = thresholds_df[f'expected_{kpi}'].idxmax()
        optimal_result = thresholds_df.iloc[optimal_idx]['threshold']
    else:
        optimal_result = None
    
    return optimal_result

def calculate_break_even_discount(df, predictions, threshold, historical_fn_rate, recovery_rate=0.2, tolerance=0.0001, max_iterations=100):
    """
    Calculate the break-even discount rate that makes expected profit zero.
    
    Args:
        df (DataFrame): DataFrame with open loan data
        predictions (Series): Predicted probabilities of default
        threshold (float): Classification threshold
        historical_fn_rate (float): Historical false negative rate (% of predicted paid that default)
        recovery_rate (float): Recovery rate for defaulted loans
        tolerance (float): Acceptable error margin for break-even point
        max_iterations (int): Maximum number of iterations for binary search
        
    Returns:
        float: Break-even discount rate
    """
    # Select loans with default probability below threshold
    pred_paid = predictions < threshold
    selected_loans = df[pred_paid].copy()
    
    # If no loans selected, cannot calculate
    if len(selected_loans) == 0:
        return None
    
    # Calculate total future value (sum of all expected payments)
    total_future_payments = selected_loans['installment'] * selected_loans['time_to_maturity']
    total_future_value = total_future_payments.sum()
    
    # Binary search for break-even discount rate
    lower_bound = 0.0
    upper_bound = 1.0  # 100% discount is reasonable upper limit
    
    for _ in range(max_iterations):
        # Try middle discount rate
        mid_discount = (lower_bound + upper_bound) / 2
        
        # Calculate purchase price with this discount
        purchase_price = total_future_value / (1 + mid_discount)
        
        # Expected returns from paid loans (full payment)
        expected_return_true_paid = total_future_value * (1 - historical_fn_rate)
        
        # Expected returns from defaulted loans with partial recovery
        expected_return_defaults = purchase_price * historical_fn_rate * recovery_rate
        
        # Total expected return
        total_expected_return = expected_return_true_paid + expected_return_defaults
        
        # Expected profit
        expected_profit = total_expected_return - purchase_price
        
        # Check if we're at break-even (within tolerance)
        if abs(expected_profit) < tolerance:
            return mid_discount
        
        # Adjust bounds based on profit
        if expected_profit > 0:  # Profit positive -> discount too high
            upper_bound = mid_discount
        else:  # Profit negative -> discount too low
            lower_bound = mid_discount
    
    # Return best approximation after max iterations
    return (lower_bound + upper_bound) / 2